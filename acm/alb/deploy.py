import boto3
import json

alb = boto3.client('elbv2')
ec2 = boto3.client('ec2')
iam = boto3.client('iam')
elbv2 = boto3.client('elbv2')
acm = boto3.client('acm')
route53 = boto3.client('route53')

def get_vpc_id():
    # Describe VPCs and find the default one
    vpcs = ec2.describe_vpcs(Filters=[{'Name': 'isDefault', 'Values': ['true']}])
    if not vpcs['Vpcs']:
        print("No default VPC found.")
        return None
    
    vpc_id = vpcs['Vpcs'][0]['VpcId']
    return vpc_id

def get_subnet_id(return_index=1):
    vpc_id = get_vpc_id()
    
    # Describe subnets within the VPC and specific AZs
    subnets = ec2.describe_subnets(
        Filters=[
            {'Name': 'vpc-id', 'Values': [vpc_id]},
            {'Name': 'availability-zone', 'Values': ['us-east-1a', 'us-east-1b']}
        ]
    )['Subnets']
    
    # Check if there are enough subnets
    if len(subnets) < return_index:
        print(f"Not enough subnets found. Found {len(subnets)} subnets.")
        return None
    
    # Return the subnet ID based on return_amount
    if return_index == 1:
        return subnets[0]['SubnetId']
    elif return_index == 2 and len(subnets) > 1:
        return subnets[1]['SubnetId']
    else:
        print("Invalid return_amount value or not enough subnets.")
        return None

def get_default_sg_group_id():
    resp = ec2.describe_security_groups(
        Filters=[{'Name': 'group-name', 'Values': ['default']}]
    )

    if resp['SecurityGroups']:
        return resp['SecurityGroups'][0]['GroupId']
    else:
        print("No default security group found.")
        return None
    

def request_certificate(domain_name, validation_method='DNS'):
    wildcard_domain_name = f"*.{domain_name}"
    
    response = acm.request_certificate(
        DomainName=domain_name,
        ValidationMethod=validation_method,
        SubjectAlternativeNames=[
            wildcard_domain_name
        ]
    )
    
    certificate_arn = response['CertificateArn']
    print(f"Certificate requested successfully. ARN: {certificate_arn}")
    return certificate_arn

def create_instances():
    def create_instance_profile():
        role_name = 'EC2-SSM'
        instance_profile_name = 'SSM-EC2-Profile'

        try:
            # Create the IAM role
            iam.create_role(
                RoleName=role_name,
                AssumeRolePolicyDocument=json.dumps({
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": "ec2.amazonaws.com"
                            },
                            "Action": "sts:AssumeRole"
                        }
                    ]
                })
            )
            print(f"Created IAM role: {role_name}")
        except iam.exceptions.EntityAlreadyExistsException:
            print(f"IAM role {role_name} already exists.")
        
        # Attach the SSM policy to the role
        iam.attach_role_policy(
            RoleName=role_name,
            PolicyArn='arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore'
        )
        
        try:
            # Create the instance profile
            iam.create_instance_profile(
                InstanceProfileName=instance_profile_name
            )
            print(f"Created instance profile: {instance_profile_name}")
        except iam.exceptions.EntityAlreadyExistsException:
            print(f"Instance profile {instance_profile_name} already exists.")

        # Add role to instance profile
        try:
            iam.add_role_to_instance_profile(
                InstanceProfileName=instance_profile_name,
                RoleName=role_name
            )
            print(f"Added role {role_name} to instance profile {instance_profile_name}")
        except iam.exceptions.LimitExceededException:
            print(f"Role {role_name} is already attached to {instance_profile_name}")

        return instance_profile_name

    instance_profile_name = create_instance_profile()
    security_group_id = get_default_sg_group_id()
    subnet_id = get_subnet_id()

    if not (instance_profile_name and security_group_id and subnet_id):
        print("Failed to get necessary components for instance creation.")
        return None

    # Create EC2 instances
    instances = ec2.run_instances(
        ImageId='ami-0ae8f15ae66fe8cda',
        InstanceType='t3.micro',
        MaxCount=2,
        MinCount=1,
        IamInstanceProfile={'Name': instance_profile_name},
        NetworkInterfaces=[
            {
                'AssociatePublicIpAddress': True,
                'DeleteOnTermination': True,
                'DeviceIndex': 0,
                'Groups': [security_group_id],
                'SubnetId': subnet_id
            }
        ]
    )

    instance_ids = [instance['InstanceId'] for instance in instances['Instances']]
    return instance_ids


# alb_info = create_instances() => Already deployed
alb_info = ['i-0092ceda95d52c9a8', 'i-0e76a2040fb05eaa5']

def create_alb(alb_info=alb_info):
    instance_ids = alb_info
    security_group_id = get_default_sg_group_id()

    subnet_1 = get_subnet_id(1)
    subnet_2 = get_subnet_id(2)

    # Example usage with ALB creation
    if instance_ids and security_group_id:
        print(f"Using Instance ID: {instance_ids[0]} and Security Group ID: {security_group_id} for ALB creation.")
        
        # Create ALB here using the instance_ids and sg_id
        # alb = elbv2.create_load_balancer(
        #     Name='my-load-balancer',
        #     Subnets=[subnet_1, subnet_2],
        #     SecurityGroups=[security_group_id],
        #     Scheme='internet-facing',
        #     Type='application',
        #     IpAddressType='ipv4'
        # )
        
        #alb_arn = alb['LoadBalancers'][0]['LoadBalancerArn']
        alb_arn = 'arn:aws:elasticloadbalancing:us-east-1:099001967703:loadbalancer/app/my-load-balancer/6ddd11a20a01eb19'
        vpc_id = get_vpc_id()

        # target_group = elbv2.create_target_group(
        #     Name='load-balancer-target-group',
        #     Protocol='HTTP',
        #     Port=80,
        #     HealthCheckEnabled=True,
        #     HealthCheckPath="/",
        #     HealthCheckIntervalSeconds=10,
        #     HealthCheckTimeoutSeconds=5,
        #     HealthyThresholdCount=2,
        #     UnhealthyThresholdCount=2,
        #     VpcId=vpc_id,
        #     TargetType='instance'
        # )

        # target_group_arn = target_group['TargetGroups'][0]['TargetGroupArn']
        target_group_arn = 'arn:aws:elasticloadbalancing:us-east-1:099001967703:targetgroup/load-balancer-target-group/e4513fb7b8d1832b'

        # # Register targets
        # elbv2.register_targets(
        #     TargetGroupArn=target_group_arn,
        #     Targets=[{'Id': instance_id, 'Port': 80} for instance_id in instance_ids]
        # )

        domain_name = 'quiet-time-assistant.com'  # Replace with your domain name
        # certificate_arn = request_certificate(domain_name)
        certificate_arn = 'arn:aws:acm:us-east-1:099001967703:certificate/1cc2b2d9-f025-4b88-9798-c74ed5e400f0'

        elbv2.create_listener(
            LoadBalancerArn=alb_arn,
            Protocol='HTTPS',
            Port=443,
            DefaultActions=[
                {
                    "Type": 'forward',
                    "TargetGroupArn": target_group_arn
                }
            ],
            Certificates=[
                {
                    'CertificateArn': certificate_arn
                }
            ]
        )

    def create_route53_record(domain_name=domain_name, alb_dns_name=alb['LoadBalancers'][0]['DNSName'], alb_hosted_zone_id=alb['LoadBalancers'][0]['CanonicalHostedZoneId']):
        hosted_zone_id = route53.list_hosted_zones()['HostedZones'][0]['Id']
        response = route53.change_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            ChangeBatch={
                'Comment': 'Create alias record for ALB',
                'Changes': [
                    {
                        'Action': 'CREATE',
                        'ResourceRecordSet': {
                            'Name': domain_name,
                            'Type': 'A',
                            'AliasTarget': {
                                'HostedZoneId': alb_hosted_zone_id,
                                'DNSName': alb_dns_name,
                                'EvaluateTargetHealth': False
                            }
                        }
                    }
                ]
            }
        )
        print(f"Route 53 record created: {response}")

    create_route53_record()

create_alb()
# Make sure everything is working and then write a function that tears is all down
# Work on type checking since a lot of values are passed into functions there can be confusion on whether a value is suppose to be a string, number, or array