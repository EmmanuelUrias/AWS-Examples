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

# Create Internet Gateway
IGW_ID=$(aws ec2 create-internet-gateway --query InternetGateway.InternetGatewayId --output text)
aws ec2 attach-internet-gateway --vpc-id $VPC_ID --internet-gateway-id $IGW_ID
echo "Internet Gateway ID: $IGW_ID"

# Configure route table to explicity associate subnets
ROUTE_TABLE_ID=$(aws ec2 describe-route-tables \
    --filters "Name=vpc-id,Values=${VPC_ID}" \
    --query 'RouteTables[0].RouteTableId' \
    --output text
)

echo "Route Table ID: $ROUTE_TABLE_ID"

# Add route to Internet Gateway
echo "Adding route to IGW..."
aws ec2 create-route --route-table-id $ROUTE_TABLE_ID --destination-cidr-block 0.0.0.0/0 --gateway-id $IGW_ID

aws ec2 associate-route-table --route-table-id $ROUTE_TABLE_ID --subnet-id $SUBNET_ID
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