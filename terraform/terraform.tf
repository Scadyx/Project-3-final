terraform {
  required_version = "~> 1.1, >= 1.1.2"

  backend "s3" {}

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.53.0"
    }
  }
}
