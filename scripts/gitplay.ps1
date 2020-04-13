# This script will automate the process of creating a repo on Github and pushing contents to it.

cls

$UserName = $args[0]

$RepoName = $args[1]

$newrepo = $args[2]

$RepoPath = $args[3]



cd scripts

$RepoPath = Get-Content path.txt

cd ..



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

$init_exist = dir -Force | ?{$_.name -eq ".git"}
if($init_exist)
{
   Remove-Item .git -Force -Recurse
}

writeLog($newrepo)
# Initiating repo
$git_init = git init

writeLog($git_init)

# Adding files to staging area

$git_add = git add *

writeLog("added the files from $RepoPath to repository")

# Commit the changes

$git_commit = git commit -m "initial commit with GitLearn"

writeLog($git_commit)
 try
 {
    # remove origin if it exists
    git remote rm origin
 }
 catch
 {
    #pass
 }
 try
 {
    # adding a remote
    $remote_add = git remote add origin https://github.com/$UserName/$RepoName.git
    writeLog("a remote is added")
 }
 catch
 {
    writeLog("Error Occured while adding a remote")
 }

 if($newrepo -eq "0")
 {
    try
    {
        git pull --rebase origin master
        writeLog("pull, downloaded the remote content")
    }
    catch
    {
        writeLog("Went wrong with git pull")
    }
 }

 #pushing the contents to repo
 $git_push = git push origin master
 writeLog("Pushed files into repo")


 Set-Location $cwd


