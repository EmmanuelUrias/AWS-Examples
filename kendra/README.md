# Create role for Index
```sh
aws iam create-role \
--role-name index-role \
--assume-role-policy-document file://index-role-policy.json
```

# Attach Policy to Role above
```sh
aws iam put-role-policy \
--role-name index-role \
--policy-name index-role-permissions-policy \
--policy-document file://index-role-permissions-policy.json
```

# Create an Index
```sh
aws kendra create-index \
--name "index-1" \
--role-arn "arn:aws:iam::099001967703:role/index-role" \
--edition "DEVELOPER_EDITION"
```

# Create bucket for Data Source
```sh
aws s3api create-bucket \
--bucket index-data-source-bucket223
```

# Create data source
```sh
aws kendra create-data-source \
--name index-1-data-source \
--index-id 9580a74b-c94d-45fc-86c9-7b13a305260f \
--role-arn "arn:aws:iam::099001967703:role/index-role" \
--type S3 \
--configuration '{"S3Configuration":{"BucketName": "index-data-source-bucket223"}}'
```

# Add object to S3
```sh
aws s3api put-object \
--bucket index-data-source-bucket223 \
--key object1.pdf \
--body ./split/xaa.pdf
```

# Sync Data
```sh
aws kendra start-data-source-sync-job \
--id a34678b8-ef65-4a49-9e86-05ab72e2f638 \
--index-id 9580a74b-c94d-45fc-86c9-7b13a305260f
```

# Query 
```sh
aws kendra query \
--index-id 9580a74b-c94d-45fc-86c9-7b13a305260f \
--query-text "What characters are in the book Oliver Twist?"
```

The files we provided in the split are unreadable to Kendra so it doesn't work but in theory when you query Kendra it'll give you a list of documents based of the query