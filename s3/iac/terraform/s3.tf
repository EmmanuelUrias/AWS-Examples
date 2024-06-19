 resource "aws_s3_bucket" "S3Bucket" {
  bucket = "my-tf-test-bucket223"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}