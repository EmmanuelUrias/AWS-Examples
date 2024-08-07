### To build run
```sh
sam build
```

### To Deploy run
```sh
sam deploy --stack-name my-dynamo-stack --capabilities CAPABILITY_IAM
```

### Put Object
```sh
aws dynamodb put-item \
--table-name Users \
--item file://users.json
```

### To tear down
```sh
sam delete --stack-name inline-lambda-function-stack
```