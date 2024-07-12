# Register Job
```sh
aws batch register-job-definition \
--job-definition-name square-job \
--type container \
--container-properties '{"image": "my-docker-image"}'
```

# Submit Job
```sh
aws batch submit-job \
--job-name my-job \
--job-definition square-job \
--job-queue my-job-queue
```