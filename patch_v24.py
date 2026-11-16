import io, hashlib
D = 'C:\\Users\\Jason\\ClaudeNotify\\magnatone\\'

NOTE_START = '<p class="iam-note">All three graphs share the same X axis'
NOTE_END = 'Chorus a 50/50 mix with dry.</p>'
NEW_NOTE = ('<p class="iam-note">All three graphs share one time axis, 0 to 500 ms. Left to right: the oscillator\'s control signal, '
            'the resistance of the swept element (100 &Omega; to 10 M&Omega;, log scale), and what the sweep does to a tone at the centre frequency. '
            'The readout gives the peak pitch bend in cents. The centre slider changes the display only, except in Tremolo, '
            'where a bigger bend at that frequency gives a deeper tremolo. Stereo, left red and right orange: the 480 and the M35 use their real second channel; '
            'the 440 was mono, so its stereo is a what-if. The Uni-Vibe is mono; its second switch is the pedal\'s Vibrato or Chorus.</p>')

OLD_READ = ('  if(trem){ el.textContent=(CR?"L ":"")+"0 / "+TL.min.toFixed(1)+" dB"+(CR?"  R 0 / "+TR.min.toFixed(1)+" dB":""); }\n'
            '  else { el.textContent=(CR?"L ":"")+"+"+TL.max.toFixed(0)+" / "+TL.min.toFixed(0)+" cents"+(CR?"  R +"+TR.max.toFixed(0)+" / "+TR.min.toFixed(0)+" cents":"")+" at "+fcLabel(); }')
NEW_READ = ('  /* the readout always shows the pitch bend in cents, in Tremolo too */\n'
            '  el.textContent=(PR?"L ":"")+"+"+PL.max.toFixed(0)+" / "+PL.min.toFixed(0)+" cents"+(PR?"  R +"+PR.max.toFixed(0)+" / "+PR.min.toFixed(0)+" cents":"")+" at "+fcLabel();')

def patch(s, name):
    a = s.find(NOTE_START)
    assert a >= 0 and s.count(NOTE_START) == 1, name + ' note start'
    b = s.find(NOTE_END, a)
    assert b >= 0, name + ' note end'
    s = s[:a] + NEW_NOTE + s[b + len(NOTE_END):]
    if OLD_READ not in s:
        o2 = OLD_READ.replace('\n', '\r\n')
        assert s.count(o2) == 1, name + ' readout'
        s = s.replace(o2, NEW_READ.replace('\n', '\r\n'))
    else:
        assert s.count(OLD_READ) == 1, name + ' readout count'
        s = s.replace(OLD_READ, NEW_READ)
    return s

for src, dst in (('post_content_v23.html', 'post_content_v24.html'), ('magnatone_preview_v23.html', 'magnatone_preview_v24.html')):
    s = io.open(D + src, encoding='utf-8', newline='').read()
    n0 = len(s)
    s = patch(s, src)
    assert chr(8212) not in s
    io.open(D + dst, 'w', encoding='utf-8', newline='').write(s)
    print('ok', dst, n0, '->', len(s), hashlib.sha256(s.encode('utf-8')).hexdigest())
