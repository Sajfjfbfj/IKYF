# fix-links.ps1
# association 配下の全HTMLで、的場の水鏡.html へのリンクを同じタブで開くようにする
# ※ このファイルは「ホームページ素材」フォルダに置いて、そこで実行してください

$root = Join-Path $PSScriptRoot "site-complete\association"

if (-not (Test-Path -LiteralPath $root)) {
    Write-Host "フォルダが見つかりません: $root"
    exit 1
}

# 「的場の水鏡」を文字コードから組み立てる(文字化け対策)
$name = -join ([char[]](0x7684, 0x5834, 0x306E, 0x6C34, 0x93E1))

# 的場の水鏡.html を指す <a ...> 開始タグにマッチ(../ の深さが違っても対応)
$tagPattern = '<a\b[^>]*href="[^"]*' + [regex]::Escape($name) + '\.html"[^>]*>'

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$changed = 0

Get-ChildItem -LiteralPath $root -Filter *.html -Recurse -File | ForEach-Object {
    $path = $_.FullName
    $text = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)

    $new = [regex]::Replace($text, $tagPattern, {
        param($m)
        $tag = $m.Value
        $tag = $tag -replace '\s+target="_blank"', ''
        $tag = $tag -replace '\s+rel="noopener"', ''
        $tag
    })

    if ($new -ne $text) {
        [System.IO.File]::WriteAllText($path, $new, $utf8NoBom)
        Write-Host "Updated: $path"
        $changed++
    }
}

Write-Host "Done: $changed file(s) updated"