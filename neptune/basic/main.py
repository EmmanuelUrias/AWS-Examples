import boto3
import json
import base64

neptune = boto3.client('neptune')
iam = boto3.client('iam')
sagemaker = boto3.client('sagemaker')


def create_neptune_instance():
    cluster_name = 'my-neptune-cluster'

    neptune.create_db_cluster(
        DBClusterIdentifier=cluster_name,
        Engine='neptune'
    )

    resp = neptune.create_db_instance(
        DBInstanceIdentifier='my-db-instance',
        DBInstanceClass='db.t4g.medium',
        Engine='neptune',
        DBClusterIdentifier=cluster_name
    )

    print(resp)

def create_notebook():
    role_policy_doc = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "sagemaker.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }

    role_resp = iam.create_role(
        RoleName='SageMakerNeptuneRole',
        AssumeRolePolicyDocument=json.dumps(role_policy_doc)
    )

    iam.attach_role_policy(
        RoleName='SageMakerNeptuneRole',
        PolicyArn='arn:aws:iam::aws:policy/AmazonSageMakerFullAccess'
    )

    print('Iam role created and policy is attached')

    notebook_instance_name = 'neptune-db-notebook'
    role_arn = role_resp['Role']['Arn']

    notebook_resp = sagemaker.create_notebook_instance(
        NotebookInstanceName=notebook_instance_name,
        InstanceType='ml.t3.medium',
        RoleArn=role_arn,
    )
    print(notebook_resp)

    def encode_to_base64(script):
        encoded_bytes = base64.b64encode(script.encode('utf-8'))
        return encoded_bytes.decode('utf-8')

    # Sample scripts to run on notebook creation and start
    on_create_script = """
    #!/bin/bash
    echo "Running on create script"
    """
    on_start_script = """
    #!/bin/bash
    echo "Running on start script"
    """

    # Encode scripts to base64
    encoded_on_create = encode_to_base64(on_create_script)
    encoded_on_start = encode_to_base64(on_start_script)

    lifecycle_config = {
        "OnCreate": [
            {
                "Content": encoded_on_create
            }
        ],
        "OnStart": [
            {
                "Content": encoded_on_start
            }
        ]
    }

    sagemaker.create_notebook_instance_lifecycle_config(
        NotebookInstanceLifecycleConfigName='MyLifecycleConfig',
        OnCreate=lifecycle_config['OnCreate'],
        OnStart=lifecycle_config['OnStart']
    )

    update_resp = sagemaker.update_notebook_instance(
        NotebookInstanceName=notebook_instance_name,
        LifecycleConfigName='MyLifecycleConfig'
    )

    print(update_resp)


create_neptune_instance()

create_notebook()
