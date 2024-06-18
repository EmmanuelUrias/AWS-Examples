Import-Module AWS.Tools.S3

$bucketName = Read-Host -Prompt 'Enter the S3 bucket name'

Write-Host "S3 Bucket: $bucketName"

Remove-S3Bucket -BucketName $bucketName

Write-Host "Deleted $bucketName"