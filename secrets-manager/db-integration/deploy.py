import boto3

cfn = boto3.client('cloudformation')

def deploy():
    # Read the contents of the CloudFormation template file
    with open('./template.yaml', 'r') as template_file:
        template_body = template_file.read()

    resp = cfn.create_stack(
        StackName='secrets-manager-db-stack',
        TemplateBody=template_body,
        Parameters=[
            {
                'ParameterKey': 'VpcId',
                'ParameterValue': 'vpc-00bb0ebfd33ff4f24'
            },
            {
                'ParameterKey': 'Subnets',
                'ParameterValue': 'subnet-0ad725ee29938aa51, subnet-025373b89d975735c'
            }
        ],
        Capabilities=['CAPABILITY_IAM']
    )
    
    print("Stack creation initiated.")
    print(resp)

deploy()