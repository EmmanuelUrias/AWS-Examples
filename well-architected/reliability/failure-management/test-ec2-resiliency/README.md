## Deploy VPC infra
```sh
aws s3 mb s3://template-bucket-443
aws s3 cp ./vpc-alb-app-db.yaml s3://template-bucket-443/vpc-alb-app-db.yaml

aws cloudformation deploy \
--stack-name WebApp1-VPC \
--template-file ./vpc-alb-app-db.yaml \
--s3-bucket template-bucket-443 \
--capabilities CAPABILITY_NAMED_IAM
```

## Deploy the EC2 and Static webapp infra
```sh
aws s3 cp ./staticwebapp.yaml s3://template-bucket-443/staticwebapp.yaml

aws cloudformation deploy \
--stack-name WebApp1-Static \
--template-file ./staticwebapp.yaml \
--s3-bucket template-bucket-443 \
--capabilities CAPABILITY_NAMED_IAM
```