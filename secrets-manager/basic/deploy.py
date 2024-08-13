import boto3

cfn = boto3.client('cloudformation')

def deploy():
    # Read the contents of the CloudFormation template file
    with open('./template.yaml', 'r') as template_file:
        template_body = template_file.read()

    resp = cfn.update_stack(
        StackName='secrets-manager-stack',
        TemplateBody=template_body
    )
    
    print("Stack creation initiated.")
    print(resp)

deploy()