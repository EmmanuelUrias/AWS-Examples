## Create Log Group
```sh
aws logs create-log-group --log-group-name /example/basic/app
```
## Create retention policy
```sh
aws logs put-retention-policy --log-group-name /example/basic/app --retention-in-days 1
```

## Create Log Stream
```sh
aws logs create-log-stream --log-group-name /example/basic/app --log-stream-name $(date +%s)
```