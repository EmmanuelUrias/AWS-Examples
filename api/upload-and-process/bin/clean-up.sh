# Test clean up
# aws s3 rm s3://test-py-code-223/sample-file.txt
# aws s3 rb s3://test-py-code-223

# aws s3 rm s3://file-processor-py-bucket-42/lambda_function.zip
# aws s3 rb s3://file-processor-py-bucket-42

# Deploy clean up
#!/usr/bin/env bash

# Define variables
PROCESSOR_BUCKET_NAME=${PROCESSOR_BUCKET_NAME:-"file-processor-py-bucket-42"}
BUCKET_NAME=${BUCKET_NAME:-"upload-and-process-bucket223"}
STACK_NAME="my-stack"

# Function to empty and delete an S3 bucket
delete_s3_bucket() {
    local bucket_name=$1
    echo "Deleting all objects in bucket: $bucket_name"
    
    # List all objects and delete them
    aws s3api list-object-versions --bucket "$bucket_name" | \
    jq -r '.Versions[] | {Key: .Key, VersionId: .VersionId}' | \
    jq -s '{"Objects": ., "Quiet": true}' | \
    aws s3api delete-objects --bucket "$bucket_name" --delete file://-

    # List all delete markers and delete them
    aws s3api list-object-versions --bucket "$bucket_name" | \
    jq -r '.DeleteMarkers[] | {Key: .Key, VersionId: .VersionId}' | \
    jq -s '{"Objects": ., "Quiet": true}' | \
    aws s3api delete-objects --bucket "$bucket_name" --delete file://-

    # Delete the bucket itself
    aws s3api delete-bucket --bucket "$bucket_name"
}

# Delete the CloudFormation stack
echo "Deleting CloudFormation stack: $STACK_NAME"
aws cloudformation delete-stack --stack-name "$STACK_NAME"

# Wait for the stack to be deleted
echo "Waiting for CloudFormation stack to be deleted..."
aws cloudformation wait stack-delete-complete --stack-name "$STACK_NAME"
echo "CloudFormation stack deleted."

# Delete the S3 buckets
delete_s3_bucket "$PROCESSOR_BUCKET_NAME"
delete_s3_bucket "$BUCKET_NAME"

echo "Tear down completed successfully."
