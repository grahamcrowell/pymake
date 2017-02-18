Write-Host $PSScriptRoot

Import-Module sqlps -DisableNameChecking

$SqlServerName = "localhost"
$SqlServer = New-Object Microsoft.SqlServer.Management.Smo.Server($SqlServerName)

$db = "CommunityMart"
# $SqlServer.Databases["master"].ExecuteNonQuery("CREATE DATABASE CommunityMart;")

# $dir = "C:\Users\user\Documents\GitHub\CommunityMart\Database\Table"
# Get-ChildItem $dir -Filter *.sql | 
# Foreach-Object {
#     $SqlScript = $_.FullName
#     Write-Host $SqlScript
#     $command = (Get-Content -Path $SqlScript)
#     # Write-Host $command
#     $SqlServer.Databases[$db].ExecuteNonQuery($command)
# }


$SqlScript="$PSScriptRoot\test.sql"
# Write-Host $SqlScript
# $SqlServer.Databases["CommunityMart"].ExecuteNonQuery((Get-Content -Path $SqlScript))
try {
        $SqlServer.Databases["master"].ExecuteNonQuery((Get-Content -Path $SqlScript))
    }
    catch {
        Write-Error $_.Exception
    }

