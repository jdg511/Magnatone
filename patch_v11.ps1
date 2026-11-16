$d="C:\Users\Jason\ClaudeNotify\magnatone"
$enc=New-Object Text.UTF8Encoding($false)
$t=[IO.File]::ReadAllText("$d\post_content_v10.html",$enc)
function R1($o,$w){ if(([regex]::Matches($script:t,[regex]::Escape($o))).Count -ne 1){ throw "anchor: $o" }; $script:t=$script:t.Replace($o,$w) }
$o1='function logArr(a){ var o=new Float32Array(a.length),i; for(i=0;i<a.length;i++) o[i]=Math.log(a[i]); return o; }'
$w1=@'
function logArr(a){ var o=new Float32Array(a.length),i; for(i=0;i<a.length;i++) o[i]=Math.log(a[i]); return o; }
/* symmetric log for graph 3: sign(v)*log10(1+|v|), so 0 stays at 0 and both signs compress the same way */
function symlog(v){ return (v<0?-1:1)*Math.log10(1+Math.abs(v)); }
function symArr(a,lim){ var o=new Float32Array(a.length),i,v; for(i=0;i<a.length;i++){ v=Math.max(-lim,Math.min(lim,a[i])); o[i]=symlog(v); } return o; }
function symTicks(vals){ return vals.map(function(x){ return {v:symlog(x),t:(x>0?"+":"")+x}; }); }
'@
R1 $o1 $w1
$o2=@'
  /* fixed scales: pitch -200 to +200 cents, loudness 0 to -96 dB */
  if(trem){ clo=-96; chi=0; ticks=[{v:0,t:"0"},{v:-16,t:"-16"},{v:-32,t:"-32"},{v:-48,t:"-48"},{v:-64,t:"-64"},{v:-80,t:"-80"},{v:-96,t:"-96"}]; }
  else { clo=-200; chi=200; ticks=linTicks(clo,chi,8); }
  axes(g2,trem?"3. LOUDNESS AT "+fcLabel():"3. PITCH AT "+fcLabel(),trem?"Y: level, dB below full":"Y: pitch bend, cents from the note",clo,chi,ticks);
  var zero=g2.py+g2.ph-(g2.ph*(0-clo)/(chi-clo));
  g.strokeStyle="#5a5040"; g.beginPath(); g.moveTo(g2.px,zero); g.lineTo(g2.px+g2.pwid,zero); g.stroke();
  if(TR){
    trace(TL.c,g2,clo,chi,"rgba(232,112,90,0.66)",ph);
    trace(TR.c,g2,clo,chi,"rgba(242,163,60,0.66)",ph);
'@
$w2=@'
  /* fixed log scales: pitch -200 to +200 cents (symmetric log), loudness 0 to -96 dB (log) */
  var lim=trem?96:200;
  if(trem){ clo=symlog(-96); chi=0; ticks=symTicks([0,-1,-3,-10,-30,-96]); }
  else { clo=symlog(-200); chi=symlog(200); ticks=symTicks([-200,-100,-30,-10,-3,0,3,10,30,100,200]); }
  axes(g2,trem?"3. LOUDNESS AT "+fcLabel():"3. PITCH AT "+fcLabel(),trem?"Y: level, dB below full (log scale)":"Y: pitch bend, cents from the note (log scale)",clo,chi,ticks);
  var zero=g2.py+g2.ph-(g2.ph*(0-clo)/(chi-clo));
  g.strokeStyle="#5a5040"; g.beginPath(); g.moveTo(g2.px,zero); g.lineTo(g2.px+g2.pwid,zero); g.stroke();
  if(TR){
    trace(symArr(TL.c,lim),g2,clo,chi,"rgba(232,112,90,0.66)",ph);
    trace(symArr(TR.c,lim),g2,clo,chi,"rgba(242,163,60,0.66)",ph);
'@
R1 $o2 $w2
$o3=@'
  } else {
    trace(TL.c,g2,clo,chi,"#e8705a",ph);
  }
'@
$w3=@'
  } else {
    trace(symArr(TL.c,lim),g2,clo,chi,"#e8705a",ph);
  }
'@
R1 $o3 $w3
R1 'Pitch is plotted on a fixed scale of -200 to +200 cents and loudness on a fixed 0 to -96 dB; the readout gives the peaks.' 'Pitch is plotted on a fixed logarithmic scale of -200 to +200 cents (symmetric about zero, so a 3 cent wobble is still visible next to a 150 cent one) and loudness on a fixed logarithmic 0 to -96 dB; the readout gives the peaks.'
$t=$t -replace "`r`n","`n"
[IO.File]::WriteAllText("$d\post_content_v11.html",$t,$enc)
(Get-FileHash "$d\post_content_v11.html" -Algorithm SHA256).Hash.ToLower()
$pv=[IO.File]::ReadAllText("$d\magnatone_preview_v10.html",$enc)
$a=$pv.IndexOf('<div class="iam-post'); $b=$pv.LastIndexOf('</body>')
[IO.File]::WriteAllText("$d\magnatone_preview_v11.html",$pv.Substring(0,$a)+$t+"`n"+$pv.Substring($b),$enc)
Copy-Item "$d\post_content_v11.html" "C:\Users\Jason\ClaudeNotify\tmp_magnatone_post_v2.html" -Force
Copy-Item "$d\post_content_v11.html" "$d\backup_v11.html" -Force
"files written"
