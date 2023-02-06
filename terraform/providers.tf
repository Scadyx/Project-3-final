provider "aws" {
  region  = var.aws_region
  profile = "group5"

  default_tags {
    tags = merge(var.tags, {
      Env       = var.env
      Temporary = var.is_temporary
    })
  }
}
