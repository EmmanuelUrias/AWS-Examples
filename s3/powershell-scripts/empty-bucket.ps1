Import-Module AWS.Tools.S3

$bucketName = Read-Host -Prompt 'Enter the S3 bucket name'

Write-Host "S3 Bucket: $bucketName"

# Empties out the bucket
$keyVersions = @()
$versions = (Get-S3Version -BucketName $bucketName).Versions

foreach ($version in $versions) { 
    $keyVersions += @{ Key = $version.Key; VersionId = $version.VersionId }
}

if ($keyVersions.Count -gt 0) {
    Remove-S3Object -BucketName $bucketName -KeyAndVersionCollection $keyVersions -Force
    Write-Host "Deleted $($keyVersions.Count) objects from bucket $bucketName."
} else {
    Write-Host "No objects found in bucket $bucketName."
}
