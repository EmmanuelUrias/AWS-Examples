## Create IAM Policy
```sh
aws iam create-policy \
--policy-name practice-policy \
--policy-document file://policy.json
```

## Attach Policy to User
```sh
aws iam create-user \
--user-name Bob

aws iam attach-user-policy \
--policy-arn arn:aws:iam::099001967703:policy/practice-policy \
--user-name Bob
```

## To update Policy
```sh
aws iam create-policy-version \
--policy-arn arn:aws:iam::099001967703:policy/practice-policy \
--policy-document file://policy.json \
--set-as-default
```

## Create bucket
```sh
aws s3api create-bucket --bucket new-practice-bucket-225
```

# Run this and it should work
```sh
aws s3api list-objects --bucket new-practice-bucket-225
```

# Run this and it shouldn't work
```sh
aws s3 ls
```

The reason as to why it doesn't work is because you have permissions to list objects within a bucket. But make sure you run the commands from the correct user.

# Tear down
```sh
aws iam delete-policy-version \
--policy-arn arn:aws:iam::099001967703:policy/practice-policy \
--version-id v1

aws iam delete-policy-version \
--policy-arn arn:aws:iam::099001967703:policy/practice-policy \
--version-id v2
aws iam delete-policy-version \
--policy-arn arn:aws:iam::099001967703:policy/practice-policy \
--version-id v3

aws iam delete-policy-version \
--policy-arn arn:aws:iam::099001967703:policy/practice-policy \
--version-id v4

aws iam detach-user-policy \
--user-name Bob \
--policy-arn arn:aws:iam::099001967703:policy/practice-policy

aws iam delete-policy --policy-arn arn:aws:iam::099001967703:policy/practice-policy

aws iam delete-user --user-name Bob
```