import boto3

client = boto3.client('cloudformation')

def create_stack():
    resp = client.create_stack(
        StackName='my-rds-stack',
        TemplateBody='./template.yaml',
        Parameters=[
            {
                '': ''
            }
        ]
    )

    print(resp)

create_stack()