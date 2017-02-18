function Invoke-SQL {
    param(
        [string] $dataSource = "localhost",
        [string] $database = "master",
        [string] $sqlCommand = $(throw "Please specify a query.")
      )

    $connectionString = "Data Source=$dataSource; " +
            "Integrated Security=SSPI; " +
            "Initial Catalog=$database"

    $connection = new-object system.data.SqlClient.SQLConnection($connectionString)
    $command = new-object system.data.sqlclient.sqlcommand($sqlCommand,$connection)
    $connection.Open()

    Write-Host $connection.database

    $adapter = New-Object System.Data.sqlclient.sqlDataAdapter $command
    $dataset = New-Object System.Data.DataSet
    $adapter.Fill($dataSet) | Out-Null

    $connection.Close()
    # return $dataSet.Tables
    # Write-Host $dataSet.Tables.Count
    $dataSet.Tables[0] | Out-GridView -Wait
    
}

$tab = Invoke-SQL -sqlCommand "SELECT GETDATE() AS dt;"
# Write-Host $tab[0]
# $tab
# $tab[0] | Out-GridView -Wait
# $x = Get-ChildItem -Attributes Directory
# Out-GridView -InputObject $x
    # $dataSet.Tables | Out-GridView 
