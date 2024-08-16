# Implement Health Checks and Managing Dependences to improve Reliability
### Deploy Infrastructure
```sh
aws s3api create-bucket --bucket webapp1-vpc-bucket
aws s3api put-object --bucket webapp1-vpc-bucket --key vpc-alb-app-db.yaml --body ./vpc-alb-app-db.yaml

aws cloudformation deploy \
--stack-name WebApp1-VPC \
--template-file vpc-alb-app-db.yaml \
--s3-bucket webapp1-vpc-bucket \
--capabilities CAPABILITY_NAMED_IAM

aws cloudformation deploy \
--stack-name HealthCheckLab \
--template-file staticwebapp.yaml \
--capabilities CAPABILITY_NAMED_IAM
```