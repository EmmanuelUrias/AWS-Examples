BUCKET_NAME = "upload-and-process-bucket223"

aws s3api create-bucket --bucket $BUCKET_NAME

zip lambda_function.zip file_processor.py

aws s3api put-object --bucket-name $BUCKET_NAME --key lambda_function.zip --body lambda_function.zip

aws cloudformation create-stack --stack-name my-stack \
  --template-body file://template.yaml \
  --parameters ParameterKey=BucketName,ParameterValue=$BUCKET_NAME \
               ParameterKey=APIName,ParameterValue=FileUploadAPI
