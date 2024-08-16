## Deploy multi-tier infrastructure using CFN
### Deploy the VPC Template
```sh
aws s3api create-bucket --bucket wa-lab-vpc-bucket
aws s3api put-object --bucket wa-lab-vpc-bucket --key vpc-alb-app-db.yaml --body ./vpc-alb-app-db.yaml


aws cloudformation deploy \
--template-file vpc-alb-app-db.yaml \
--stack-name delete-soon-asap \
--s3-bucket wa-lab-vpc-bucket \
--capabilities CAPABILITY_NAMED_IAM

aws cloudformation deploy \
--template-file ./staticwebapp.yaml \
--stack-name delete-soon-asap-app \
--capabilities CAPABILITY_NAMED_IAM
```