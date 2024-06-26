## Create a user with no permissions

New user with no permission to generate access keys

```sh
aws iam create-user \
--user-name sts-machine-user

aws iam create-access-key \
--user-name sts-machine-user
```

Get the access key and secret access key from the output and paste it into it's respective key after running:

```sh
aws configure
```

## Edit credentials file to change away from default profile
```sh
open ~/.aws/credentials
```

## Test who you are then make sure you don't have access to S3
```sh
aws sts get-caller-identity --profile sts

aws s3 ls --profile sts
```

## Create a Role

Role with access to new resource
```sh
chmod u+x bin/deploy
./bin/deploy
```

## Use new user credientials and assume role
```sh
aws sts assume-role \
--role-arn arn:aws:iam::099001967703:role/my-sts-stack-StsRole-eAtAgzkhItGD \
--role-session-name s3-sts-example \
--profile sts
```

## Add new assume role to credentials
```sh
open ~/.aws/credentials
```

## Check user
```sh
aws sts get-caller-identity --profile assumed
```

## Check permissions 
```sh
aws s3 ls --profile assumed
```

## Clean up
```sh
aws iam delete-user-policy --user-name sts-machine-user --policy-name StsAssumePolicy 
aws iam delete-user --user-name sts-machine-user

aws cloudformation delete-stack --stack-name my-sts-stack
```

