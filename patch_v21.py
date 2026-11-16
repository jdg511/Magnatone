# Builds v21 (NOT live) from v20: swaps the two reverb impulse responses.
#  two-spring long tank (Custom 480)            -> loops\GAS-L.wav
#  three-spring short tank and all M-series amps -> loops\GBS-L.wav
import io, hashlib
D = r'C:\Users\Jason\ClaudeNotify\magnatone' + '\\'
rd = lambda p: io.open(p, encoding='utf-8', newline='').read()
src = rd(D + 'post_content_v20.html'); prev = rd(D + 'magnatone_preview_v20.html')
old = 'var IRF={sp2:"2sp-long.wav",sp3:"3sp-sh.wav"}'
assert src in prev and src.count(old) == 1
s = src.replace(old, 'var IRF={sp2:"GAS-L.wav",sp3:"GBS-L.wav"}')
io.open(D + 'post_content_v21.html', 'w', encoding='utf-8', newline='').write(s)
io.open(D + 'magnatone_preview_v21.html', 'w', encoding='utf-8', newline='').write(prev.replace(src, s))
print('ok', len(s), hashlib.sha256(s.encode('utf-8')).hexdigest())
