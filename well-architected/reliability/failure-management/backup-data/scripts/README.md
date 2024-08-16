### Create Primary prefix list
```sh
export AWS_PROFILE=PRIMARY
aws ec2 create-managed-prefix-list \
--prefix-list-name MyPrefixList \
--entries Cidr=0.0.0.0/0,Description=CorpNetworkPrimary \
--max-entries 10 \
--address-family IPv4 
```
### Create a Backup prefix list
```sh
export AWS_PROFILE=BACKUP
aws ec2 create-managed-prefix-list \
--prefix-list-name MyPrefixList \
--entries Cidr=0.0.0.0/0,Description=CorpNetworkBackup \
--max-entries 10 \
--address-family IPv4
```