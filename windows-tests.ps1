function Find-And-Execute-Metacall {
    param (
        [Parameter(Mandatory=$true)]
        [string]$Directory
    )

    $metacallFile = "metacall.json"

    Get-ChildItem -Path $Directory -Recurse -Filter $metacallFile -File | ForEach-Object {
        $metacallPath = $_.FullName
        $jsonData = Get-Content -Raw -Path $metacallPath | ConvertFrom-Json
        $scripts = $jsonData.scripts

        if ($scripts) {
            $dirPath = Split-Path -Path $metacallPath
            $scripts | ForEach-Object {
                $scriptCommand = "metacall $($_)"
                Push-Location $dirPath
                try {
                    Invoke-Expression $scriptCommand
                    Write-Host "Executed script '$_' from $dirPath"
                } finally {
                    Pop-Location
                }
            }
        }
    }
}

# Call the function with the current working directory
Find-And-Execute-Metacall -Directory (Get-Location).Path