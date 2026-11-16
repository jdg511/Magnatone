$d="C:\Users\Jason\ClaudeNotify\magnatone"
$enc=New-Object Text.UTF8Encoding($false)
$t=[IO.File]::ReadAllText("$d\post_content_v8.html",$enc)
function R1($o,$w){ if(([regex]::Matches($script:t,[regex]::Escape($o))).Count -ne 1){ throw "anchor: $o" }; $script:t=$script:t.Replace($o,$w) }
function Wrap($start,$endstart,$compact){ $i=$script:t.IndexOf($start); $k=$script:t.IndexOf($endstart); if($i -lt 0 -or $k -lt 0){ throw "wrap marker $start" }; $j=$script:t.IndexOf("`n",$k); $script:t=$script:t.Substring(0,$i)+"<div class=`"iam-detail`">`n"+$script:t.Substring($i,$j-$i)+"`n</div>`n<div class=`"iam-compact`">`n"+$compact+"`n</div>"+$script:t.Substring($j) }
R1 '<div class="iam-post">' '<div class="iam-post iam-mode-compact">'
$css=@'

.iam-post{position:relative}
.iam-post .iam-togglebar{height:0;position:relative;z-index:60}
.iam-post .iam-toggle{position:absolute;right:0;top:0;font:700 12px/1 system-ui,-apple-system,"Segoe UI",sans-serif;letter-spacing:.06em;text-transform:uppercase;background:#f2a33c;color:#120f0b;border:0;border-radius:999px;padding:11px 15px;cursor:pointer;box-shadow:0 2px 10px rgba(0,0,0,.4);white-space:nowrap}
.iam-post .iam-toggle:hover{background:#ffb95a}
.iam-post .iam-togglebar.iam-fixed .iam-toggle{position:fixed;top:16px;right:18px;z-index:10000}
.iam-post .iam-intro{padding-right:200px}
.iam-post.iam-mode-compact .iam-detail{display:none}
.iam-post:not(.iam-mode-compact) .iam-compact{display:none}
@media (max-width:760px){
.iam-post .iam-togglebar{height:auto;margin:0 0 16px}
.iam-post .iam-toggle,.iam-post .iam-togglebar.iam-fixed .iam-toggle{position:static;display:inline-block}
.iam-post .iam-intro{padding-right:0}
}
'@
R1 '.iam-post .iam-st{color:#f2a33c;font-weight:700;white-space:nowrap}' ('.iam-post .iam-st{color:#f2a33c;font-weight:700;white-space:nowrap}'+$css)
$bar=@'
<div class="iam-togglebar" id="iamToggleBar"><button type="button" class="iam-toggle" id="iamToggle" aria-pressed="false">For More Details</button></div>
<script>
(function(){
  var post=document.querySelector('.iam-post'),bar=document.getElementById('iamToggleBar'),btn=document.getElementById('iamToggle');
  if(!post||!bar||!btn) return;
  function compact(){ return post.classList.contains('iam-mode-compact'); }
  function label(){ btn.textContent=compact()?'For More Details':'The Compact Version'; btn.setAttribute('aria-pressed',compact()?'false':'true'); }
  /* keep whatever shared element is at the top of the screen in place when the text above it changes length */
  function anchor(){ var els=post.querySelectorAll('h2,p,.iam-card,table'),i,e,r; for(i=0;i<els.length;i++){ e=els[i]; if(!e.offsetParent) continue; if(e.closest('.iam-detail,.iam-compact')) continue; r=e.getBoundingClientRect(); if(r.bottom>90) return e; } return null; }
  btn.addEventListener('click',function(){ var a=anchor(),t=a?a.getBoundingClientRect().top:0; post.classList.toggle('iam-mode-compact'); label(); if(a) window.scrollBy(0,a.getBoundingClientRect().top-t); place(); });
  function place(){ if(window.innerWidth<=760){ bar.classList.remove('iam-fixed'); return; } var r=post.getBoundingClientRect(); bar.classList.toggle('iam-fixed', r.top<16 && r.bottom>120); }
  window.addEventListener('scroll',place,{passive:true}); window.addEventListener('resize',place); label(); place();
})();
</script>
'@
R1 '<p><em>Part of a series' ($bar+"`n"+'<p class="iam-intro"><em>Part of a series')
$c1=@'
<p>Almost every amp of the era gave you the top trace. Magnatone gave you the bottom one.</p>

<h2>Why real vibrato was considered close to impossible</h2>

<p>Pitch is how fast a waveform's phase goes by, so a box that raises pitch has to deliver the waveform faster than it arrived. A box that changes pitch is a box that manipulates time. The normal way to do that is a delay line whose delay is swept up and down, which is how every chorus and vibrato pedal works today. In 1957 none of the ways to build one existed: tape was a studio trick, the bucket brigade chip was twelve years away, and digital memory was science fiction.</p>

<p>Magnatone's loophole was phase. An all-pass filter passes every frequency at the same level but delays each by a different amount, and while its phase is being swept, every note inside its band comes out pitch-shifted, because a changing phase is indistinguishable from a changing frequency. Sweep 130 degrees of phase back and forth a few times a second and you get real, measurable cents of bend from nothing but a capacitor and a resistor that can change its own value.</p>
'@
Wrap '<p>Almost every amp' "<p>Magnatone's engineer found" $c1
$c2=@'
<h2>A patent, an organ company, and a resistor made of sand</h2>

<p>The engineer was Don L. Bonham, who joined Magnatone in early 1957 from the organ world, where he had been patenting phase-shift vibrato circuits since 1954.<sup><a href="#iam-s4">[4]</a></sup><sup><a href="#iam-s5">[5]</a></sup> The idea traces to a 1953 oscilloscope trick by Robert Moses: an RC bridge whose output phase swings as you vary the resistance. Bonham filed the patent that defines the Magnatone sound in October 1958, number 2,988,706, with two stereo patents the next year.<sup><a href="#iam-s5">[5]</a></sup></p>

<p>The clever part is what varies the resistance. Bonham used varistors: discs of sintered silicon carbide whose resistance collapses as the voltage across them rises. Drive them with a slow oscillator and they become a resistor that changes its mind several times a second, over about a 25:1 range, with no moving parts.<sup><a href="#iam-s5">[5]</a></sup> Billy Gibbons called the varistor "an oddball device."<sup><a href="#iam-s7">[7]</a></sup></p>

<p>It is also why a Magnatone sounds like a Magnatone. Silicon carbide is lopsidedly non-linear, the tube driving it clips harder one way than the other, and the feed resistor compresses the top of the sweep, so the pitch snaps up fast and sags back slowly. In the model below, at full depth around 1 kHz, the upward bend is nearly three times the downward one. Less a sine wave, more a wrist.</p>

<p>If you are hunting one: a dead vibrato is nearly always tubes, sockets, leaky coupling caps or a stopped oscillator, so check those before you blame the varistors.<sup><a href="#iam-s5">[5]</a></sup> The originals are long gone; Estey sold the last of the stock at factory moving sales between 1968 and 1972.<sup><a href="#iam-s23">[23]</a></sup></p>
'@
Wrap '<h2>A patent' '<p>For anyone hunting' $c2
$c3=@'
<p>Nobody has published the spring count or decay of the original tanks, so the reverbs in the last widget are informed approximations.<sup><a href="#iam-s20">[20]</a></sup></p>

<h2>The transistor coda, 1967 to 1969</h2>

<p>In November 1967 Magnatone went solid state with the Brutes, topping out at the 300-watt-peak M35 "The Killer," which the 1969 catalog called "the only amplifier in the world with the thrilling effect of STEREO VIBRATO."<sup><a href="#iam-s21">[21]</a></sup> There were no varistors inside. Engineer Bill Layton kept the Moses bridge but swapped the silicon carbide for an incandescent lamp shining on cadmium sulfide photocells, two per channel, each the resistive arm of a bridge against a 0.01 microfarad capacitor, with a transistor phase splitter in place of the triode.<sup><a href="#iam-s5">[5]</a></sup><sup><a href="#iam-s24">[24]</a></sup> A lamp has thermal lag and a photocell darkens slowly, so the sweep is smoother than the varistor version and shallows at fast rates. The transistor mode in the widgets uses those values. Production ran until late 1970; the company went out still refusing to fake its vibrato.<sup><a href="#iam-s4">[4]</a></sup><sup><a href="#iam-s24">[24]</a></sup></p>

<h2>The Uni-Vibe, the cousin from Japan</h2>

<p>In 1967 Fumio Mieda in Japan was finishing the same idea in a pedal. Honey sold it as the Vibra Chorus, Shin-ei took it over, and Univox put it in American stores in 1968 as the Uni-Vibe, where Jimi Hendrix made it the sound of Woodstock.<sup><a href="#iam-s25">[25]</a></sup> Inside, it is Bonham's circuit almost component for component: four transistor phase splitters, each feeding a bridge with a photocell as the swept arm, four cells under one lamp. The differences make it a different instrument. Magnatone used two identical stages per channel, so the sweep comes out as a clean pitch bend. The Uni-Vibe staggers its four stages across the spectrum, so different parts of the note bend at different moments, and its Chorus switch mixes the swept signal with the dry one, turning moving phase into moving notches. That is why the world calls it a phaser. Flip it to Vibrato, which drops the dry signal, and it is a four-stage mono Magnatone in a pedal.<sup><a href="#iam-s25">[25]</a></sup> Nobody sued anybody: Bonham's patents were American, Honey built in Japan, and by 1967 the optical phase stage was already in organ kits and Ampeg amps.<sup><a href="#iam-s5">[5]</a></sup></p>

<h2>Pick an amp and hear it</h2>

<p>Six of the amps above with their actual feature sets: mono or stereo, one or two modulator stages, reverb only where the real amp had it. The oscilloscope shows the note as it leaves the speakers.</p>
'@
Wrap '<p>Nobody has published' '<p>Six of the amps' $c3
$t=$t -replace "`r`n","`n"
[IO.File]::WriteAllText("$d\post_content_v9.html",$t,$enc)
"bytes " + [IO.File]::ReadAllBytes("$d\post_content_v9.html").Length
(Get-FileHash "$d\post_content_v9.html" -Algorithm SHA256).Hash.ToLower()
$pv=[IO.File]::ReadAllText("$d\magnatone_preview_v8.html",$enc)
$a=$pv.IndexOf('<div class="iam-post'); $b=$pv.LastIndexOf('</body>')
[IO.File]::WriteAllText("$d\magnatone_preview_v9.html",$pv.Substring(0,$a)+$t+"`n"+$pv.Substring($b),$enc)
"preview written"
