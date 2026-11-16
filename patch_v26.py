import io, hashlib, subprocess
D = 'C:\\Users\\Jason\\ClaudeNotify\\magnatone\\'
# audio is served from the public repo, pinned to the commit that holds the files
AUDIO_COMMIT = '4a9af33'
full = subprocess.check_output(['git', '-C', D, 'rev-parse', AUDIO_COMMIT]).decode().strip()
assert len(full) == 40
BASE = 'https://raw.githubusercontent.com/jdg511/Magnatone/' + full + '/loops/'

S24 = '<sup><a href="#iam-s5">[5]</a></sup><sup><a href="#iam-s24">[24]</a></sup>'
REPS = [
    (2, 'In the model below, at full depth around 1 kHz, the upward bend is nearly three times the downward one.',
        'In the model below, at full depth around 1 kHz, the Custom 440 swings about 29 cents sharp and 37 cents flat, climbing faster than it falls.'),
    (1, "are informed approximations, with the 480's one-sided routing",
        "are impulse responses of stand-in spring tanks, a long two-spring for the Custom 480 and a short three-spring for the M series, with the 480's one-sided routing"),
    (1, 'are informed approximations.<sup>',
        'are impulse responses of stand-in spring tanks: a long two-spring for the Custom 480, a short three-spring for the M series.<sup>'),
    (1, 'The spring reverb in the last demo is an informed approximation of the original tanks, not a measurement of one.',
        'The spring reverbs in the last demo are impulse responses of stand-in tanks, not measurements of the originals.'),
    (1, 'with a transistor phase splitter standing in for the triode; a second board with its own lamp handles the other channel.',
        'with a transistor phase splitter standing in for the triode. The mono M30 carries one such board; the M35 adds a second with its own lamp, fed through an inverter so the two channels sweep in opposite directions.'),
    (1, 'with a transistor phase splitter in place of the triode.' + S24,
        'with a transistor phase splitter in place of the triode.' + S24 + ' The mono M30 has one such board; the M35 adds a second for the other channel.'),
    (1, 'var LBASE=(window.iamLoopBase||"loops/");',
        'var LBASE=(window.iamLoopBase||"' + BASE + '");'),
]
for src, dst in (('post_content_v24.html', 'post_content_v26.html'), ('magnatone_preview_v24.html', 'magnatone_preview_v26.html')):
    s = io.open(D + src, encoding='utf-8', newline='').read()
    n0 = len(s)
    for cnt, old, new in REPS:
        assert s.count(old) == cnt, (src, old[:50], s.count(old))
        s = s.replace(old, new)
    assert chr(8212) not in s and s.count('informed approximation') == 1 and 'three times the downward' not in s
    io.open(D + dst, 'w', encoding='utf-8', newline='').write(s)
    print('ok', dst, n0, '->', len(s), hashlib.sha256(s.encode('utf-8')).hexdigest())
print(BASE)
