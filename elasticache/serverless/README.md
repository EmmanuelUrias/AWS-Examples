# Create Serverless Cache
```sh
aws elasticache create-serverless-cache --serverless-cache-name my-redis-cache --engine redis
```

## Install Redis
Do this on your own its a simple brew commands

## Make ec2 to connect to redis cache
```sh
aws cloudformation deploy \
--template-file template.yml \
--stack-name redis-ec2 \
--capabilities CAPABILITY_NAMED_IAM
```