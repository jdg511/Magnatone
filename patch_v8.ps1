$d="C:\Users\Jason\ClaudeNotify\magnatone"
$enc=New-Object Text.UTF8Encoding($false)
$t=[IO.File]::ReadAllText("$d\post_content_v7.html",$enc)
$nd=[IO.File]::ReadAllText("$d\newdraw.txt",$enc)
$nd=$nd -replace "`r`n","`n"
if(-not $nd.EndsWith("`n`n")){ $nd=$nd.TrimEnd("`n")+"`n`n" }
function R1($o,$w){ if(([regex]::Matches($script:t,[regex]::Escape($o))).Count -ne 1){ throw "anchor: $o" }; $script:t=$script:t.Replace($o,$w) }
R1 '<canvas id="iamW2c" width="900" height="330"' '<canvas id="iamW2c" width="900" height="370"'
R1 'id="iamW2fc" min="0" max="1000" step="1" value="667" aria-label="Centre frequency of the displayed curve, 10 hertz to 10 kilohertz, logarithmic"' 'id="iamW2fc" min="0" max="1000" step="1" value="500" aria-label="Centre frequency of the displayed curve, 100 hertz to 10 kilohertz, logarithmic"'
R1 'aria-label="Three animated panels showing the oscillator waveform, the resistance sweep it produces, and the resulting pitch deviation in cents (or loudness in dB) over half a second"' 'aria-label="Three animated graphs sharing a time axis of 0 to 500 milliseconds: the oscillator control signal from minus one to plus one, the resistance of the swept element in ohms on a log scale, and the resulting pitch deviation in cents (or loudness in decibels) at the centre frequency"'
$o=@'
<p class="iam-note">Each panel shows half a second. Left: the oscillator output scaled by depth. Middle: the resistance sweep. Right: the pitch in cents (or loudness in dB) of a tone at the centre frequency; the readout gives the peaks. The centre slider (10 Hz to 10 kHz) changes the display only,
'@
$w=@'
<p class="iam-note">All three graphs share the same X axis: time, 0 to 500 ms, so 2 Hz draws one cycle and 10 Hz draws five. Y axes, left to right: the oscillator's control signal, scaled by depth, from -1 to +1 (1 is the hardest the element can be driven); the resistance of the swept element in ohms on a log scale from 100 &Omega; to 10 M&Omega;; and what that sweep does to a tone at the centre frequency, in cents of pitch above or below the unmodulated note, or in dB below full level in Tremolo. The readout gives the peaks. The centre slider (100 Hz to 10 kHz) changes the display only,
'@
R1 $o $w
R1 'function fc(){ return 10*Math.pow(10,3*fcv/1000); }' 'function fc(){ return 100*Math.pow(10,2*fcv/1000); }'
R1 'var rate=5, depth=1, vol=0.8, fcv=667,' 'var rate=5, depth=1, vol=0.8, fcv=500,'
$i=$t.IndexOf('function panel(x0,label)'); $j=$t.IndexOf('/* audio */')
if($i -lt 0 -or $j -lt 0){ throw "draw block markers not found" }
$t=$t.Substring(0,$i)+$nd+$t.Substring($j)
[IO.File]::WriteAllText("$d\post_content_v8.html",$t,$enc)
"bytes " + [IO.File]::ReadAllBytes("$d\post_content_v8.html").Length
(Get-FileHash "$d\post_content_v8.html" -Algorithm SHA256).Hash.ToLower()
$pv=[IO.File]::ReadAllText("$d\magnatone_preview_v7.html",$enc)
$a=$pv.IndexOf('<div class="iam-post">'); $b=$pv.LastIndexOf('</body>')
[IO.File]::WriteAllText("$d\magnatone_preview_v8.html",$pv.Substring(0,$a)+$t+"`n"+$pv.Substring($b),$enc)
"preview written"
