param(
    [string]$InputFile,
    [int]$LinesPerFile = 100
)

if (!(Test-Path $InputFile)) {
    Write-Host "文件不存在: $InputFile"
    exit
}

$folder = Split-Path $InputFile
$name = [System.IO.Path]::GetFileNameWithoutExtension($InputFile)
$ext = [System.IO.Path]::GetExtension($InputFile)

$lines = Get-Content $InputFile -Encoding UTF8

$count = 0
$fileIndex = 1

while ($count -lt $lines.Count) {

    $start = $count
    $end = [Math]::Min($count + $LinesPerFile - 1, $lines.Count - 1)

    $output = Join-Path $folder ("{0}_part_{1:D3}{2}" -f $name,$fileIndex,$ext)

    $lines[$start..$end] | Set-Content $output -Encoding UTF8

    Write-Host "生成: $output ($($end-$start+1) 行)"

    $count += $LinesPerFile
    $fileIndex++
}

Write-Host "完成，共生成 $($fileIndex-1) 个文件"
