import io, hashlib
D = 'C:\\Users\\Jason\\ClaudeNotify\\magnatone\\'
OLD = 'var IRF={sp2:"GAS-L.wav",sp3:"GBS-L.wav"}'
NEW = 'var IRF={sp2:"2sp-long.wav",sp3:"GBS-L.wav"}'
for src, dst in (('post_content_v24.html', 'post_content_v25.html'), ('magnatone_preview_v24.html', 'magnatone_preview_v25.html')):
    s = io.open(D + src, encoding='utf-8', newline='').read()
    assert s.count(OLD) == 1, src
    assert s.count('if(m.tank==="t480"){ wet.connect(R); }') == 1, src + ' right-only routing'
    s = s.replace(OLD, NEW)
    io.open(D + dst, 'w', encoding='utf-8', newline='').write(s)
    print('ok', dst, len(s), hashlib.sha256(s.encode('utf-8')).hexdigest())
