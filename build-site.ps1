param([string]$OutputDirectory = "site", [int]$Limit = 0)

$ErrorActionPreference = "Stop"
$siteRoot = "https://www.kyudo.jp"
$outputRoot = Join-Path $PSScriptRoot $OutputDirectory
$menuCssSource = Join-Path $PSScriptRoot "site-menu.css"
$menuJsSource = Join-Path $PSScriptRoot "site-menu.js"
$encoding = New-Object System.Text.UTF8Encoding($false)
Add-Type -AssemblyName System.Net.Http
$handler = New-Object System.Net.Http.HttpClientHandler
$handler.AutomaticDecompression = [System.Net.DecompressionMethods]::GZip -bor [System.Net.DecompressionMethods]::Deflate
$client = New-Object System.Net.Http.HttpClient($handler)
$client.Timeout = [TimeSpan]::FromSeconds(35)

function Get-LocalPath([string]$url) {
  $path = [Uri]::UnescapeDataString(([Uri]$url).AbsolutePath).TrimStart("/")
  if (-not $path) { return "index.html" }
  if ($path.EndsWith("/")) { return "$($path)index.html" }
  return $path
}

function Get-RelativeLink([string]$fromFile, [string]$toFile) {
  $from = [Uri]::new((Join-Path (Split-Path $fromFile -Parent) "_from.html"))
  $to = [Uri]::new($toFile)
  return [Uri]::UnescapeDataString($from.MakeRelativeUri($to).ToString())
}

function ConvertTo-PlainText([string]$value) {
  $value = [regex]::Replace($value, "(?is)<(script|style|noscript)\b[^>]*>.*?</\1>", " ")
  $value = [regex]::Replace($value, "(?s)<[^>]+>", " ")
  return (([System.Net.WebUtility]::HtmlDecode($value) -replace "\s+", " ").Trim())
}

function Escape([string]$value) { return [System.Net.WebUtility]::HtmlEncode($value) }

function Get-PageData([string]$url, [string]$html) {
  $headings = @([regex]::Matches($html, "(?is)<h[1-6]\b[^>]*>(.*?)</h[1-6]>") | ForEach-Object { ConvertTo-PlainText $_.Groups[1].Value } | Where-Object { $_.Length -ge 3 -and $_.Length -le 120 })
  $match = [regex]::Match($html, '(?is)<meta\s+property=["'']og:title["'']\s+content=["'']([^"'']+)')
  $title = if ($match.Success) { ConvertTo-PlainText $match.Groups[1].Value } elseif ($headings.Count) { $headings | Sort-Object Length -Descending | Select-Object -First 1 } else { [IO.Path]::GetFileName(([Uri]$url).AbsolutePath.TrimEnd('/')) }
  $dateMatch = [regex]::Match($html, '(?<!\d)(20\d{2})[./年-](\d{1,2})[./月-](\d{1,2})')
  $date = if ($dateMatch.Success) { "{0}.{1}.{2}" -f $dateMatch.Groups[1].Value, $dateMatch.Groups[2].Value.PadLeft(2, '0'), $dateMatch.Groups[3].Value.PadLeft(2, '0') } else { "" }
  $documents = @([regex]::Matches($html, '(?is)<a\b[^>]*href=["'']([^"'']+\.(?:pdf|docx?|xlsx?)(?:\?[^"'']*)?)["''][^>]*>(.*?)</a>') | ForEach-Object {
    $href = [System.Net.WebUtility]::HtmlDecode($_.Groups[1].Value)
    $label = ConvertTo-PlainText $_.Groups[2].Value
    $documentUri = [Uri]::new([Uri]$siteRoot, $href)
    if (-not $label) { $label = [IO.Path]::GetFileName($documentUri.AbsolutePath) }
    [PSCustomObject]@{ Url = $documentUri.AbsoluteUri; Label = $label }
  } | Sort-Object Url -Unique)
  $path = ([Uri]$url).AbsolutePath.ToLowerInvariant()
  $category = if ($path -match '^/taikai/') { "全国大会" } elseif ($path -match '^/chuoshinsa/') { "中央審査会" } elseif ($path -match '^/region/') { "地方審査会" } elseif ($path -match '^/association/') { "連合審査会" } elseif ($path -match '^/notice/') { "連盟からのお知らせ" } elseif ($path -match '^/howto/') { "弓道の心" } elseif ($path -match '^/begin/') { "見学・入門" } elseif ($path -match '^/aboutus/') { "連盟について" } elseif ($path -match '^/map/') { "全国弓道場" } elseif ($path -match '^/info/') { "ご案内" } else { "大会・審査情報" }
  $summary = switch ($category) {
    "全国大会" { "全国規模の弓道大会に関する実施要項、立順、結果などを掲載しています。" }
    "中央審査会" { "中央審査会に関する日程、進行情報、結果などを掲載しています。" }
    "地方審査会" { "各地域の審査会に関する日程や案内を掲載しています。" }
    "連合審査会" { "連合審査会に関する日程や案内を掲載しています。" }
    "連盟からのお知らせ" { "全日本弓道連盟からのお知らせと関連資料を掲載しています。" }
    "弓道の心" { "弓道の精神や歴史、射法について紹介します。" }
    "見学・入門" { "弓道を始める方に向けた案内や道具、よくある質問をまとめています。" }
    "連盟について" { "全日本弓道連盟の組織、活動、刊行物に関する情報です。" }
    "全国弓道場" { "全国の弓道場に関する情報を掲載しています。" }
    "ご案内" { "各種方針、窓口、関連情報をご案内します。" }
    default { "大会・審査会に関する情報を掲載しています。" }
  }
  return [PSCustomObject]@{ Url = $url; Title = $title; Date = $date; Category = $category; Summary = $summary; Documents = $documents }
}

function Write-Page([object]$data, [string]$filePath) {
  New-Item -ItemType Directory -Path (Split-Path $filePath -Parent) -Force | Out-Null
  $homeLink = Get-RelativeLink $filePath (Join-Path $outputRoot "index.html")
  $allLink = Get-RelativeLink $filePath (Join-Path $outputRoot "all-pages.html")
  $menuCssLink = Escape (Get-RelativeLink $filePath (Join-Path $outputRoot "site-menu.css"))
  $menuJsLink = Escape (Get-RelativeLink $filePath (Join-Path $outputRoot "site-menu.js"))
  $title = Escape $data.Title; $category = Escape $data.Category; $summary = Escape $data.Summary
  $dateBlock = if ($data.Date) { "<time>$($data.Date)</time>" } else { "" }
  $documentLinks = @($data.Documents | ForEach-Object { '<li><a href="' + (Escape $_.Url) + '" target="_blank" rel="noopener">' + (Escape $_.Label) + '</a></li>' }) -join "`n"
  if (-not $documentLinks) { $documentLinks = '<li class="quiet">このページに関連する資料リンクはありません。</li>' }
  $sourceUrl = Escape $data.Url
  $html = @"
<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="$summary"><title>$title｜全日本弓道連盟</title><link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@400;600&display=swap" rel="stylesheet"><style>
:root{color-scheme:dark;--bg:#14121c;--ink:#f3eef8;--sub:rgba(243,238,248,.72);--line:rgba(243,238,248,.18);--accent:#b79be0}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-family:"Shippori Mincho","Yu Mincho",serif;line-height:1.9}a{color:inherit;text-decoration:none}a:hover{color:var(--accent)}a:focus-visible{outline:2px solid var(--accent);outline-offset:4px}.top{padding:30px 7vw 24px;border-bottom:1px solid var(--line);display:flex;align-items:center;justify-content:space-between;gap:24px}.brand b{display:block;font-size:18px;letter-spacing:.16em}.brand span{font:11px Arial,sans-serif;letter-spacing:.12em;color:var(--sub)}.top nav{display:flex;gap:24px;flex-wrap:wrap;font-size:13px;letter-spacing:.12em}.wrap{width:min(900px,86vw);margin:0 auto;padding:8vh 0 12vh}.crumb{font-size:12px;letter-spacing:.1em;color:var(--sub);margin-bottom:8vh}.crumb span{padding:0 .7em;color:var(--accent)}.eyebrow{font-size:12px;letter-spacing:.22em;color:var(--accent)}h1{font-size:clamp(30px,5vw,56px);font-weight:600;line-height:1.5;letter-spacing:.14em;margin:.5em 0 .7em;overflow-wrap:anywhere}.meta{display:flex;gap:1.5em;align-items:center;color:var(--sub);font-size:13px;border-bottom:1px solid var(--line);padding-bottom:1.5em}.summary{font-size:17px;line-height:2.1;max-width:42em;margin:3em 0 4em}.materials h2{font-size:19px;letter-spacing:.16em;font-weight:600;margin:0 0 1em}.materials ul{list-style:none;margin:0;padding:0;border-top:1px solid var(--line)}.materials li{padding:1em 0;border-bottom:1px solid var(--line)}.quiet{color:var(--sub);font-size:14px}.source{margin-top:4em;font-size:13px;color:var(--sub)}.source a{border-bottom:1px solid var(--accent);padding-bottom:.2em}.bottom{border-top:1px solid var(--line);padding:24px 7vw 42px;color:var(--sub);font-size:12px;display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}@media(max-width:650px){.top{align-items:flex-start;flex-direction:column}.top nav{gap:12px 18px}.wrap{padding-top:6vh}.crumb{margin-bottom:5vh}.summary{font-size:15px}}
</style></head><body><header class="top"><a class="brand" href="$homeLink"><b>全日本弓道連盟</b><span>All Nippon Kyudo Federation</span></a><nav aria-label="ページ"><a href="$allLink">全ページ一覧</a><a href="$homeLink">トップ</a></nav></header><main class="wrap"><div class="crumb"><a href="$homeLink">HOME</a><span>›</span>$category</div><p class="eyebrow">$category</p><h1>$title</h1><div class="meta">$dateBlock<span>公益財団法人 全日本弓道連盟</span></div><p class="summary">$summary</p><section class="materials"><h2>関連資料</h2><ul>$documentLinks</ul></section><p class="source"><a href="$sourceUrl" target="_blank" rel="noopener">公式サイトの掲載内容を確認する</a></p></main><footer class="bottom"><span>公益財団法人 全日本弓道連盟</span><a href="$allLink">全ページ一覧</a></footer></body></html>
"@
  $html = $html.Replace("</head>", '<link rel="stylesheet" href="' + $menuCssLink + '"></head>')
  $html = $html.Replace("</body>", '<script src="' + $menuJsLink + '" defer></script></body>')
  [IO.File]::WriteAllText($filePath, $html, $encoding)
}

New-Item -ItemType Directory -Path $outputRoot -Force | Out-Null
Copy-Item $menuCssSource (Join-Path $outputRoot "site-menu.css") -Force
Copy-Item $menuJsSource (Join-Path $outputRoot "site-menu.js") -Force
$sitemapIndex = [xml]$client.GetStringAsync("$siteRoot/wp-sitemap.xml").GetAwaiter().GetResult()
$ns = New-Object System.Xml.XmlNamespaceManager($sitemapIndex.NameTable)
$ns.AddNamespace("s", "http://www.sitemaps.org/schemas/sitemap/0.9")
$urls = [System.Collections.Generic.List[string]]::new()
foreach ($map in $sitemapIndex.SelectNodes("//s:sitemap/s:loc", $ns)) {
  $xml = [xml]$client.GetStringAsync($map.InnerText).GetAwaiter().GetResult()
  foreach ($node in $xml.SelectNodes("//s:url/s:loc", $ns)) { $urls.Add($node.InnerText) }
}
$required = @("/", "/howto/", "/howto/history.html", "/howto/syaho.html", "/howto/terminology.html", "/begin/", "/begin/tool.html", "/begin/faq.html", "/improve/", "/movie/", "/schedule/", "/schedule/taikai/", "/schedule/chuoshinsa/", "/schedule/association/", "/schedule/region/", "/documents/", "/map/", "/schedule/chuoshinsa/overview.html", "/aboutus/", "/aboutus/overview.html", "/aboutus/plan.html", "/aboutus/org.html", "/aboutus/recruit.html", "/aboutus/book.html", "/aboutus/officialgoods.html", "/aboutus/rule.html", "/aboutus/latestissue.html", "/notice/", "/info/contact.html", "/info/english.html", "/info/usearrow.html", "/info/guidelines.html", "/info/personalinfo.html", "/info/link.html")
foreach ($path in $required) { $urls.Add(([Uri]::new([Uri]$siteRoot, $path)).AbsoluteUri) }
$urls = @($urls | Sort-Object -Unique)
$urls = @($urls | Where-Object { ([Uri]$_).AbsolutePath -ne "/" })
if ($Limit -gt 0) { $urls = @($urls | Select-Object -First $Limit) }
$records = [System.Collections.Generic.List[object]]::new()
$batch = [System.Collections.Generic.List[object]]::new()
$completed = 0
foreach ($url in $urls) {
  $batch.Add([PSCustomObject]@{ Url = $url; Task = $client.GetStringAsync($url) })
  if ($batch.Count -ge 12 -or $url -eq $urls[-1]) {
    foreach ($item in $batch) {
      $html = ""; try { $html = $item.Task.GetAwaiter().GetResult() } catch { }
      $data = Get-PageData $item.Url $html
      $filePath = Join-Path $outputRoot (Get-LocalPath $item.Url)
      Write-Page $data $filePath
      $records.Add([PSCustomObject]@{ Url = $data.Url; Path = (Get-LocalPath $data.Url); Title = $data.Title; Date = $data.Date; Category = $data.Category; Documents = $data.Documents })
      $completed++
    }
    $batch.Clear()
    Write-Progress -Activity "ページ生成" -Status "$completed / $($urls.Count)" -PercentComplete (100 * $completed / $urls.Count)
  }
}
Write-Progress -Activity "ページ生成" -Completed

$homeHtml = [IO.File]::ReadAllText((Join-Path $PSScriptRoot "index.html"))
$homeHtml = $homeHtml.Replace('K="https://www.kyudo.jp"', 'K="."')
$homeHtml = [regex]::Replace($homeHtml, 'href="https://www\.kyudo\.jp(/[^"#?]*)"', 'href=".$1"')
$homeHtml = [regex]::Replace($homeHtml, 'href="\./([^".][^"]*\.(?:pdf|docx?|xlsx?))"', 'href="https://www.kyudo.jp/$1"', [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
$homeHtml = $homeHtml.Replace('<div id="ui">', '<div class="site-index-link"><a href="./all-pages.html">サイト内の全ページを見る</a></div><div id="ui">')
$homeHtml = $homeHtml.Replace('このページはデザイン試作です。公式サイトは <a href="./">www.kyudo.jp</a> です。', 'サイト内の各ページをこのデザインでご覧いただけます。')
$homeHtml = $homeHtml.Replace('</style>', '.site-index-link{position:fixed;z-index:4;right:5vw;bottom:2vh;font-size:12px;letter-spacing:.12em;color:var(--sub)}.site-index-link a{border-bottom:1px solid var(--accent);padding-bottom:.25em}</style>')
[IO.File]::WriteAllText((Join-Path $outputRoot "index.html"), $homeHtml, $encoding)

$groups = $records | Group-Object Category | Sort-Object Name
$sections = foreach ($group in $groups) {
  $rows = foreach ($record in ($group.Group | Sort-Object Title)) {
    $target = Join-Path $outputRoot $record.Path
    $href = Get-RelativeLink (Join-Path $outputRoot "all-pages.html") $target
    '<li><a href="' + (Escape $href) + '">' + (Escape $record.Title) + '</a><span>' + (Escape $record.Date) + '</span></li>'
  }
  '<section class="group"><h2>' + (Escape $group.Name) + '<small>' + $group.Count + '</small></h2><ul>' + ($rows -join "`n") + '</ul></section>'
}
$allPages = @"
<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>全ページ一覧｜全日本弓道連盟</title><link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@400;600&display=swap" rel="stylesheet"><style>
:root{color-scheme:dark;--bg:#14121c;--ink:#f3eef8;--sub:rgba(243,238,248,.72);--line:rgba(243,238,248,.18);--accent:#b79be0}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-family:"Shippori Mincho","Yu Mincho",serif;line-height:1.8}a{color:inherit;text-decoration:none}a:hover{color:var(--accent)}header,footer{padding:26px 7vw;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;gap:20px}header b{display:block;letter-spacing:.16em}header span,footer{font-size:12px;color:var(--sub)}main{width:min(1000px,86vw);margin:7vh auto 12vh}h1{font-size:clamp(30px,5vw,52px);letter-spacing:.16em;font-weight:600;margin:0 0 .4em}.intro{color:var(--sub);margin:0 0 3em}input{width:100%;background:transparent;color:var(--ink);font:inherit;border:1px solid var(--line);padding:14px 16px;margin-bottom:4em}input:focus{outline:2px solid var(--accent)}.group{margin:0 0 4em}.group h2{font-size:20px;letter-spacing:.14em;border-bottom:1px solid var(--accent);padding-bottom:.6em}.group small{font:12px Arial,sans-serif;color:var(--sub);margin-left:1em}.group ul{padding:0;margin:0;list-style:none}.group li{display:grid;grid-template-columns:1fr 9em;gap:1em;padding:.8em 0;border-bottom:1px solid var(--line)}.group li span{text-align:right;color:var(--sub);font-size:12px}@media(max-width:600px){.group li{grid-template-columns:1fr}.group li span{text-align:left}}
</style></head><body><header><a href="index.html"><b>全日本弓道連盟</b><span>All Nippon Kyudo Federation</span></a><a href="index.html">トップへ</a></header><main><p class="intro">サイトマップ掲載ページと主要案内ページ</p><h1>全ページ一覧</h1><input id="q" type="search" placeholder="ページ名で検索" aria-label="ページ名で検索">$($sections -join "`n")</main><footer><span>公益財団法人 全日本弓道連盟</span><a href="index.html">トップへ戻る</a></footer><script>document.getElementById('q').addEventListener('input',function(){var q=this.value.trim().toLowerCase();document.querySelectorAll('.group').forEach(function(g){var rows=g.querySelectorAll('li');var shown=0;rows.forEach(function(r){var match=r.textContent.toLowerCase().includes(q);r.hidden=!match;if(match)shown++;});g.hidden=!shown;});});</script></body></html>
"@
"@
$allPages = $allPages.Replace("</head>", '<link rel="stylesheet" href="site-menu.css"></head>')
$allPages = $allPages.Replace("</body>", '<script src="site-menu.js" defer></script></body>')
[IO.File]::WriteAllText((Join-Path $outputRoot "all-pages.html"), $allPages, $encoding)
$client.Dispose()
Write-Host "Generated $($records.Count) pages in $outputRoot"