import boto3
from botocore.exceptions import ClientError


client = boto3.client('comprehend')

class DetectPII:
    def __init__(self):
        self = self

    def detect_pii(self, text):
        try:
            response = client.detect_pii_entities(Text=text, LanguageCode='en')
            print(response)
        except ClientError:
            print(f'You have an error: {ClientError}')

def demo():
    detect_pii = DetectPII()
    with open("detect_sample.txt") as sample_file:
        sample_text = sample_file.read()

    detect_pii.detect_pii(sample_text)

if __name__ =='__main__':
    demo()