resource "aws_db_instance" "this" {
  allocated_storage               = var.allocated_storage
  identifier                      = "rds-instance-group-5"
  db_name                         = "postgres"
  engine                          = "postgres"
  engine_version                  = var.engine_version
  instance_class                  = var.instance_type
  username                        = local.username
  password                        = local.password
  vpc_security_group_ids          = ["sg-04382520bd7fb72a6"]
  db_subnet_group_name            = aws_db_subnet_group.this.name
  skip_final_snapshot             = var.skip_final_snapshot
  publicly_accessible             = var.publicly_accessible
  deletion_protection             = var.deletion_protection
  enabled_cloudwatch_logs_exports = ["postgresql", "upgrade"]
  snapshot_identifier             = var.snapshot_identifier


  timeouts {
    create = var.timeouts.create
    update = var.timeouts.update
    delete = var.timeouts.delete
  }

  lifecycle {
    ignore_changes = [
      password,
      snapshot_identifier,
    ]
  }
}

resource "aws_db_subnet_group" "this" {
  name       = "subnet-group-5"
  subnet_ids = ["subnet-0443d448351d08f51", "subnet-060ac7b9ac7888077", "subnet-04927be24fcd4f20e"]
}

resource "postgresql_database" "my_db" {
  name              = "metadata"
  allow_connections = true
}
