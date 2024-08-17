## Deploy the asg
```sh
aws cloudformation deploy \
--template-file template.yaml \
--capabilities CAPABILITY_NAMED_IAM \
--stack-name asg-stack
```