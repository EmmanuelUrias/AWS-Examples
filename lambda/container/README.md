## To build
```sh
sam build \
--template-file "./template.yaml" \
--base-dir "./function"
```
## To deploy
```sh
# Register Container
aws ecr create-repository \
--repository-name function-container \
--image-tag-mutability IMMUTABLE

# deploy
sam deploy \
--template-file "./.aws-sam/build/template.yaml" \
--stack-name "container-lambda" \
--capabilities "CAPABILITY_IAM" \
--image-repository 099001967703.dkr.ecr.us-east-1.amazonaws.com/function-container
```

### Tear down
```sh
sam delete --stack-name container-lambda

aws ecr delete-repository \
--repository-name function-container
```
