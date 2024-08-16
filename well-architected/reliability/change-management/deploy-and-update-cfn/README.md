## Deploy and Update using CFN stack
## Deploy simple stack
```sh
aws cloudformation deploy \
--stack-name CloudFormationLab \
--template-file ./simple_stack.yaml \
--capabilities CAPABILITY_NAMED_IAM
```
## Update the stack to deploy the subnet, route table, and IGW
```sh
aws cloudformation update-stack \
--stack-name CloudFormationLab \
--template-body file://simple_stack.yaml \
--parameters '[{"ParameterKey": "PublicEnabledParam", "ParameterValue": "true"}, {"ParameterKey": "EC2SecurityEnabledParam", "ParameterValue": "true"}]'
```
## Create Stacks for StackSet permissions
```sh
aws cloudformation deploy \
--stack-name StackSetAdministratorRole \
--template-file ./AWSCloudFormationStackSetAdministrationRole.yml \
--capabilities CAPABILITY_NAMED_IAM

aws cloudformation deploy \
--stack-name StackSetExecutionRole \
--template-file ./AWSCloudFormationStackSetExecutionRole.yml \
--capabilities CAPABILITY_NAMED_IAM \
--parameter-overrides '[{"ParameterKey": "AdministratorAccountId", "ParameterValue": "099001967703"}]'
```
## Create a StackSet
```sh
aws cloudformation create-stack-set \
--stack-set-name StackSetsLab \
--template-body file://simple_stack.yaml \
--parameters '[{"ParameterKey": "PublicEnabledParam", "ParameterValue": "true"}, {"ParameterKey": "EC2SecurityEnabledParam", "ParameterValue": "true"}]' \
--capabilities CAPABILITY_NAMED_IAM
```
## Create StackSet instances
```sh
aws cloudformation create-stack-instances \
--stack-set-name StackSetsLab \
--accounts 099001967703 \
--regions us-east-1 us-east-2 us-west-1 us-west-2 \
--operation-preferences FailureToleranceCount=2
```

## Clean Up
```sh
aws cloudformation delete-stack-instances \
--stack-set-name StackSetsLab \
--accounts 099001967703 \
--regions us-east-2 us-west-1 us-west-2 \
--no-retain-stacks

aws cloudformation delete-stack-set \
--stack-set-name StackSetsLab
```