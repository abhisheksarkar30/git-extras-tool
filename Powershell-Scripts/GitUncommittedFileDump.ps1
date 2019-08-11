$GitStatus = git status -s
$DestDir = '/UncommittedFiles'

for($i = 0; $i -lt $GitStatus.length; $i++) {    
    $targetFile = $GitStatus[$i].ToString().Substring($GitStatus[$i].ToString().LastIndexOf(" ")+1)
    Write-host $TargetFile
    if(!(Test-Path -Path $DestDir )){
        New-Item -Path $DestDir -ItemType Directory
    }
    Copy-Item $TargetFile -Destination $DestDir
}