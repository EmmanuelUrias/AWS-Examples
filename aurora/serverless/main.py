import boto3
import os

rds = boto3.client('rds')
cfn = boto3.client('cloudformation')
ec2 = boto3.client('ec2')

def create_aurora_db():
    def create_db_subnet_group():
        try:
            response = rds.create_db_subnet_group(
                DBSubnetGroupName='my-db-subnet-group',
                DBSubnetGroupDescription='My DB subnet group',
                SubnetIds=[
                    'subnet-xxxxxxxx',  # Replace with your subnet IDs
                    'subnet-yyyyyyyy'
                ]
            )
            print(f'Successfully created DB subnet group: {response}')
        except Exception as e:
            print(f'Error creating DB subnet group: {e}')

    create_db_subnet_group()

    try:
        response = rds.create_db_cluster(
            DBClusterIdentifier='my-aurora-serverless-cluster',
            Engine='aurora-mysql',  # Use 'aurora-postgresql' for PostgreSQL
            EngineMode='serverless',
            MasterUsername='admin',
            MasterUserPassword='yourpassword',
            BackupRetentionPeriod=7,
            DBSubnetGroupName='my-db-subnet-group',  # Replace with your DB subnet group
            VpcSecurityGroupIds=[
                'sg-xxxxxxxx'  # Replace with your security group ID
            ],
            ScalingConfiguration={
                'AutoPause': True,
                'MinCapacity': 0.5,
                'MaxCapacity': 3,
                'SecondsUntilAutoPause': 300  # 5 minutes
            }
        )
        print(f'Successfully created Aurora Serverless cluster: {response}')
    except Exception as e:
        print(f'Error creating Aurora Serverless cluster: {e}')

    with open('template.yaml', 'r') as template_file:
        template_body = template_file.read()

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

    create_ec2_instance = cfn.create_stack(
        StackName='my-aurora-stack',
        TemplateBody=template_body,
        Parameters=[
            {
                'ParameterKey': 'KeyPair',
                'ParameterValue': key_pair
            }
        ]
    )

    print(create_ec2_instance)