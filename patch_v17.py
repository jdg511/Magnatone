# Builds v17 (NOT live) from v16:
#  - every module plays one of two dry guitar loops (loops\dry-staccato.mp3, loops\dry-sustained-chord.mp3)
#    chosen with a "guitar loop" switch shown in each module; the choice is shared by all modules
#  - only one module sounds at a time: starting one stops whichever was playing
#  - the old synthesized phrase stays only as a fallback if a loop file cannot be loaded
# The loops are fetched from window.iamLoopBase (default "loops/"), so the live page needs them hosted.
import io, hashlib
D = r'C:\Users\Jason\ClaudeNotify\magnatone' + '\\'
rd = lambda p: io.open(p, encoding='utf-8', newline='').read()
src = rd(D + 'post_content_v16.html'); prev = rd(D + 'magnatone_preview_v16.html')
assert src in prev
s = src
def rep(old, new):
    global s
    n = s.count(old); assert n == 1, 'anchor count %d for: %s' % (n, old[:70])
    s = s.replace(old, new)

SHARED = r'''/* Illicit Apothecary: the two dry guitar loops every module plays, the shared
   loop choice, and the rule that only one module sounds at a time. */
var LOOPS=[{name:"Staccato",file:"dry-staccato.mp3"},{name:"Sustained chord",file:"dry-sustained-chord.mp3"}];
var LBASE=(window.iamLoopBase||"loops/");
var LP=window.iamLoops={sel:0,bufs:[]};
var BUS=window.iamBus={cur:null,
  claim:function(key,stop,restart,on){ var c=BUS.cur; if(c&&c.key!==key){ BUS.cur=null; try{ c.stop(); }catch(e){} } BUS.cur={key:key,stop:stop,restart:restart,on:on}; }};
/* decode once, fold to mono, level it, and find where the playing starts and
   stops so the long silent tail of each file is not part of the loop */
function loopPrep(ab,i){
  var AC=window.OfflineAudioContext||window.webkitOfflineAudioContext; if(!AC) return;
  var done=function(b){
    var n=b.length,m=new Float32Array(n),c,k,pk=0,ch=b.numberOfChannels,sr=b.sampleRate;
    for(c=0;c<ch;c++){ var d=b.getChannelData(c); for(k=0;k<n;k++) m[k]+=d[k]/ch; }
    for(k=0;k<n;k++){ var a=Math.abs(m[k]); if(a>pk) pk=a; }
    var th=pk*0.003,st=0,en=n-1; while(st<n&&Math.abs(m[st])<th) st++; while(en>st&&Math.abs(m[en])<th) en--;
    var gn=pk>0?0.5/pk:1; for(k=0;k<n;k++) m[k]*=gn;
    LP.bufs[i]={data:m,rate:sr,start:Math.max(0,st/sr-0.005),end:Math.min(n/sr,en/sr+0.35)};
  };
  try{ var p=new AC(1,1,44100).decodeAudioData(ab,done,function(){}); if(p&&p.catch) p.catch(function(){}); }catch(e){}
}
LOOPS.forEach(function(l,i){
  try{ fetch(LBASE+l.file).then(function(r){ if(!r.ok) throw 0; return r.arrayBuffer(); }).then(function(ab){ loopPrep(ab,i); }).catch(function(){}); }catch(e){}
});
/* every module asks here for its sound source */
window.iamSynth=function(ctx){
  var b=LP.bufs[LP.sel]; if(!b) return iamPluck(ctx);
  var ab=ctx.createBuffer(1,b.data.length,b.rate); ab.getChannelData(0).set(b.data);
  var src=ctx.createBufferSource(); src.buffer=ab; src.loop=true; src.loopStart=b.start; src.loopEnd=b.end;
  return src;
};
LP.set=function(i){
  LP.sel=i;
  var bs=document.querySelectorAll(".iam-loopbtn"),k;
  for(k=0;k<bs.length;k++){ var on=(+bs[k].getAttribute("data-loop")===i); bs[k].classList.toggle("iam-on",on); bs[k].setAttribute("aria-pressed",on?"true":"false"); }
  var c=BUS.cur; if(c&&c.on&&c.on()){ try{ c.restart(); }catch(e){} }
};
document.addEventListener("click",function(e){
  var t=e.target; while(t&&t!==document){ if(t.className&&typeof t.className==="string"&&t.className.indexOf("iam-loopbtn")>=0){ LP.set(+t.getAttribute("data-loop")); return; } t=t.parentNode; }
});

'''
ROW = ('<div class="iam-row" role="group" aria-label="Guitar loop"><span class="iam-sl">guitar loop</span>'
       '<button type="button" class="iam-btn iam-loopbtn iam-on" data-loop="0" aria-pressed="true">Staccato</button>'
       '<button type="button" class="iam-btn iam-loopbtn" data-loop="1" aria-pressed="false">Sustained chord</button></div>\n')

# shared code
rep('/* Illicit Apothecary: shared pluck synth (Karplus-Strong) */\nwindow.iamSynth = window.iamSynth || function(ctx){',
    '/* Illicit Apothecary: fallback pluck synth (Karplus-Strong), used only if a loop file cannot be loaded */\nvar iamPluck = function(ctx){')
rep('/* Widget 1: tremolo vs vibrato */', SHARED + '/* Widget 1: tremolo vs vibrato */')

# loop switch in each module
rep('<p class="iam-note">Synthesized guitar phrase, generated in your browser. ', ROW + '<p class="iam-note">Pick either dry guitar loop; the choice carries to every demo on the page, and only one demo plays at a time. ')
rep('<p class="iam-note">All three graphs share', ROW + '<p class="iam-note">All three graphs share')
rep('<p class="iam-note" id="iamW3note"></p>', ROW + '<p class="iam-note" id="iamW3note"></p>')
rep('Audio is the same phrase as the first demo, through a delay line', 'Audio is the dry guitar loop you pick, through a delay line')

# one module at a time
rep('  actx.resume(); stopAll();\n  src=window.iamSynth(actx);\n  var out=actx.createGain();',
    '  actx.resume(); stopAll();\n  window.iamBus.claim("w1",stopAll,function(){ play(mode,btn); },function(){ return !!src; });\n  src=window.iamSynth(actx);\n  var out=actx.createGain();')
rep('  actx.resume(); stopAll(); rebuild();',
    '  actx.resume(); stopAll(); rebuild();\n  window.iamBus.claim("w2",stopAll,startAll,function(){ return playing; });')
rep('  actx.resume(); stopAudio();\n  var m=MODELS[cur];',
    '  actx.resume(); stopAudio();\n  window.iamBus.claim("w3",stopAudio,startAudio,function(){ return playing; });\n  var m=MODELS[cur];')

assert '\u2014' not in s and '&mdash;' not in s
assert s.count('window.iamSynth(actx)') == 3
io.open(D + 'post_content_v17.html', 'w', encoding='utf-8', newline='').write(s)
io.open(D + 'magnatone_preview_v17.html', 'w', encoding='utf-8', newline='').write(prev.replace(src, s))
print('ok', len(src), '->', len(s), hashlib.sha256(s.encode('utf-8')).hexdigest())
