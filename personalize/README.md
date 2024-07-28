# Create Data Set Group
```sh
aws personalize create-dataset-group \
--name my-dataset-group \
--domain ECOMMERCE
```

# Create Schema
```sh
aws personalize create-schema \
--name my-schema \
--domain ECOMMERCE \
--schema file://schema.json

aws personalize delete-schema \
--schema-arn arn:aws:personalize:us-east-1:099001967703:schema/my-schema
```

# Create Data Set
```sh
aws personalize create-dataset \
--name my-dataset \
--schema-arn arn:aws:personalize:us-east-1:099001967703:schema/my-schema \
--dataset-group-arn arn:aws:personalize:us-east-1:099001967703:dataset-group/my-dataset-group \
--dataset-type Interactions
```

# Create Bucket to hold data
```sh
aws s3api create-bucket \
--bucket dataset-bucket-443
```

# Upload data
```sh
aws s3api put-object \
--bucket dataset-bucket-443 \
--key interactions.csv \
--body ./interactions.csv
```