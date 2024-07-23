## Create a Bucket to put an image then trigger an event for step functions
```sh
aws s3api create-bucket --bucket step-functions-bucket223

# enable event bridge communication
aws s3api put-bucket-notification-configuration \
--bucket step-functions-bucket223 \
--notification-configuration file://notification.json
```

## Create a step function
```sh
aws stepfunctions create-state-machine --name step-function-state-machine --definition  --role-arn
```

## Create eventbridge
do this via console

## Upload files
```sh
aws s3 cp picard.jpg s3://step-functions-bucket223/inputs/picard.jpg
```