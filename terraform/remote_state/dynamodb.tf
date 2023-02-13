resource "aws_dynamodb_table" "this" {
  name           = "tflock-group-5"
  hash_key       = "LockID"
  billing_mode   = "PROVISIONED"
  stream_enabled = false
  read_capacity  = 5
  write_capacity = 5

  attribute {
    name = "LockID"
    type = "S"
  }

  point_in_time_recovery {
    enabled = false
  }

  server_side_encryption {
    enabled = false
  }
}
