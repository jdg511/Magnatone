import io, hashlib, subprocess, sys
D = 'C:\\Users\\Jason\\ClaudeNotify\\magnatone\\'
# commit that holds loops/2.wav and loops/3.wav (passed in by the build script)
full = sys.argv[1].strip()
assert len(full) == 40
OLD_HASH = '4a9af33fd8c1de05f84e339c8edf16a6bdbc4685'
REPS = [
    ('var IRF={sp2:"GAS-L.wav",sp3:"GBS-L.wav"}', 'var IRF={sp2:"2.wav",sp3:"3.wav"}'),
    ('raw.githubusercontent.com/jdg511/Magnatone/' + OLD_HASH + '/loops/', 'raw.githubusercontent.com/jdg511/Magnatone/' + full + '/loops/'),
]
for src, dst in (('post_content_v26.html', 'post_content_v27.html'), ('magnatone_preview_v26.html', 'magnatone_preview_v27.html')):
    s = io.open(D + src, encoding='utf-8', newline='').read()
    for old, new in REPS:
        assert s.count(old) == 1, (src, old[:40], s.count(old))
        s = s.replace(old, new)
    assert s.count('if(m.tank==="t480"){ wet.connect(R); }') == 1
    assert chr(8212) not in s
    io.open(D + dst, 'w', encoding='utf-8', newline='').write(s)
    print('ok', dst, len(s), hashlib.sha256(s.encode('utf-8')).hexdigest())
