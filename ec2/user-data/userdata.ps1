<powershell>
# Define download URL for Apache HTTP server
$downloadUrl = "https://www.apachelounge.com/download/VS17/binaries/httpd-2.4.58-240131-win64-VS17.zip"

# Define where to save the downloaded zip
$zipPath = "C: \apache.zip"

# Use web client to downlaod instead
$WebClient = New-Object System.Net.WebClient
$WebClient.DownloadFile($downloadUrl, $zipPath)

# Define extraction path
$extractPath = "C:\"

# Extract the zip file
Expand-Archive -Path $zipPath -DestinationPath $extractPath

# Remove the downloaded zip file to save space
Remove-Item -Path $zipPath

# Install Apache as a windows service
$httpdPath = Join-Path -Path $extractPath -ChildPath "Apache24\bin\httpd.exe"
Start-Process -FilePath $httpdPath -ArgumentList "-k install -d C:\Apache24" -Wait

# Start the Apache service
Start-Service -Name "Apache2.4"
</powershell>