# Make Buckets and sync data between them
## Make Buckets
```sh
aws s3api create-bucket --bucket my-data-sync-source-bucket-1
aws s3api create-bucket --bucket my-data-sync-dest-bucket-2
```
## Upload Object
```sh
echo "new file with content" > hello.txt

aws s3api put-object --bucket my-data-sync-source-bucket-1 --key transfer-data/
aws s3api put-object --bucket my-data-sync-dest-bucket-2 --key transfered-data/
aws s3api put-object --bucket my-data-sync-source-bucket-1 --key transfer-data/hello.txt --body hello.txt

rm hello.txt
```

## Create DataSync task
Go to console to grab the bucket's arns and if it the command doesn't work just use the console to create the task and start the execution
```sh
aws datasync create-task --source-location-arn arn:aws:s3:::my-data-sync-source-bucket-1 --destination-location-arn arn:aws:s3:::my-data-sync-dest-bucket-2 --name sync-buckets

aws datasync start-task-execution --task-arn arn:aws:datasync:::
```

### I made a mistake and this is the command to move the object
```sh
aws s3api copy-object --bucket my-data-sync-source-bucket-1 --copy-source my-data-sync-source-bucket-1/hello.txt --key transfer-data/hello.txt
```