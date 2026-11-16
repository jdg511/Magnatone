$d="C:\Users\Jason\ClaudeNotify\magnatone"
$enc=New-Object Text.UTF8Encoding($false)
$t=[IO.File]::ReadAllText("$d\post_content_v6.html",$enc)
$old='.iam-post .iam-st{color:#f2a33c;font-weight:700;white-space:nowrap}'
$new=$old+"`n.iam-post table.iam-tbl tr.iam-dt td{border-bottom:0;padding-bottom:4px}`n.iam-post table.iam-tbl tr.iam-nt td{padding:2px 10px 16px;font-size:13.5px;line-height:1.55;opacity:.92}`n.iam-post table.iam-tbl tr.iam-nt .iam-nl{display:block;font-size:11.5px;text-transform:uppercase;letter-spacing:.05em;opacity:.7;margin:0 0 3px}"
if(([regex]::Matches($t,[regex]::Escape($old))).Count -ne 1){ throw "css anchor count wrong" }
$t=$t.Replace($old,$new)
$m=[regex]::Match($t,'(?s)<table class="iam-tbl">.*?</table>')
if(-not $m.Success){ throw "table not found" }
$tbl=$m.Value
$rows=[regex]::Matches($tbl,'(?s)<tr><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>')
if($rows.Count -ne 4){ throw "row count $($rows.Count)" }
$out=New-Object Collections.Generic.List[string]
$out.Add('<table class="iam-tbl">')
$out.Add('<tr><th>Series</th><th>Years</th><th>Vibrato models</th><th>Reverb</th></tr>')
foreach($r in $rows){
  $g=$r.Groups
  $out.Add('<tr class="iam-dt"><td>'+$g[1].Value+'</td><td>'+$g[2].Value+'</td><td>'+$g[3].Value+'</td><td>'+$g[4].Value+'</td></tr>')
  $out.Add('<tr class="iam-nt"><td colspan="4"><span class="iam-nl">Notes</span>'+$g[5].Value+'</td></tr>')
}
$out.Add('</table>')
$t=$t.Replace($tbl,($out -join "`n"))
[IO.File]::WriteAllText("$d\post_content_v6b.html",$t,$enc)
"bytes " + [IO.File]::ReadAllBytes("$d\post_content_v6b.html").Length
(Get-FileHash "$d\post_content_v6b.html" -Algorithm SHA256).Hash.ToLower()
$pv=[IO.File]::ReadAllText("$d\magnatone_preview_v5.html",$enc)
$i=$pv.IndexOf('<div class="iam-post">'); $j=$pv.LastIndexOf('</body>')
[IO.File]::WriteAllText("$d\magnatone_preview_v6.html",$pv.Substring(0,$i)+$t+"`n"+$pv.Substring($j),$enc)
"preview written"
