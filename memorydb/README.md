# Create MemoryDB Cluster
```sh
aws memorydb create-cluster \
--cluster-name my-db-cluster \
--node-type db.t4g.small \
--acl-name open-access
```

# Create an EC2 instance to connect to the Cluster
```sh
aws cloudformation deploy \
--template-file template.yml \
--stack-name redis-ec2 \
--capabilities CAPABILITY_NAMED_IAM
```

# Run this command to connect to the cluster from EC2
```sh
redis-cli -h clustercfg.my-db-cluster.cnnqz1.memorydb.us-east-1.amazonaws.com --tls
```