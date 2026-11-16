# Builds v23 (NOT live) from v22: in "Inside the Magnatone sweep" the Tremolo depth now follows the size
# of the pitch bend at the centre frequency. 65 cents peak to peak (the 440 at 1 kHz, full depth) keeps the
# old 16.5 dB; everything else is proportional, capped at 30 dB. The graph's auto-scaling is unchanged.
import io, hashlib
D = r'C:\Users\Jason\ClaudeNotify\magnatone' + '\\'
rd = lambda p: io.open(p, encoding='utf-8', newline='').read()
src = rd(D + 'post_content_v22.html'); prev = rd(D + 'magnatone_preview_v22.html')
assert src in prev
s = src
def rep(old, new):
    global s
    n = s.count(old); assert n == 1, 'anchor count %d for: %s' % (n, old[:70])
    s = s.replace(old, new)
rep('  for(i=0;i<N;i++){ var pn=span>0?(tr.c[i]-tr.min)/span:0.5; t.am[i]=1-0.85*depth*(1-pn); }',
    '  /* depth in dB follows the peak-to-peak bend in cents: 65 cents = 16.5 dB, 30 dB at most */\n'
    '  var lo=Math.pow(10,-Math.min(30,16.5*span/65)/20);\n'
    '  for(i=0;i<N;i++){ var pn=span>0?(tr.c[i]-tr.min)/span:0.5; t.am[i]=1-(1-lo)*(1-pn); }')
rep('where it also sets the loudness curve you hear.',
    'where it also sets the loudness curve you hear. Tremolo depth follows the size of the pitch bend at the centre frequency: 65 cents from top to bottom gives about 16.5 dB, a smaller bend gives less, and it stops at 30 dB.')
assert '\u2014' not in s and '&mdash;' not in s
io.open(D + 'post_content_v23.html', 'w', encoding='utf-8', newline='').write(s)
io.open(D + 'magnatone_preview_v23.html', 'w', encoding='utf-8', newline='').write(prev.replace(src, s))
print('ok', len(src), '->', len(s), hashlib.sha256(s.encode('utf-8')).hexdigest())
