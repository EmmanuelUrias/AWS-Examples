## Deploy infra
```sh
aws ec2 create-key-pair --key-name MyKeyPair

aws cloudformation deploy \
--stack-name perf-lab \
--template-file ./time_test.yaml \
--parameter-overrides KeyName=MyKeyPair Ec2InstanceSubnetId=subnet-0ad725ee29938aa51 \
--capabilities CAPABILITY_NAMED_IAM
```