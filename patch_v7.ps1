$d="C:\Users\Jason\ClaudeNotify\magnatone"
$enc=New-Object Text.UTF8Encoding($false)
$t=[IO.File]::ReadAllText("$d\post_content_v6b.html",$enc)
$n=0
$o=@'
Every moving graphic and every sound on this page is generated live by a model of the real Magnatone circuit, not a recording.
'@
$w=@'
Every moving graphic and every sound on this page is generated live by a model of the real Magnatone circuit, so what you see and hear is the math of the thing, not a recording.
'@
if(([regex]::Matches($t,[regex]::Escape($o))).Count -ne 1){ throw "anchor $n" }; $t=$t.Replace($o,$w); $n++
$o=@'
<p>Frequency is the rate at which a waveform's phase goes by.
'@
$w=@'
<p>To understand why nobody else did this, think about what pitch shifting actually requires. Frequency is the rate at which a waveform's phase goes by.
'@
if(([regex]::Matches($t,[regex]::Escape($o))).Count -ne 1){ throw "anchor $n" }; $t=$t.Replace($o,$w); $n++
$o=@'
A tape loop with a wobbling playback speed was a studio trick, not something to cram next to a 6V6 and sell for $179.50. The bucket brigade chip would not be invented at Philips until 1969. Digital memory for audio was science fiction.</p>
'@
$w=@'
A tape loop with a wobbling playback speed was a studio trick, not something to cram next to a 6V6 and sell for $179.50. The bucket brigade chip, the BBD that made Small Stones and Memory Men possible, would not be invented at Philips until 1969. Digital memory for audio was science fiction. There was, on paper, no way to build a time machine out of 1957 parts.</p>
'@
if(([regex]::Matches($t,[regex]::Escape($o))).Count -ne 1){ throw "anchor $n" }; $t=$t.Replace($o,$w); $n++
$o=@'
number 2,988,706, with two stereo patents following in 1959; he left around 1961 and Estey kept building the circuit under license.
'@
$w=@'
number 2,988,706, granted in June 1961, with two stereo patents following in 1959; he left around 1961 and Estey kept building the circuit under license, renaming it Stereo F.M. Vibrato.
'@
if(([regex]::Matches($t,[regex]::Escape($o))).Count -ne 1){ throw "anchor $n" }; $t=$t.Replace($o,$w); $n++
$o=@'
so check those before you blame the sand. Estey sold its remaining varistors at factory moving sales between 1968 and 1972, which is why the real ones live in collectors' drawers.
'@
$w=@'
so check those before you blame the sand. Still, a sixty year old amp whose vibrato has gone shallow may simply have drifted varistors, or, worse, harvested ones. The original schematics say only "varistor" with no part number, Bonham himself described the original selection as slow and laborious, and Estey sold its remaining stock at factory moving sales between 1968 and 1972, which is why the real ones live in collectors' drawers.
'@
if(([regex]::Matches($t,[regex]::Escape($o))).Count -ne 1){ throw "anchor $n" }; $t=$t.Replace($o,$w); $n++
$o=@'
<p>Tony Price, who ran engineering at Estey from 1963 to 1965, had the plainest description:
'@
$w=@'
<p>Tony Price, who ran engineering at Estey from 1963 to 1965 and inherited the circuit from Bonham, had the plainest description:
'@
if(([regex]::Matches($t,[regex]::Escape($o))).Count -ne 1){ throw "anchor $n" }; $t=$t.Replace($o,$w); $n++
$o=@'
The first mass-market stereo LPs reached stores in 1958. Magnatone was shipping countersweeping stereo pitch modulation while the average record player could not yet say the word.</p>
'@
$w=@'
Sit with the date for a second. The first mass-market stereo LPs reached stores in 1958. Magnatone was shipping countersweeping stereo pitch modulation while the average record player could not yet say the word.</p>
'@
if(([regex]::Matches($t,[regex]::Escape($o))).Count -ne 1){ throw "anchor $n" }; $t=$t.Replace($o,$w); $n++
$o=@'
two cascaded stages per side, and later added a Stereo Vibrato switch that runs the sides in phase for mono or out of phase for stereo.
'@
$w=@'
two cascaded stages per side, and later added a Stereo Vibrato switch that runs the sides in phase for mono or out of phase for stereo. In the suitcase era that meant a 12DW7, two 12AU7s and eight varistors devoted to vibrato alone.
'@
if(([regex]::Matches($t,[regex]::Escape($o))).Count -ne 1){ throw "anchor $n" }; $t=$t.Replace($o,$w); $n++
$o=@'
The 480 ($499.95, eight varistors) feeds its reverb to output No. 2 only, which is why its two sides are wired in opposite polarity.
'@
$w=@'
The 480 ($499.95, 50 watts, four 6973s, two 12s and two 5x7 ovals, eight varistors) drives its Hammond-style tank with a 6DR7, recovers it with a germanium transistor, and feeds the reverb to output No. 2 only, which is why its two sides are wired in opposite polarity.
'@
if(([regex]::Matches($t,[regex]::Escape($o))).Count -ne 1){ throw "anchor $n" }; $t=$t.Replace($o,$w); $n++
$o=@'
The M10 ($380, 38 watts, four varistors) was the best seller.<sup><a href="#iam-s20">[20]</a></sup> The M14 ($460, four 7189As, eight varistors) is the 280's true successor, an M15 without reverb; the M15 went through four reverb designs in four years.
'@
$w=@'
The M10 ($380, 38 watts, four varistors) was the best seller; its 12AU7 drives a Hammond tank with transistor recovery, an updated 480 reverb.<sup><a href="#iam-s20">[20]</a></sup> The M14 ($460, four 7189As, eight varistors) is the 280's true successor, an M15 without reverb, and sold poorly against Ampeg's $380 Super Echo Twin. The M15 went through four reverb designs in four years, ending with a tank driven straight from the channel 1 speaker output and an "Echo" knob that puts a neon-lamp photocell tremolo on the reverb signal.
'@
if(([regex]::Matches($t,[regex]::Escape($o))).Count -ne 1){ throw "anchor $n" }; $t=$t.Replace($o,$w); $n++
$o=@'
The line topped out at the 300-watt-peak M35 "The Killer," two 15s, two horns, 105 pounds, and, the 1969 catalog insisted,
'@
$w=@'
The line topped out at the 300-watt-peak M35 "The Killer," two 15s, two horns, 105 pounds, a six-transistor spring reverb, and, the 1969 catalog insisted,
'@
if(([regex]::Matches($t,[regex]::Escape($o))).Count -ne 1){ throw "anchor $n" }; $t=$t.Replace($o,$w); $n++
$o=@'
and at fast rates it shallows and skews because the cell never fully recovers. Production ran until late 1970. The company went out still refusing to fake its vibrato.
'@
$w=@'
and at fast rates it shallows and skews because the cell never fully recovers. The transistor mode in the widgets uses those values, with the lamp and photocell behaviour modeled from textbook data rather than measured from an amp. The 240SV accordion amp of November 1968 kept the stereo version, and production ran until late 1970, after which the brand was mothballed. The company went out still refusing to fake its vibrato.
'@
if(([regex]::Matches($t,[regex]::Escape($o))).Count -ne 1){ throw "anchor $n" }; $t=$t.Replace($o,$w); $n++
$o=@'
and said his effect was meant to recreate the drifting sound of shortwave radio under atmospheric interference, not a Leslie. Honey sold it in Japan in 1967 as the Vibra Chorus; Shin-ei took it over,
'@
$w=@'
and said later that his effect was meant to recreate the drifting, swirling sound of shortwave radio under atmospheric interference, not a Leslie, whatever the catalogs implied. Honey sold it in Japan in 1967 as the Vibra Chorus; when Honey folded, Shin-ei took it over,
'@
if(([regex]::Matches($t,[regex]::Escape($o))).Count -ne 1){ throw "anchor $n" }; $t=$t.Replace($o,$w); $n++
$o=@'
There is no record of a dispute: Bonham's patents were American, Honey built in Japan, and by 1967
'@
$w=@'
There is no record of a dispute: Bonham's patents were American, Honey built in Japan, Mieda credited his own organ work, and by 1967
'@
if(([regex]::Matches($t,[regex]::Escape($o))).Count -ne 1){ throw "anchor $n" }; $t=$t.Replace($o,$w); $n++
$o=@'
Bo Diddley told Rolling Stone of his first one,
'@
$w=@'
Bo Diddley ran Magnatones too, and told Rolling Stone of his first one,
'@
if(([regex]::Matches($t,[regex]::Escape($o))).Count -ne 1){ throw "anchor $n" }; $t=$t.Replace($o,$w); $n++
$o=@'
Scotty Moore kept a 213 Troubadour at home for recording until the end.
'@
$w=@'
Scotty Moore, the man who invented rock and roll guitar behind Elvis, kept a late-fifties 213 Troubadour at home for recording until the end.
'@
if(([regex]::Matches($t,[regex]::Escape($o))).Count -ne 1){ throw "anchor $n" }; $t=$t.Replace($o,$w); $n++
$o=@'
Neil Young has run a vintage 280 in his live rig for decades, purely for that stereo vibrato,
'@
$w=@'
Neil Young has run a vintage 280 in his live rig for decades, with his tech feeding a padded-down Fender Deluxe output into it purely for that stereo vibrato,
'@
if(([regex]::Matches($t,[regex]::Escape($o))).Count -ne 1){ throw "anchor $n" }; $t=$t.Replace($o,$w); $n++
$o=@'
leaned on a Custom 410 and a 480 for the textures all over Arctic Monkeys' AM.
'@
$w=@'
leaned on a vintage Custom 410 and a 480 for the vibrato-soaked textures all over Arctic Monkeys' AM era.
'@
if(([regex]::Matches($t,[regex]::Escape($o))).Count -ne 1){ throw "anchor $n" }; $t=$t.Replace($o,$w); $n++
$o=@'
When the varistors ran out they did it again with a light bulb and a photocell. There are not many circuits
'@
$w=@'
When the varistors ran out they did it again with a light bulb and a photocell, and when the company ran out the idea went dormant for fifty years. There are not many circuits
'@
if(([regex]::Matches($t,[regex]::Escape($o))).Count -ne 1){ throw "anchor $n" }; $t=$t.Replace($o,$w); $n++
$o=@'
the other great misnamed modulation of the era. If the Magnatone bends time,
'@
$w=@'
the other great misnamed modulation of the era, which splits the guitar in two and rocks the halves against each other. If the Magnatone bends time,
'@
if(([regex]::Matches($t,[regex]::Escape($o))).Count -ne 1){ throw "anchor $n" }; $t=$t.Replace($o,$w); $n++
[IO.File]::WriteAllText("$d\post_content_v7.html",$t,$enc)
"applied $n"; (Get-FileHash "$d\post_content_v7.html" -Algorithm SHA256).Hash.ToLower()