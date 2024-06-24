## Create a bucket
```sh
aws s3api create-bucket --bucket encryption-practice1
```
## Create a file and upload it
```sh
echo "hello world" > hello.txt
aws s3api put-object --bucket encryption-practice1 --key hello.txt --body hello.txt
```
## Put object with encryption of KMS
```sh
aws s3api put-object --bucket encryption-practice1 \
--key hello.txt \
--body hello.txt \
--server-side-encryption aws:kms \
--ssekms-key-id 7b80990d-890c-43fa-b7ce-19a11b713cca
```
## Download Object
```sh
aws s3 cp s3://encryption-practice1/hello.txt hello.txt
```

## Put object with SSE-C
```sh
openssl rand -out ssec.key 32

aws s3 cp hello.txt s3://encryption-practice1/hello.txt \
--sse-c AES256 \
--sse-c-key fileb://ssec.key
```
## Download object
```sh
aws s3 cp s3://encryption-practice1/hello.txt hello.txt \
--sse-c AES256 \
--sse-c-key fileb://ssec.key
```

## Clean up
```sh
aws s3 rm s3://encryption-practice1 --recursive
aws s3 rb s3://encryption-practice1
aws kms disable-key --key 7b80990d-890c-43fa-b7ce-19a11b713cca
aws kms schedule-key-deletion --key 7b80990d-890c-43fa-b7ce-19a11b713cca --pending-window-in-days 7
```