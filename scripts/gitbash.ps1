
$cwd = $args[0]
$cwd = Get-Content path.txt

Set-Location $cwd
cd logs

$FileExists = ls | ? {$_.Name -eq "gitbash.txt"}

# Checkinng if a file exists
if(-not $FileExists)
{
    New-Item gitbash.txt
    Add-Content gitbash.txt "`n===============================GitBash logs started===============================`n"
}

# check logs/setup.txt for info

try
{
    # starting Git Bash
    start "C:\Program Files\Git\bin\sh.exe" --login

    $timestamp =($(get-date -f MM-dd-yyyy)+" "+$(get-date -f HH_mm_ss))

    Add-Content gitbash.txt "$timestamp : Git bash opened!" 
}
catch
{
    $timestamp = ($(get-date -f MM-dd-yyyy)+" "+$(get-date -f HH_mm_ss))
    Add-Content gitbash.txt "$timestamp : Something went wrong. Please check that you have installed git"
}