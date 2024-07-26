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