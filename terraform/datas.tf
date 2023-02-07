data "aws_secretsmanager_secret" "by-arn" {
  arn = "arn:aws:secretsmanager:${var.region}:${var.account_id}:secret:db-credentials-group-5-hUSdCB"
}

data "aws_secretsmanager_secret_version" "current" {
  secret_id = data.aws_secretsmanager_secret.by-arn.id
}
