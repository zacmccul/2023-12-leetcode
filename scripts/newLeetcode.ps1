param(
    [string]$fileName
)

if ($fileName -ne $null) {
    $rootDir = Split-Path $PSScriptRoot -Parent
    $rootDir = $rootDir + "\"
    #$filePath = $rootDir + $fileName  # Change this path to the desired directory
    Copy-Item -Path ($rootDir + "tests\_TEMPLATE.py") -Destination ($rootDir + "tests\" + $fileName + "_test.py")
    Copy-Item -Path ($rootDir + "TEMPLATE.py") -Destination ($rootDir + $fileName + ".py")
    #New-Item -ItemType File -Path $filePath # -Force
    #Set-Content -Path $filePath -Value $content
    #Write-Host "File '$fileName' created successfully at $filePath"
    
} else {
    Write-Host "Please provide a valid file name as an argument."
}