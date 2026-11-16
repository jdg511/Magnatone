# Builds v16 (NOT live) from v14:
#  - tube and transistor Magnatone models replaced by SPICE-derived ones (spice440\model_*_filled.js)
#  - pitch sign fixed in the cents display (phi is a lag: rising phi = falling pitch)
#  - "Six Magnatones on the bench" becomes eight: adds M30 (mono) and M35 (stereo) transistor amps
import io, re, hashlib
D = r'C:\Users\Jason\ClaudeNotify\magnatone' + '\\'
rd = lambda p: io.open(p, encoding='utf-8', newline='').read()
src = rd(D + 'post_content_v14.html'); prev = rd(D + 'magnatone_preview_v14.html')
tube = rd(D + r'spice440\model_tube_filled.js'); ss = rd(D + r'spice440\model_ss_filled.js')
assert src in prev
s = src

def rep(old, new, count=1):
    global s
    n = s.count(old)
    assert (n == count) if count else (n >= 1), 'anchor count %d for: %s' % (n, old[:70])
    s = s.replace(old, new)

def cut(a, b, new):
    global s
    assert s.count(a) == 1 and s.count(b) == 1, (a[:40], s.count(a), b[:40], s.count(b))
    i, j = s.index(a), s.index(b); assert i < j
    s = s[:i] + new.rstrip('\n') + '\n\n' + s[j:]

# ---- model library ----
cut('/* The tube LFO: measured harmonic series', '/* Shared lamp + photocell dynamics', tube)
cut('/* 1967 TRANSISTOR Magnatone (M35 vibrato board 35-0060)', '/* UNI-VIBE (Shin-ei, 1968)', ss)
for dead in ('M.lfoWave(', 'M.tubeStage(', 'solveV(', 'RSCALE*'): assert dead not in s, dead
rep('   Ported from the Python simulation of the Magnatone vibrato chain.',
    '   The tube and transistor Magnatone circuits run on tables from ngspice\n   simulations of the factory schematics (Custom 440, Custom 480, M30 / M35 board 35-0060).')
rep('    var d=(c.phi[(i+1)%N]-c.phi[i])/dt/(2*Math.PI);',
    '    var d=-(c.phi[(i+1)%N]-c.phi[i])/dt/(2*Math.PI);   /* phi is a lag: rising phi is falling pitch */')

# ---- W2 note ----
a = 'Stereo on the Magnatones is the 280 countersweep'
rep(a, 'The two Magnatone circuits run on curves from SPICE simulations of the factory schematics (Custom 440 here; the Custom 480 for the two-stage amps on the bench below; the M30 and M35 vibrato board): the simulated volts across the varistors, or the simulated lamp current, drive the bridge. The real speed controls cover only about 4.5 to 6 Hz (440), 4.2 to 6.4 Hz (480) and 4.8 to 8.4 Hz (transistor); the slider goes wider. Below about 400 Hz at high depth the varistor curve is extrapolated past its measured points, so treat those readings as rough. ' + a)

# ---- W3: eight amps ----
rep('<h4>Six Magnatones on the bench</h4>', '<h4>Eight Magnatones on the bench</h4>')
rep('Six of the amps above with their actual feature sets: mono or stereo, one or two modulator stages, reverb only where the real amp had it.',
    'Eight amps from this story with their actual feature sets: mono or stereo, varistors or lamp and photocells, one or two modulator stages, reverb only where the real amp had it.', count=0)
rep('/* ---- the six amps: documented feature sets ---- */', '/* ---- the eight amps: documented feature sets ---- */')
rep('sub:"stereo, eight varistors, no reverb"}\n};',
    'sub:"stereo, eight varistors, no reverb"},\n'
    '  m30:{name:"M30",years:"1967 to 1970",stereo:false,ss:true,stages:2,tank:"tSS",art:"ss",sub:"mono, one lamp, two photocells, reverb"},\n'
    '  m35:{name:"M35 The Killer",years:"1967 to 1970",stereo:true,ss:true,stages:2,tank:"tSS",art:"ss2",sub:"stereo, two lamps, four photocells, reverb"}\n};')
rep('var ORDER=["m213","m280","m413","m480","m10","m14"];', 'var ORDER=["m213","m280","m413","m480","m10","m14","m30","m35"];')
rep('  } else if(kind==="suit"){',
    '''  } else if(kind==="ss"||kind==="ss2"){
    var blk='fill="#1c1c1e" stroke="#9aa0a6" stroke-width="1.2"', cone='fill="#0c0c0d"';
    s+='<rect x="32" y="4" width="56" height="14" rx="2" '+blk+'/><rect x="37" y="8" width="46" height="5" fill="#9aa0a6"/>';
    s+='<rect x="32" y="20" width="56" height="60" rx="3" '+blk+'/><circle cx="60" cy="'+(kind==="ss2"?44:38)+'" r="11" '+cone+'/><circle cx="60" cy="67" r="11" '+cone+'/>';
    if(kind==="ss2"){ s+='<rect x="40" y="24" width="14" height="6" rx="1" '+cone+'/><rect x="66" y="24" width="14" height="6" rx="1" '+cone+'/>';
      s+='<text x="92" y="14" font-size="9" font-weight="700" fill="#9aa0a6" font-family="serif">VV</text>'; }
  } else if(kind==="suit"){''')
rep('label:"three shorter springs, brighter recovery"}',
    'label:"three shorter springs, brighter recovery"},\n  tSS:{springs:[0.031,0.041],decay:2.0,hf:4200,fhi:3000,label:"transistor-driven spring tank (the pan itself is undocumented)"}')
rep('function cycleFor(m,invert){ return M.tubeCycle(depth,m.stages,invert); }',
    'function cycleFor(m,invert){ return m.ss?M.ssCycle(rate,depth,invert):M.tubeCycle(depth,m.stages,invert); }')
rep('(m.stages===2?", two cascaded modulator stages.":", one modulator stage.");',
    '(m.ss?", a lamp and two photocell phase stages per channel.":(m.stages===2?", two cascaded modulator stages.":", one modulator stage."));')

assert '\u2014' not in s and '&mdash;' not in s
for m in re.finditer(r'[^.>]{0,60}\b[Ss]ix\b[^.<]{0,60}', s): print('SIX:', m.group(0))
io.open(D + 'post_content_v16.html', 'w', encoding='utf-8', newline='').write(s)
io.open(D + 'magnatone_preview_v16.html', 'w', encoding='utf-8', newline='').write(prev.replace(src, s))
print('ok', len(src), '->', len(s), hashlib.sha256(s.encode('utf-8')).hexdigest())
