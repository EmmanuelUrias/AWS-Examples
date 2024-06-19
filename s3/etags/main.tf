terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.54.1"
    }
  }
}

provider "aws" {
  # Configuration options
}

resource "aws_s3_bucket" "S3Bucket" {
  bucket = "my-tf-test-bucket445"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}

resource "aws_s3_object" "object" {
  bucket = aws_s3_bucket.S3Bucket.id
  key    = "mytestfile.txt"
  source = "mytestfile.txt"

# Without this etag terraform would have no way of detecting changes within the file, if you run terraform plan you'll see that there no changes but if you go into the file and change it a bit and run the command again terraform will detect the changes in the etag
  etag = filemd5("mytestfile.txt")
}