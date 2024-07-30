import boto3

client = boto3.client('personalize-runtime')

campaign_arn = 'arn:aws:personalize:us-east-1:099001967703:campaign/my-campaign'
user_id = '7'
item_id='14'

response = client.get_recommendations(campaignArn=campaign_arn, userId=user_id, itemId=item_id)

for item in response['itemList']:
    print(item)