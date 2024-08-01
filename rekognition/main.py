import boto3
import json

reko = boto3.client('rekognition')
s3 = boto3.client('s3')

bucket_name = 'rekognition-bucket-443'
image_path = './PaulWalkerEdit-1.jpg'
bucket_policy = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowRekognitionServiceReadAccess",
      "Effect": "Allow",
      "Principal": {
        "Service": "rekognition.amazonaws.com"
      },
      "Action": [
        "s3:GetObject",
        "s3:GetObjectAcl",
        "s3:ListBucket"
      ],
      "Resource": [
        f"arn:aws:s3:::{bucket_name}",
        f"arn:aws:s3:::{bucket_name}/*"
      ]
    }
  ]
}

def create_bucket(bucket):
    resp = s3.create_bucket(
        Bucket=bucket,
    )

    print(resp)

def put_bucket_policy(bucket, policy):
    policy_json = json.dumps(policy)
    s3.put_bucket_policy(
        Bucket=bucket,
        Policy=policy_json
    )
    print('Bucket policy applied.')

def upload_image_to_bucket(bucket, image_path):
    image_name = image_path.split('/')[-1]
    with open(image_path, 'rb') as image_file:
        resp = s3.put_object(
            Bucket=bucket,
            Key=image_name,
            Body=image_file
        )
    s3_image_uri = f"s3://{bucket}/{image_name}"
    print(resp)
    return s3_image_uri

def detect_faces(image_uri):
    bucket = image_uri.split('/')[2]
    key = '/'.join(image_uri.split('/')[3:])
    resp = reko.detect_faces(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': key
            }
        },
        Attributes=['ALL']
    )
    print(resp)

if __name__ == "__main__":
#    create_bucket(bucket_name)
#    put_bucket_policy(bucket_name, bucket_policy)
    upload_image_to_bucket(bucket_name, image_path)

    s3_image_uri = upload_image_to_bucket(bucket_name, image_path)
    detect_faces(s3_image_uri)