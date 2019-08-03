$keyword = Read-Host -Prompt 'Enter keyword:'
$javaActive = jps -l | select-string $keyword

for($i = 0; $i -lt $javaActive.length; $i++) { 
    Write-host $javaActive[$i]
    $targetPid = $javaActive[$i].ToString().Substring(0,$javaActive[$i].ToString().IndexOf(" "))
    $result = taskkill /f /pid $targetPid
    Write-Host $result
}