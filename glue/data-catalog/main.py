import boto3
import json
import time

s3 = boto3.client('s3')
glue = boto3.client('glue')
iam = boto3.client('iam')


class CrawlData:
    def __init__(self, name, bucket):
        self.name = name
        self.bucket = bucket

    def set_up_data(self):
        try:
            # Create the bucket
            s3.create_bucket(Bucket=self.bucket)

            # Upload the CSV file to the bucket
            s3.put_object(
                Bucket=self.bucket,
                Key='data.csv',
                Body=open('./data/Electric_Vehicle_Population_Data.csv', 'rb')
            )
        except Exception as e:
            print(f"Error in set_up_data: {e}")
            self.delete_bucket()
            raise

    def set_up_glue(self, db, role, assume_policy, policy_name, policy_doc, crawler_name):
        try:
            # Create the Glue database
            glue.create_database(
                DatabaseInput={
                    'Name': db
                }
            )

            # Create the IAM role
            self.create_role(role, assume_policy, policy_name, policy_doc)

            # Create the Glue crawler
            time.sleep(10)
            glue.create_crawler(
                Name=crawler_name,
                Role=role,
                DatabaseName=db,
                Targets={'S3Targets': [{'Path': f's3://{self.bucket}/'}]}
            )
        except Exception as e:
            print(f"Error in set_up_glue: {e}")
            self.delete_glue_resources(db, crawler_name)
            self.delete_role(role)
            raise

    def create_role(self, role, assume_policy, policy_name, policy_doc):
        try:
            iam.create_role(
                RoleName=role,
                AssumeRolePolicyDocument=json.dumps(assume_policy)
            )

            iam.put_role_policy(
                RoleName=role,
                PolicyName=policy_name,
                PolicyDocument=json.dumps(policy_doc)
            )

            # Attach a managed policy for S3 access
            iam.attach_role_policy(
                RoleName=role,
                PolicyArn='arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole'
            )

        except Exception as e:
            print(f"Error in create_role: {e}")
            self.delete_role(role)
            raise

    def delete_bucket(self):
        try:
            # Delete all objects in the bucket
            response = s3.list_objects_v2(Bucket=self.bucket)
            if 'Contents' in response:
                for obj in response['Contents']:
                    s3.delete_object(Bucket=self.bucket, Key=obj['Key'])

            # Delete the bucket
            s3.delete_bucket(Bucket=self.bucket)
            print(f"Bucket {self.bucket} deleted successfully.")
        except Exception as e:
            print(f"Error in delete_bucket: {e}")

    def delete_role(self, role):
        try:
            # Detach policies and delete the role
            iam.detach_role_policy(
                RoleName=role,
                PolicyArn='arn:aws:iam::aws:policy/service-role/AWSGlueServiceRoles'
            )
            iam.delete_role_policy(
                RoleName=role,
                PolicyName='MyS3AccessPolicy'
            )
            iam.delete_role(RoleName=role)
            print(f"Role {role} deleted successfully.")
        except Exception as e:
            print(f"Error in delete_role: {e}")

    def delete_glue_resources(self, db, crawler_name):
        try:
            # Delete the Glue crawler
            glue.delete_crawler(Name=crawler_name)
            # Delete the Glue database
            glue.delete_database(Name=db)
            print(f"Glue resources for {db} and {crawler_name} deleted successfully.")
        except Exception as e:
            print(f"Error in delete_glue_resources: {e}")

if __name__ == '__main__':
    demo = CrawlData('BasicCrawler', 'my-glue-bucket-443')
    try:
        # demo.set_up_data()
        assume_role_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "glue.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
        policy_document = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": "s3:*",
                    "Resource": [
                        f"arn:aws:s3:::my-glue-bucket-443",
                        f"arn:aws:s3:::my-glue-bucket-443/*"
                    ]
                }
            ]
        }
        demo.set_up_glue('my-glue-db', 'MyGlueServiceRole', assume_role_policy, 'MyS3AccessPolicy', policy_document, 'MyCrawler')
    except Exception as e:
        print(f"Error encountered: {e}")