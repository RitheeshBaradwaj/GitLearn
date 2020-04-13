cls



cd scripts

$RepoPath = Get-Content path.txt

cd ..

$RepoUrl = $args[0]

$cwd = pwd

cd logs

$FileExists = ls | ? {$_.Name -eq "gitplay.txt"}

# Checkinng if a file exists
if(-not $FileExists)
{
    New-Item gitplay.txt
    Add-Content gitplay.txt "`n===============================GitPlay logs started===============================`n"
}


$FileExists = ls | ?{$_.Name -eq "description.txt"}

if($FileExists)
{
    $Description = Get-Content description.txt
}
else
{
    $Description = "This repo was made with GitLearn"
}

# To write status into a file

function writeLog($msg)
{
    Set-Location $cwd
    cd logs
    $timestamp =($(get-date -f MM-dd-yyyy)+" "+$(get-date -f HH_mm_ss))
    Add-Content gitplay.txt "$timestamp : $msg"
    Set-Location $RepoPath
}


Set-Location $RepoPath

# Cloning repo

git clone $RepoUrl

writeLog("Repository is cloned")

Set-Location $cwd