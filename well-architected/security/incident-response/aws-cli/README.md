## Query AWS CloudTrail
### List all of the CloudWatch Logs
```sh
aws logs describe-log-groups --region us-east-1
```

### CloudTrail logs for IAM access denied attempts
```sh
aws logs filter-log-events --region us-east-1 --start-time 1722031992221 --log-group-name CloudTrail/my-logs --filter-pattern AccessDenied --output json --query 'events[*].message'| jq -r '.[] | fromjson | .userIdentity, .sourceIPAddress, .responseElements'
```

### Users IAM access key
This can be useful in order to select a particular user using the access key.
```sh
aws logs filter-log-events --region us-east-1 --start-time 1551402000000 --log-group-name CloudTrail/DefaultLogGroup --filter-pattern AKIAIOSFODNN7EXAMPLE --output json --query 'events[*].message'| jq -r '.[] | fromjson | .userIdentity, .sourceIPAddress, .responseElements'
```

### Source IP Address
This is useful if a specific IP address is taking malicious actions
```sh
aws logs filter-log-events --region us-east-1 --start-time 1551402000000 --log-group-name CloudTrail/DefaultLogGroup --filter-pattern 192.0.2.1 --output json --query 'events[*].message'| jq -r '.[] | fromjson | .userIdentity, .sourceIPAddress, .responseElements'
```

## Block Access in AWS IAM
### Retrieve Users, Roles, and Groups
```sh
aws iam list-users

aws iam list-roles

aws iam list-groups
```
### To only display the name do this
```sh
aws iam list-users --output table --query 'Users[*].UserName'
```

### Attach inline deny policy
```sh
aws iam put-user-policy --user-name USERNAME --policy-name DenyAll --policy-document '{ "Statement": [ { "Effect": "Deny", "Action": "*", "Resource": "*" } ] }'

aws iam put-role-policy --role-name ROLENAME --policy-name DenyAll --policy-document '{ "Statement": [ { "Effect": "Deny", "Action": "*", "Resource": "*" } ] }'
```

### To delete inline policy and restore access
```sh
aws iam delete-user-policy --user-name USERNAME --policy-name DenyAll

aws iam delete-role-policy --role-name ROLENAME --policy-name DenyAll
```