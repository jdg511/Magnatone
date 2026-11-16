import io, hashlib, sys
D = 'C:\\Users\\Jason\\ClaudeNotify\\magnatone\\'
# v28 = v27 with the audio base moved to the commit that holds the de-ringed loops/2.wav
full = sys.argv[1].strip()
assert len(full) == 40
OLD_HASH = 'c95e61a062d32949579237924895c59951d9c2d4'
old = 'raw.githubusercontent.com/jdg511/Magnatone/' + OLD_HASH + '/loops/'
new = 'raw.githubusercontent.com/jdg511/Magnatone/' + full + '/loops/'
for src, dst in (('post_content_v27.html', 'post_content_v28.html'), ('magnatone_preview_v27.html', 'magnatone_preview_v28.html')):
    s = io.open(D + src, encoding='utf-8', newline='').read()
    assert s.count(old) == 1, src
    s = s.replace(old, new)
    io.open(D + dst, 'w', encoding='utf-8', newline='').write(s)
    print('ok', dst, len(s), hashlib.sha256(s.encode('utf-8')).hexdigest())
