

# Current directory as an argument
$cwd = $args[0]

$cwd = Get-Content path.txt

Set-Location $cwd
cd logs

$FileExists = ls | ? {$_.Name -eq "setup.txt"}

# Checkinng if a file exists
if(-not $FileExists)
{
    New-Item setup.txt
    Add-Content setup.txt "`n===============================Setup logs started===============================`n"
}

# check logs/setup.txt for info

try
{
    $git_version = git --version
    $timestamp =($(get-date -f MM-dd-yyyy)+" "+$(get-date -f HH_mm_ss))
    Add-Content setup.txt "$timestamp : Git already downloaded - $git_version" 
}
catch
{
    choco install git
    $timestamp = ($(get-date -f MM-dd-yyyy)+" "+$(get-date -f HH_mm_ss))
    Add-Content setup.txt "$timestamp : Git installed succesfully!!"
}