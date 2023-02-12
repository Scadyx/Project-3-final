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

provider "postgresql" {
  host            = "rds-instance-group-5.c2ncm6mxe8zp.eu-central-1.rds.amazonaws.com"
  port            = 5432
  database        = "postgres"
  username        = "postgres"
  password        = "qwerty123"
  sslmode         = "disable"
  connect_timeout = 15
}
