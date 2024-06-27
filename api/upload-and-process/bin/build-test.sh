## Make sure your in the /test directory
aws s3api create-bucket --bucket test-py-code-223

aws s3api put-object --bucket test-py-code-223 --key sample-file.txt --body sample-file.txt