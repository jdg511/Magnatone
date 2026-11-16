# Builds v19 (NOT live) from v18:
#  - "Inside the Magnatone sweep": "Original (varistor)" becomes two circuits, "440 (one stage)" and "480 (two stage)"
#  - bench reverbs use recorded spring impulse responses: loops\2sp-long.wav (two-spring tanks) and
#    loops\3sp-sh.wav (three-spring tanks); the synthesized tank stays as the fallback
import io, hashlib
D = r'C:\Users\Jason\ClaudeNotify\magnatone' + '\\'
rd = lambda p: io.open(p, encoding='utf-8', newline='').read()
src = rd(D + 'post_content_v18.html'); prev = rd(D + 'magnatone_preview_v18.html')
assert src in prev
s = src
def rep(old, new):
    global s
    n = s.count(old); assert n == 1, 'anchor count %d for: %s' % (n, old[:70])
    s = s.replace(old, new)

# ---- W2: 440 and 480 as separate circuits ----
rep('<button class="iam-btn iam-on" id="iamW2tube">Original (varistor)</button>',
    '<button class="iam-btn iam-on" id="iamW2tube">440 (one stage)</button>\n<button class="iam-btn" id="iamW2tube2">480 (two stage)</button>')
rep("A live model of three circuits: Magnatone's varistor original, its 1967 lamp-and-photocell transistor version, and the Uni-Vibe.",
    "A live model of four circuits: the one-stage Custom 440 and the two-stage Custom 480 varistor vibratos, Magnatone's 1967 lamp-and-photocell transistor version, and the Uni-Vibe.")
rep('  if(circuit==="tube") return M.tubeCycle(depth,1,invert,om);',
    '  if(circuit==="tube") return M.tubeCycle(depth,1,invert,om);\n  if(circuit==="tube2") return M.tubeCycle(depth,2,invert,om);')
rep('var oscT=circuit==="tube"?', 'var oscT=(circuit==="tube"||circuit==="tube2")?')
rep('var swT=circuit==="tube"?"2. VARISTOR RESISTANCE":', 'var swT=circuit==="tube"?"2. VARISTOR RESISTANCE":circuit==="tube2"?"2. VARISTOR RESISTANCE, 2 STAGES":')
rep('setBtn("iamW2tube",c==="tube"); ', 'setBtn("iamW2tube",c==="tube"); setBtn("iamW2tube2",c==="tube2"); ')
a = 'document.getElementById("iamW2tube").onclick=function(){ setCircuit("tube"); };'
rep(a, a + '\ndocument.getElementById("iamW2tube2").onclick=function(){ setCircuit("tube2"); };')
rep('(Custom 440 here; the Custom 480 for the two-stage amps on the bench below; the M30 and M35 vibrato board)', '(Custom 440, Custom 480, and the M30 and M35 vibrato board)')
rep('Stereo on the Magnatones is the 280 countersweep, left red, right orange.',
    'Stereo, left red and right orange: on the 480 it is the amp\'s own second channel, countersweeping; the 440 was a mono amp, so its stereo setting is a what-if with the oscillator inverted for the right side; on the transistor circuit it is the M35\'s second board.')

# ---- recorded spring impulse responses ----
rep('/* every module asks here for its sound source */',
'''/* recorded spring reverb impulse responses, decoded once and shared */
var IRF={sp2:"2sp-long.wav",sp3:"3sp-sh.wav"}, IRS=window.iamIR={};
Object.keys(IRF).forEach(function(k){
  try{ fetch(LBASE+IRF[k]).then(function(r){ if(!r.ok) throw 0; return r.arrayBuffer(); }).then(function(ab){
    var AC=window.OfflineAudioContext||window.webkitOfflineAudioContext; if(!AC) return;
    var p=new AC(2,1,44100).decodeAudioData(ab,function(b){ var ch=[],c; for(c=0;c<b.numberOfChannels;c++) ch.push(new Float32Array(b.getChannelData(c))); IRS[k]={ch:ch,rate:b.sampleRate}; },function(){});
    if(p&&p.catch) p.catch(function(){});
  }).catch(function(){}); }catch(e){}
});
/* every module asks here for its sound source */''')
rep('/* ---- spring reverb tank models (synthesized impulse responses) ----', '/* ---- spring reverb tanks: recorded impulse responses, with a synthesized tank as the fallback ----')
rep('t480:{springs:[0.036,0.043],', 't480:{ir:"sp2",springs:[0.036,0.043],')
rep('tM10:{springs:[0.029,0.034,0.039],', 'tM10:{ir:"sp3",springs:[0.029,0.034,0.039],')
rep('tSS:{springs:[0.031,0.041],', 'tSS:{ir:"sp2",springs:[0.031,0.041],')
rep('  if(irCache[id]) return irCache[id];\n',
    '  var rec=window.iamIR&&window.iamIR[TANKS[id].ir];\n'
    '  if(rec){ if(!irCache[id+"r"]){ var rb=ctx.createBuffer(rec.ch.length,rec.ch[0].length,rec.rate),rc; for(rc=0;rc<rec.ch.length;rc++) rb.getChannelData(rc).set(rec.ch[rc]); irCache[id+"r"]=rb; } return irCache[id+"r"]; }\n'
    '  if(irCache[id]) return irCache[id];\n')

assert '\u2014' not in s and '&mdash;' not in s
io.open(D + 'post_content_v19.html', 'w', encoding='utf-8', newline='').write(s)
io.open(D + 'magnatone_preview_v19.html', 'w', encoding='utf-8', newline='').write(prev.replace(src, s))
print('ok', len(src), '->', len(s), hashlib.sha256(s.encode('utf-8')).hexdigest())
