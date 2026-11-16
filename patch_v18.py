# Builds v18 (NOT live) from v17: the bench goes back to six amps.
#  - removes 210 / 213 and Custom 280
#  - replaces the M14 (stereo, no reverb) with the M15 (stereo vibrato plus reverb)
#  - M10 stays on two stages (four varistors), using the two-stage curves from the Custom 480 run
import io, hashlib
D = r'C:\Users\Jason\ClaudeNotify\magnatone' + '\\'
rd = lambda p: io.open(p, encoding='utf-8', newline='').read()
src = rd(D + 'post_content_v17.html'); prev = rd(D + 'magnatone_preview_v17.html')
assert src in prev
s = src
def rep(old, new):
    global s
    n = s.count(old); assert n == 1, 'anchor count %d for: %s' % (n, old[:70])
    s = s.replace(old, new)
rep('  m213:{name:"210 / 213 Troubadour",years:"1957 to 1962",stereo:false,stages:1,tank:null,art:"combo",sub:"mono, two varistors, no reverb"},\n', '')
rep('  m280:{name:"Custom 280",years:"1957 to 1962",stereo:true,stages:2,tank:null,art:"wide",sub:"stereo, eight varistors, no reverb"},\n', '')
rep('  m14:{name:"M14 Mighty Midget",years:"1963 to 1965",stereo:true,stages:2,tank:null,art:"suit2",sub:"stereo, eight varistors, no reverb"},',
    '  m15:{name:"M15",years:"1963 to 1965",stereo:true,stages:2,tank:"tM10",art:"suit2",sub:"stereo, eight varistors, reverb"},')
rep('var ORDER=["m213","m280","m413","m480","m10","m14","m30","m35"];', 'var ORDER=["m413","m480","m10","m15","m30","m35"];')
rep('<h4>Eight Magnatones on the bench</h4>', '<h4>Six Magnatones on the bench</h4>')
assert s.count('Eight amps from this story with their actual feature sets') == 2   # compact and detailed copies
s = s.replace('Eight amps from this story with their actual feature sets', 'Six amps from this story with their actual feature sets')
rep('/* ---- the eight amps: documented feature sets ---- */', '/* ---- the six amps: documented feature sets ---- */')
assert '\u2014' not in s and '&mdash;' not in s and 'm213' not in s and 'm280' not in s and '"m14"' not in s
io.open(D + 'post_content_v18.html', 'w', encoding='utf-8', newline='').write(s)
io.open(D + 'magnatone_preview_v18.html', 'w', encoding='utf-8', newline='').write(prev.replace(src, s))
print('ok', len(src), '->', len(s), hashlib.sha256(s.encode('utf-8')).hexdigest())
