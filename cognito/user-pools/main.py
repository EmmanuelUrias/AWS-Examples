import boto3

## Unable to confirm the user using an email verification
cognito = boto3.client('cognito-idp')

def create_user_pool():
    resp = cognito.create_user_pool(
        PoolName='My-User-Pool',
        Policies={
            'PasswordPolicy': {
                'MinimumLength': 8,
                'RequireUppercase': True
            }
        },
        AutoVerifiedAttributes=['email'],
        VerificationMessageTemplate={
            'DefaultEmailOption': 'CONFIRM_WITH_CODE'
        }
    )

    user_pool_id = resp['UserPool']['Id']

    domain = cognito.create_user_pool_domain(
        Domain='my-cool-userpool',
        UserPoolId=user_pool_id
    )

    user_pool_domain = input('Please enter User Pool domain: \n')

    client = cognito.create_user_pool_client(
        UserPoolId=user_pool_id,
        ClientName='my-client',
        CallbackURLs=[f'{user_pool_domain}/callback'],
        LogoutURLs=[f'{user_pool_domain}/logout'],
        AllowedOAuthFlows=['code', 'implicit'],  # Enable code and implicit grant types
        AllowedOAuthScopes=['openid', 'email', 'profile'],  # Configure OAuth 2.0 scopes
        SupportedIdentityProviders=['COGNITO'],  # Enable Cognito as an identity provider
        AllowedOAuthFlowsUserPoolClient=True  # Enable OAuth 2.0 flow for the client
    )

    print(client)

create_user_pool()