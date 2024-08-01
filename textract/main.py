import boto3
import json

client = boto3.client('textract')
s3client = boto3.client('s3')

policy = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowTextractServiceFullAccess",
      "Effect": "Allow",
      "Principal": {
        "Service": "textract.amazonaws.com"
      },
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::textract-bucket-443",
        "arn:aws:s3:::textract-bucket-443/*"
      ]
    }
  ]
}

class Textract:
    def __init__(self, name):
        self.name = name

    def create_bucket(self):
        response = s3client.create_bucket(
            Bucket='textract-bucket-443'
        )

        resp = s3client.put_object(
            Bucket='textract-bucket-443',
            Key='Form.PNG',
            Body='./sign_pdf_15.png'
        )

        policy_json = json.dumps(policy)
        s3client.put_bucket_policy(
            Bucket='textract-bucket-443',
            Policy=policy_json
        )

        print(response, resp)

    def analyze_document_in_s3(self):
        response = client.analyze_document(
            Document={
                'S3Object': {
                    'Bucket': 'textract-bucket-443',
                    'Name': 'Form.PNG'
                }
            },
            FeatureTypes=[
                'FORMS'
            ]
        )

        print(response)

    def delete_bucket(self):
        bye_objects = s3client.delete_objects(
            Bucket='textract-bucket-443',
            Delete={
                'Objects':[
                    {
                        'Key': 'Form.PNG'
                    }
                ]
            }
        )

        print(bye_objects)

        response = s3client.delete_bucket(
            Bucket='textract-bucket-443'
        )

        print(response)

if __name__ == '__main__':
    demo = Textract('demo')
    #demo.create_bucket()
    demo.analyze_document_in_s3()
    #demo.delete_bucket()