resource "aws_s3_bucket" "example" {
  bucket = "my-tf-test-bucketdrssds2189321364dev"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}