## Deploy the stack
```sh
aws cloudformation create-stack --stack-name MyFargateClusterStack --template-body file://template.yaml --capabilities CAPABILITY_NAMED_IAM
```