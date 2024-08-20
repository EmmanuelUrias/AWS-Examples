# Monitoring an Amazon Linux EC2 Instance with CloudWatch Dashboards
### Deploy infra
```sh
aws s3 mb s3://template-bucket-223
aws s3 cp ./vpc-alb-app-db.yaml s3://template-bucket-223/vpc-alb-app-db.yaml

aws cloudformation deploy \
--stack-name PerfLab-VPC \
--template-file ./vpc-alb-app-db.yaml \
--s3-bucket template-bucket-223 \
--capabilities CAPABILITY_NAMED_IAM
```
### Deploy the instance
```sh
aws cloudformation deploy \
--stack-name LinuxMachineDeploy \
--template-file ./LinuxMachineDeploy.yaml \
--capabilities CAPABILITY_NAMED_IAM
```