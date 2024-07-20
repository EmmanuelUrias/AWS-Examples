## To build
```sh
sam build \
--template-file "./template.yaml"
```
## To deploy
```sh
aws s3api create-bucket --bucket-name zip-local-lambda-deployment-bucket

### Zip file and upload
zip function.zip ./function/function.py

aws s3api put-object --bucket zip-local-lambda-deployment-bucket --key function.zip --body function.zip

# deploy
sam deploy \
--template-file "./.aws-sam/build/template.yaml" \
--stack-name "zip-local-lambda" \
--capabilities "CAPABILITY_IAM" \
--s3-bucket zip-local-lambda-deployment-bucket
```

### Tear down
```sh
sam delete --stack-name zip-local-lambda

aws s3api delete-bucket --bucket zip-local-lambda-deployment-bucket
```
