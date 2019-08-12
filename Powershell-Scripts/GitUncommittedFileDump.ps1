$GitStatus = git status -s
$DestDir = '/UncommittedFiles'

if(!(Test-Path -Path $DestDir )) {
    New-Item -Path $DestDir -ItemType Directory
}
foreach($line in $GitStatus) {
    if("?M".Contains($line[1])) {
        $targetFile = $line.ToString().Substring($line.ToString().LastIndexOf(" ")+1)
        Write-host $TargetFile
        Copy-Item $TargetFile -Destination $DestDir
    }
}