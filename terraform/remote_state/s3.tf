module "s3_bucket" {
  source  = "terraform-aws-modules/s3-bucket/aws"
  version = "3.6.0"

  # S3 Ownership control
  control_object_ownership = true
  object_ownership         = "BucketOwnerPreferred"

  bucket = "tfstate-group-5"

  # S3 Bucket Policies control
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true

  versioning = {
    enabled = false
  }
}
