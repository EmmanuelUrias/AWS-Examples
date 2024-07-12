# Build Image ps make sure your in batch dir
```sh
docker build -t app .
```

# Register Job
```sh
aws batch register-job-definition \
--job-definition-name square-job \
--type container \
--container-properties '{"image": "099001967703.dkr.ecr.us-east-1.amazonaws.com/square:latest","vcpus": 1,"memory": 128}'
```

# Create Compute Env
```sh
aws batch create-compute-environment --compute-environment-name my-compute-env \
--type MANAGED \
--compute-resources minvCpus=0,desiredvCpus=1,maxvCpus=1,instanceTypes=m4.16xlarge,subnets=subnet-0ad725ee29938aa51,securityGroupIds=sg-0938fea805aa7dddd
--service-role arn:aws:iam::099001967703:role/service-role/AWSServiceRoleForBatch
```

# Create Job Queue
```sh
aws batch create-job-queue \
--job-queue-name my-job-queue \
--state ENABLED \
--priority 1 \
--compute-environment-order '[{"order": 1,"computeEnvironment": "arn:aws:batch:us-east-1:099001967703:compute-environment/my-compute-env"}]'
```

# Submit Job
```sh
aws batch submit-job \
--job-name my-job \
--job-definition square-job \
--job-queue my-job-queue
```