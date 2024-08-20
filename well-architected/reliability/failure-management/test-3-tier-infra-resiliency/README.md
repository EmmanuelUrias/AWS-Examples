## Deploy Multi Region
```sh
aws s3 mb s3://template-bucket-443-2 --region us-east-2

aws s3 cp ./lambda_functions_for_deploy_two_regions.yaml s3://template-bucket-443-2/lambda_functions_for_deploy_two_regions.yaml

aws cloudformation deploy \
--stack-name DeployResiliencyWorkshop \
--template-file ./lambda_functions_for_deploy_two_regions.yaml \
--s3-bucket template-bucket-443-2 \
--capabilities CAPABILITY_NAMED_IAM \
--region us-east-2
```