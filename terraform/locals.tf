locals {
  username = jsondecode(data.aws_secretsmanager_secret_version.current.secret_string)["username"]
  password = jsondecode(data.aws_secretsmanager_secret_version.current.secret_string)["password"]
}