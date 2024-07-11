# Using DMS
First you run the cloudformation stacks to create the 2 db instances then you connect to the instances to upload the table and data.
After that you create the DMS instance to then create the DMS task that will transfer the data.
After you create the task you run it and pray that is works
At this point the data should be replicated in both db instances

## Install MySQL and PSQL Client
```sh
sudo apt-get install -y postgresql-client 
sudo apt-get install -y mysql-client 
```
### Assemble PSQL Connection String
postgresql://postgres:password@:3306/mydatabase

### Assemble MySQL Connection String
mysql://admin:password@:5432/mydatabase
mysql -u admin -ppassword -h database-2.ck6c4llggxsy.us-east-1.rds.amazonaws.com -P 5432 database psql postgresql://postgres:password@rds-dms-postgres-rdsinstance-ghj0ttbqkmaf.cv1x0r3utzcm.ca-central-1.rds.amazonaws.com:3306/mydatabase