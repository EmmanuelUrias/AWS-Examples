## Create a new bucket
```sh
aws s3api create-bucket --bucket acl-demo-bucket34 --region us-east-1
```

## Turn of Block Public Access for ACLs
```sh
aws s3api put-public-access-block \
--bucket acl-demo-bucket34 \
--public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=true,RestrictPublicBuckets=true"
```

## Change Bucket Ownership
```sh
aws s3api put-bucket-ownership-controls \
--bucket acl-demo-bucket34 \
--ownership-controls="Rules=[{ObjectOwnership=BucketOwnerPreferred}]"
```

## Add acl and give full permissions to other user
```sh
 aws s3api put-bucket-acl --bucket acl-demo-bucket34 --grant-full-control emailaddress=emmanuelurias60@gmail.com
```

## Create a file and upload
```sh
echo "Hello World" > hello.txt

aws s3api put-object \
--bucket acl-demo-bucket34 \
--key hello.txt\
--body hello.txt
```

#### From the other account you should be able to access the S3 bucket and read the file using this
```sh
aws s3 ls s3://acl-demo-bucket34
```