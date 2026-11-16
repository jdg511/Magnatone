# Builds v15_thick (NOT live) from v14: adds a "thickness" switch to the
# "Inside the Magnatone sweep" module (W2). Stock 440 = 1 phase stage,
# 2x thick = 2 identical stages at full drive. Dashed ghost = stock 440.
import io, hashlib
D = r'C:\Users\Jason\ClaudeNotify\magnatone' + '\\'
src = io.open(D + 'post_content_v14.html', encoding='utf-8', newline='').read()
prev = io.open(D + 'magnatone_preview_v14.html', encoding='utf-8', newline='').read()
assert src in prev
s = src

def rep(old, new):
    global s
    n = s.count(old)
    assert n == 1, 'anchor count %d for: %s' % (n, old[:70])
    s = s.replace(old, new)

# 1 card: thickness row
a = '<button class="iam-btn" id="iamW2st" aria-pressed="false">Stereo</button>'
rep(a, a + '''
</div>
<div class="iam-row" role="group" aria-label="Thickness: number of cascaded phase stages in the varistor circuit">
<span class="iam-sl" id="iamW2thLbl">thickness</span>
<button class="iam-btn iam-on" id="iamW2th1" aria-pressed="true">Stock 440 (1 stage)</button>
<button class="iam-btn" id="iamW2th2" aria-pressed="false">2x thick (2 stages)</button>''')

# 2 state
rep('uvMode="vib", playing=false, WIN=0.5;', 'uvMode="vib", playing=false, WIN=0.5, thick=1, GH=null;')

# 3 model: second identical bridge stage, same drive, phase swing doubles
rep('if(circuit==="tube") return M.tubeCycle(depth,1,invert,om);',
'''if(circuit==="tube"){ var tc=M.tubeCycle(depth,1,invert,om);
    /* thickness 2: a second identical bridge stage driven just as hard, so the phase swing doubles */
    if(thick===2){ var ti; for(ti=0;ti<tc.phi.length;ti++) tc.phi[ti]*=2; tc.pmin*=2; tc.pmax*=2; }
    return tc; }''')

# 4 ghost trace of the stock 440
a = 'var PL=M.centsTrace(CL,rate,f), PR=CR?M.centsTrace(CR,rate,f):null;'
rep(a, a + '''
  GH=(circuit==="tube"&&thick===2&&!trem)?M.centsTrace(M.tubeCycle(depth,1,false,omd),rate,f):null;''')

# 5 readout
rep('+" at "+fcLabel(); }', '+" at "+fcLabel()+(GH?"  (stock 440: +"+GH.max.toFixed(0)+" / "+GH.min.toFixed(0)+")":""); }')

# 6 draw the ghost
a = 'g.strokeStyle="#5a5040"; g.beginPath(); g.moveTo(g2.px,zero); g.lineTo(g2.px+g2.pwid,zero); g.stroke();'
rep(a, a + '''
  if(GH){ g.setLineDash([5,4]); trace(GH.c,g2,clo,chi,"#9a9183",-1); g.setLineDash([]);
    g.fillStyle="#9a9183"; g.font="10px sans-serif"; g.fillText("- - stock 440",g2.px+6,g2.py+12); }''')
rep('var swT=circuit==="tube"?"2. VARISTOR RESISTANCE":', 'var swT=circuit==="tube"?(thick===2?"2. VARISTOR RESISTANCE, 2 STAGES":"2. VARISTOR RESISTANCE"):')

# 7 switches
a = 'm.disabled=dim; s.disabled=dim; document.getElementById("iamW2chLbl").style.opacity=dim?"0.35":"1";'
rep(a, a + '''
  var tOff=(circuit!=="tube"); setBtn("iamW2th1",thick===1); setBtn("iamW2th2",thick===2);
  document.getElementById("iamW2th1").disabled=tOff; document.getElementById("iamW2th2").disabled=tOff;
  document.getElementById("iamW2thLbl").style.opacity=tOff?"0.35":"1";''')
a = 'document.getElementById("iamW2st").onclick=function(){ setSecond(true); };'
rep(a, a + '''
document.getElementById("iamW2th1").onclick=function(){ thick=1; syncSwitches(); refresh(false); };
document.getElementById("iamW2th2").onclick=function(){ thick=2; syncSwitches(); refresh(false); };''')

# 8 module note
a = 'Stereo on the Magnatones is the 280 countersweep'
rep(a, 'Thickness works on the varistor circuit only: Stock 440 is one phase stage with two varistors, as in the 213, 413 and 440; 2x thick adds a second identical stage driven just as hard, which doubles the phase swing and so the bend, and the dashed grey line keeps the stock 440 on screen for comparison. ' + a)

assert '\u2014' not in s and '&mdash;' not in s
io.open(D + 'post_content_v15_thick.html', 'w', encoding='utf-8', newline='').write(s)
io.open(D + 'magnatone_preview_v15_thick.html', 'w', encoding='utf-8', newline='').write(prev.replace(src, s))
print('ok', len(src), '->', len(s), hashlib.sha256(s.encode('utf-8')).hexdigest())
