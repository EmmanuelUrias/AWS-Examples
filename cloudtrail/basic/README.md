# Create bucket for Trail
```sh
aws s3api create-bucket --bucket trail-bucket-443
```

# Create and attach new bucket policy
```sh
aws s3api put-bucket-policy --bucket trail-bucket-443 --policy file://policy.json
```

# Create Trail
```sh
aws cloudtrail create-trail --name my-trail --s3-bucket-name trail-bucket-443
```

# Start logging for Trail
```sh
aws cloudtrail start-logging --name my-trail
```

# Create DynamoDB table and add items to create logs
```sh
aws dynamodb create-table \
--table-name users \
--attribute-definitions AttributeName=User,AttributeType=S \
--key-schema AttributeName=User,KeyType=HASH \
--billing-mode PAY_PER_REQUEST
```

```sh
aws dynamodb put-item \
--table-name users \
--item '{"User": {"S": "Emmanuel"}}'
```