## Create website 1
## Create a bucket
```sh
aws s3api create-bucket --bucket cors-demo-bucket42
```
## Change block public access
```sh
aws s3api put-public-access-block \
--bucket cors-demo-bucket42 \
--public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=false,RestrictPublicBuckets=false"
```
## Create a bucket policy
```sh
aws s3api put-bucket-policy --bucket cors-demo-bucket42 --policy file://policy.json
```
## Turn on static website hosting
```sh
aws s3api put-bucket-website --bucket cors-demo-bucket42 --website-configuration file://website.json
```
## Upload our index.html file and include a resource that would be cross-origin
```sh
aws s3api put-object --bucket cors-demo-bucket42 --key index.html --body index.html
```
## View website
https://cors-demo-bucket42.s3.amazonaws.com/index.html

## Create website 2
## Create a bucket
```sh
aws s3api create-bucket --bucket cors-demo-bucket43
```
## Change block public access
```sh
aws s3api put-public-access-block \
--bucket cors-demo-bucket43 \
--public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=false,RestrictPublicBuckets=false"
```
## Create a bucket policy
```sh
aws s3api put-bucket-policy --bucket cors-demo-bucket43 --policy file://policy2.json
```
## Upload our hello.js file and include a resource that would be cross-origin
```sh
aws s3api put-object --bucket cors-demo-bucket43 --key hello.js --body hello.js
```
## At this point the cors shouldn't work
## Create API Gateway with mock response and then test the endpoint
```sh
curl -X POST -H "Content-Type: application/json" https://hoqksv3pfa.execute-api.us-east-1.amazonaws.com/test/hello
```
## Apply a CORS policy on the first bucket
```sh
aws s3api put-bucket-cors --bucket cors-demo-bucket42 --cors-configuration file://cors.json
```
## Go back to website to make sure cors works
## Clean up
```sh
aws apigatewayv2 delete-api --api-id hoqksv3pfa

aws s3 rm s3://cors-demo-bucket42 --recursive
aws s3 rm s3://cors-demo-bucket43 --recursive

aws s3api delete-bucket --bucket cors-demo-bucket42
aws s3api delete-bucket --bucket cors-demo-bucket43
```