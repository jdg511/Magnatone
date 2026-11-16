# Builds v20 (NOT live) from v19: every M-series amp on the bench (M10, M15, M30, M35) uses the
# three-spring impulse response loops\3sp-sh.wav. Only the Custom 480 stays on loops\2sp-long.wav.
import io, hashlib
D = r'C:\Users\Jason\ClaudeNotify\magnatone' + '\\'
rd = lambda p: io.open(p, encoding='utf-8', newline='').read()
src = rd(D + 'post_content_v19.html'); prev = rd(D + 'magnatone_preview_v19.html')
assert src in prev and src.count('tSS:{ir:"sp2",') == 1
s = src.replace('tSS:{ir:"sp2",', 'tSS:{ir:"sp3",')
io.open(D + 'post_content_v20.html', 'w', encoding='utf-8', newline='').write(s)
io.open(D + 'magnatone_preview_v20.html', 'w', encoding='utf-8', newline='').write(prev.replace(src, s))
print('ok', len(s), hashlib.sha256(s.encode('utf-8')).hexdigest())
