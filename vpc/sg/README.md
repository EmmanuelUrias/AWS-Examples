## Create a VPC w/ subnets
```sh
VPC_ID=$(aws ec2 create-vpc --cidr-block "10.10.0.0/16" \
    --region us-east-1 \
    --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=PracticeVPC}]' \
    --query Vpc.VpcId \
    --output text
)

echo "VPC ID: $VPC_ID"

SUBNET_ID=$(aws ec2 create-subnet --vpc-id $VPC_ID \
    --cidr-block 10.10.0.0/20 \
    --query Subnet.SubnetId \
    --output text
)
echo "Subnet ID: $SUBNET_ID"
```
## Create a SG
```sh
aws cloudformation deploy \
    --template-file "template.yml" \
    --stack-name "my-nacl-stack" \
    --parameter-overrides SubnetID=$SUBNET_ID VpcID=$VPC_ID \
    --capabilities CAPABILITY_IAM
```

##