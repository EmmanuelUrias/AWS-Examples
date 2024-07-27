# Create CloudWatch Log Group
```sh
aws logs create-log-group --log-group-name my-logs

aws logs create-log-stream --log-group-name my-logs --log-stream-name my-logs-stream

aws iam create-role \
--role-name cloudwatch-role \
--assume-role-policy-document file://Policy.json

aws iam put-role-policy --role-name cloudwatch-role --policy-name CloudTrailPermissions --policy-document file://permissions-policy.json

```

# Update the Trail from the basic directory for CloudWatch Logs
```sh
aws cloudtrail update-trail \
--name my-trail \
--cloud-watch-logs-log-group-arn arn:aws:logs:us-east-1:099001967703:log-group:my-logs:\* \
--cloud-watch-logs-role-arn arn:aws:iam::099001967703:role/cloudwatch-role
```