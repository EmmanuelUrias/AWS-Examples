## Create an s3 bucket
```
aws s3 mb s3://metadata-demo-bucket223
```

## Create new file
```sh
echo "Important legal document" > court-case.txt
```

## Upload file with metadata
```sh
aws s3api put-object --bucket metadata-demo-bucket223 --key court-case.txt --body court-case.txt --metadata reviewed-by="Emmanuel Urias",date-reviewed="05/14/2024"
```

## Get metadara through head object
```sh
aws s3api head-object --bucket metadata-demo-bucket223 --key court-case.txt
```