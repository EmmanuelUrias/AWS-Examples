## Deploy the EFS Stack
```sh
aws cloudformation deploy --stack-name MyEFSStack \
--template-file template.yaml \
--parameter-overrides VpcId=vpc-00bb0ebfd33ff4f24 SubnetId1=subnet-0ad725ee29938aa51 SubnetId2=subnet-025373b89d975735c SecurityGroupId=sg-0938fea805aa7dddd \
--capabilities CAPABILITY_NAMED_IAM
```

## Deploy the Test EFS stack
```sh
aws cloudformation deploy --stack-name MyEFSTestStack \
--template-file test.yaml \
--parameter-overrides VpcId=vpc-00bb0ebfd33ff4f24 SubnetId=subnet-0ad725ee29938aa51 SecurityGroupId=sg-0938fea805aa7dddd EfsFileSystemId=fs-079331ab7e99d2a08 \
--capabilities CAPABILITY_NAMED_IAM
```