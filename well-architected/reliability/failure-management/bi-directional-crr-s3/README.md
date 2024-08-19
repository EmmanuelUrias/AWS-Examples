## Deploy S3 stack
```sh
aws cloudformation deploy \
--stack-name s3-stack \
--template-file ./s3_bucket.yaml \
--capabilities CAPABILITY_NAMED_IAM
```