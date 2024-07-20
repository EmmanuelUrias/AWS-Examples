## To build
```sh
sam build \
--template-file "./template.yaml"
```
## To deploy
```sh
# create bucket
aws s3api create-bucket --bucket zip-packaged-lambda-deployment-bucket

# package file
sam package \
--template-file "./.aws-sam/build/template.yaml" \
--output-template-file ./.aws-sam/build/packaged.yaml \
--s3-bucket zip-packaged-lambda-deployment-bucket \
--s3-prefix "zip-package-python"

# deploy
sam deploy \
--template-file "./.aws-sam/build/packaged.yaml" \
--stack-name "zip-packaged-lambda" \
--capabilities "CAPABILITY_IAM" 
```

### Tear down
```sh
sam delete --stack-name zip-packaged-lambda

aws s3api delete-bucket --bucket zip-packaged-lambda-deployment-bucket
```
