$d="C:\Users\Jason\ClaudeNotify\magnatone"
$enc=New-Object Text.UTF8Encoding($false)
$t=[IO.File]::ReadAllText("$d\post_content_v9.html",$enc)
function R1($o,$w){ if(([regex]::Matches($script:t,[regex]::Escape($o))).Count -ne 1){ throw "anchor: $o" }; $script:t=$script:t.Replace($o,$w) }
$o1=@'
function tremFromTrace(c,tr){
  var N=c.phi.length,i,span=tr.max-tr.min,t={lfo:c.lfo,rr:c.rr,phi:c.phi,pmin:c.pmin,pmax:c.pmax,rmin:c.rmin,rmax:c.rmax,am:new Float32Array(N)};
  for(i=0;i<N;i++){ var pn=span>0?(tr.c[i]-tr.min)/span:0.5; t.am[i]=1-0.85*depth*(1-pn); }
  return t;
}
'@
$w1=@'
/* Tremolo: loudness follows how far the pitch trace swings from 0 cents at the
   centre frequency. 0 cents = 0 dB, 200 cents either way = -96 dB, linear in dB. */
function tremFromTrace(c,tr){
  var N=c.phi.length,i,t={lfo:c.lfo,rr:c.rr,phi:c.phi,pmin:c.pmin,pmax:c.pmax,rmin:c.rmin,rmax:c.rmax,am:new Float32Array(N)};
  for(i=0;i<N;i++){ var db=-96*Math.min(Math.abs(tr.c[i]),200)/200; t.am[i]=Math.pow(10,db/20); }
  return t;
}
'@
R1 $o1 $w1
R1 '  for(i=0;i<N;i++){ out[i]=20*Math.log10(Math.max(c.am[i],1e-3)); if(out[i]<mn)mn=out[i]; if(out[i]>mx)mx=out[i]; }' '  for(i=0;i<N;i++){ out[i]=20*Math.log10(Math.max(c.am[i],1e-5)); if(out[i]<mn)mn=out[i]; if(out[i]>mx)mx=out[i]; }'
$o3=@'
  if(trem){ clo=Math.min(TL.min,TR?TR.min:0); clo=-Math.max(5,Math.ceil(-clo/5)*5); chi=0; ticks=linTicks(clo,chi,4); }
  else { var mn=Math.min(TL.min,TR?TR.min:0), mx=Math.max(TL.max,TR?TR.max:0), a=Math.max(10,Math.abs(mn),Math.abs(mx)); var s=niceStep(2*a,6); chi=Math.ceil(a/s)*s; clo=-chi; ticks=linTicks(clo,chi,6); }
'@
$w3=@'
  /* fixed scales: pitch -200 to +200 cents, loudness 0 to -96 dB */
  if(trem){ clo=-96; chi=0; ticks=[{v:0,t:"0"},{v:-16,t:"-16"},{v:-32,t:"-32"},{v:-48,t:"-48"},{v:-64,t:"-64"},{v:-80,t:"-80"},{v:-96,t:"-96"}]; }
  else { clo=-200; chi=200; ticks=linTicks(clo,chi,8); }
'@
R1 $o3 $w3
R1 'The readout gives the peaks. The centre slider (100 Hz to 10 kHz) changes the display only, except in Tremolo, where it also sets the loudness curve you hear.' 'Pitch is plotted on a fixed scale of -200 to +200 cents and loudness on a fixed 0 to -96 dB; the readout gives the peaks. The centre slider (100 Hz to 10 kHz) changes the display only, except in Tremolo, where the loudness you hear follows it: the further the pitch trace swings from 0 cents at that frequency, the deeper the dip, with 0 cents = 0 dB and 200 cents either way = -96 dB.'
$t=$t -replace "`r`n","`n"
[IO.File]::WriteAllText("$d\post_content_v10.html",$t,$enc)
(Get-FileHash "$d\post_content_v10.html" -Algorithm SHA256).Hash.ToLower()
$pv=[IO.File]::ReadAllText("$d\magnatone_preview_v9.html",$enc)
$a=$pv.IndexOf('<div class="iam-post'); $b=$pv.LastIndexOf('</body>')
[IO.File]::WriteAllText("$d\magnatone_preview_v10.html",$pv.Substring(0,$a)+$t+"`n"+$pv.Substring($b),$enc)
Copy-Item "$d\post_content_v10.html" "C:\Users\Jason\ClaudeNotify\tmp_magnatone_post_v2.html" -Force
Copy-Item "$d\post_content_v10.html" "$d\backup_v10.html" -Force
"files written"
