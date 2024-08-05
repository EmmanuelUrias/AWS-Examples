import boto3
import os

client = boto3.client('rds')
cfn = boto3.client('cloudformation')
ec2 = boto3.client('ec2')

def create_aurora_db():
    create_cluster = client.create_db_cluster(
        DBClusterIdentifier='my-aurora-cluster',
        Engine='aurora-postgresql'
    )

    print(create_cluster)

    create_instance = client.create_db_instance(
        DBInstanceIdentifier='my-aurora-instance',
        DBInstanceClass='t3.micro',
        Engine='aurora-postgresql',
        DBClusterIdentfier='my-aurora-cluster'
    )

    print(create_instance)

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