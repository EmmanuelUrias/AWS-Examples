import boto3
import os
import json
import time

client = boto3.client('cloudformation')
secret = boto3.client('secretsmanager')
ec2 = boto3.client('ec2')
iam = boto3.client('iam')

def create_stack():
    make_secret = secret.create_secret(
        Name='my-rds-secret'
    )
    rds_secret = make_secret['ARN']

     # Read the template file content
    with open('template.yaml', 'r') as template_file:
        template_body = template_file.read()

    resp = client.create_stack(
        StackName='my-rds-stack',
        TemplateBody=template_body,
        Parameters=[
            {
                'ParameterKey': 'VpcId',
                'ParameterValue': 'vpc-00bb0ebfd33ff4f24'
            },
            {
                'ParameterKey': 'WebServerSGGroupId',
                'ParameterValue': 'sg-0938fea805aa7dddd'
            },
            {
                'ParameterKey': 'RdsSecretArn',
                'ParameterValue': 'arn:aws:secretsmanager:us-east-1:099001967703:secret:my-rds-secret-y1Lxpa'
            },
            {
                'ParameterKey': 'Username',
                'ParameterValue': 'emmanuel'
            },
            {
                'ParameterKey': 'Subnets',
                'ParameterValue': "subnet-025373b89d975735c,subnet-0ad725ee29938aa51"
            }
        ]
    )

    print(resp)

create_stack()

def create_instance():
    def create_key_pair(key_name, save_to_file=True):
        try:
            # Create a key pair
            response = ec2.create_key_pair(KeyName=key_name)

            # Get the key material
            private_key = response['KeyMaterial']

            # Optionally save the private key to a file
            if save_to_file:
                file_name = f"{key_name}.pem"
                with open(file_name, 'w') as file:
                    file.write(private_key)
                os.chmod(file_name, 0o400)  # Set permissions to read-only for the owner
                print(f"Key pair created and saved to {file_name}")
                return key_name
            else:
                print("Key pair created. Private key material:")
                print(private_key)

        except Exception as e:
            print(f"Error creating key pair: {e}")

    key_pair = create_key_pair('my-ec2-keypair')

    trust_policy = {
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
    }

    iam.create_role(
        RoleName='EC2SSMRole',
        AssumeRolePolicyDocument=json.dumps(trust_policy)
    )
    iam.attach_role_policy(
        RoleName='EC2SSMRole',
        PolicyArn='arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore'
    )
    instance_profile = iam.create_instance_profile(
        InstanceProfileName='MyInstanceProfile443'
    )
    iam.add_role_to_instance_profile(
        InstanceProfileName='MyInstanceProfile443',
        RoleName='EC2SSMRole'
    )

    time.sleep(10)

    instance = ec2.run_instances(
        ImageId='ami-0ba9883b710b05ac6',
        InstanceType='t3a.micro',
        KeyName=key_pair,
        SubnetId='subnet-025373b89d975735c',
        SecurityGroupIds=['sg-0938fea805aa7dddd'],
        IamInstanceProfile={'Arn': f'{instance_profile['InstanceProfile']['Arn']}'},
        MinCount=1,
        MaxCount=1
    )

    print(instance)

create_instance()