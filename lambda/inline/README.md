### To build run
```sh
sam build
```

### To Deploy run
```sh
sam deploy --stack-name my-stack --capabilities CAPABILITY_IAM
```

### To tear down
```sh
sam delete --stack-name inline-lambda-function-stack
```