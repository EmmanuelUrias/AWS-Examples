import boto3

kafka = boto3.client('kafka')

# tried this and CLI doesn't work just use the console

def create_serverless_cluster():
    response = kafka.create_cluster_v2(
        ClusterName='my-serverless-cluster',
        Serverless={
            'VpcConfigs': [
                {
                    'SubnetIds': [
                        'subnet-0ad725ee29938aa51',
                        'subnet-025373b89d975735c',
                    ],
                    'SecurityGroupIds': [
                        'sg-0938fea805aa7dddd',
                    ]
                }
            ]
        }
    )
    print(response)

create_serverless_cluster()
