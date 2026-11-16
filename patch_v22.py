# Builds v22 (NOT live) from v21:
#  - the Staccato loop option is removed; every module plays the sustained chord by default
#  - visitors can upload their own audio file to loop instead (decoded in the browser, never sent anywhere);
#    "Your audio" switches back to it, "Upload audio" picks a new file; the choice is shared by all modules
import io, hashlib
D = r'C:\Users\Jason\ClaudeNotify\magnatone' + '\\'
rd = lambda p: io.open(p, encoding='utf-8', newline='').read()
src = rd(D + 'post_content_v21.html'); prev = rd(D + 'magnatone_preview_v21.html')
assert src in prev
s = src
def rep(old, new, count=1):
    global s
    n = s.count(old); assert n == count, 'anchor count %d for: %s' % (n, old[:70])
    s = s.replace(old, new)

OLDROW = ('<div class="iam-row" role="group" aria-label="Guitar loop"><span class="iam-sl">guitar loop</span>'
          '<button type="button" class="iam-btn iam-loopbtn iam-on" data-loop="0" aria-pressed="true">Staccato</button>'
          '<button type="button" class="iam-btn iam-loopbtn" data-loop="1" aria-pressed="false">Sustained chord</button></div>\n')
NEWROW = ('<div class="iam-row" role="group" aria-label="Sound to loop"><span class="iam-sl">loop</span>'
          '<button type="button" class="iam-btn iam-loopbtn iam-on" data-loop="0" aria-pressed="true">Sustained chord</button>'
          '<button type="button" class="iam-btn iam-loopbtn" data-loop="1" aria-pressed="false" disabled>Your audio</button>'
          '<button type="button" class="iam-btn iam-loopup">Upload audio</button></div>\n')
rep(OLDROW, NEWROW, count=3)
rep('var LOOPS=[{name:"Staccato",file:"dry-staccato.mp3"},{name:"Sustained chord",file:"dry-sustained-chord.mp3"}];',
    'var LOOPS=[{name:"Sustained chord",file:"dry-sustained-chord.mp3"}];   /* slot 1 is the visitor\'s own upload */')
rep('function loopPrep(ab,i){', 'function loopPrep(ab,i,cb){')
rep('  var AC=window.OfflineAudioContext||window.webkitOfflineAudioContext; if(!AC) return;\n  var done=function(b){',
    '  var AC=window.OfflineAudioContext||window.webkitOfflineAudioContext; if(!AC){ if(cb) cb(false); return; }\n  var done=function(b){')
rep('LP.bufs[i]={data:m,rate:sr,start:Math.max(0,st/sr-0.005),end:Math.min(n/sr,en/sr+0.35)};',
    'LP.bufs[i]={data:m,rate:sr,start:Math.max(0,st/sr-0.005),end:Math.min(n/sr,en/sr+0.35)}; if(cb) cb(true);')
rep('decodeAudioData(ab,done,function(){}); if(p&&p.catch) p.catch(function(){}); }catch(e){}',
    'decodeAudioData(ab,done,function(){ if(cb) cb(false); }); if(p&&p.catch) p.catch(function(){}); }catch(e){ if(cb) cb(false); }')
rep('  var t=e.target; while(t&&t!==document){ if(t.className',
    '  var t=e.target; while(t&&t!==document){ if(t.className&&typeof t.className==="string"&&t.className.indexOf("iam-loopup")>=0){ upPick(); return; } if(t.className')
rep('document.addEventListener("click",function(e){',
'''/* a visitor's own audio file: read and decoded in the browser, never sent anywhere */
var upIn=null;
function upSay(t){ var bs=document.querySelectorAll(".iam-loopup"),k; for(k=0;k<bs.length;k++) bs[k].textContent=t; }
function upPick(){
  if(!upIn){
    upIn=document.createElement("input"); upIn.type="file"; upIn.accept="audio/*"; upIn.style.display="none"; upIn.setAttribute("aria-hidden","true");
    document.body.appendChild(upIn);
    upIn.onchange=function(){
      var f=upIn.files&&upIn.files[0]; if(!f) return;
      if(f.size>40*1024*1024){ upSay("Too large (40 MB max)"); return; }
      upSay("Reading...");
      var fr=new FileReader();
      fr.onload=function(){ loopPrep(fr.result,1,function(ok){
        if(!ok){ upSay("Could not read that file"); return; }
        var nm=f.name.length>22?f.name.slice(0,20)+"...":f.name, bs=document.querySelectorAll('.iam-loopbtn[data-loop="1"]'),k;
        for(k=0;k<bs.length;k++){ bs[k].disabled=false; bs[k].textContent=nm; }
        upSay("Upload audio"); LP.set(1);
      }); };
      fr.onerror=function(){ upSay("Could not read that file"); };
      fr.readAsArrayBuffer(f); upIn.value="";
    };
  }
  upSay("Upload audio"); upIn.click();
}
document.addEventListener("click",function(e){''')
rep('Pick either dry guitar loop; the choice carries to every demo on the page, and only one demo plays at a time.',
    'Every demo loops the same dry guitar chord, or a sound file of your own: press Upload audio (the file is read in your browser and never leaves it). The choice carries to every demo on the page, and only one demo plays at a time.')
rep('Audio is the dry guitar loop you pick, through a delay line', 'Audio is the dry guitar chord, or your own uploaded file, through a delay line')

assert '\u2014' not in s and '&mdash;' not in s and 'Staccato' not in s and 'dry-staccato' not in s
io.open(D + 'post_content_v22.html', 'w', encoding='utf-8', newline='').write(s)
io.open(D + 'magnatone_preview_v22.html', 'w', encoding='utf-8', newline='').write(prev.replace(src, s))
print('ok', len(src), '->', len(s), hashlib.sha256(s.encode('utf-8')).hexdigest())
