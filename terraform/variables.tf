variable "env" {
  description = "Environment"
  type        = string
}

variable "aws_region" {
  description = "AWS Region"
  type        = string
  default     = "eu-central-1"
}

variable "is_temporary" {
  description = "Set to true if this resource created temporary and should be removed after var.delete_after"
  type        = bool
  default     = false
}

variable "tags" {
  description = "Default tag for AWS provider"
  type        = map(string)
  default = {
    "Project"   = "final-project/group-5"
    "Team"      = "group 5"
    "Terraform" = "true"
    "Owner"     = "group 5"
  }
}

variable "backup_retention_period" {
  type        = number
  description = "Backup retention period in days. Must be > 0 to enable backups"
  default     = 0
}

variable "timeouts" {
  type = object({
    create = string
    update = string
    delete = string
  })
  description = "A list of DB timeouts to apply to the running code while creating, updating, or deleting the DB instance."
  default = {
    create = "40m"
    update = "80m"
    delete = "60m"
  }
}

variable "allocated_storage" {
  default     = 20
  type        = number
  description = "Storage allocated to database instance"
}

variable "engine_version" {
  default     = "13.9"
  type        = string
  description = "Database engine version"
}

variable "instance_type" {
  default     = "db.t3.micro"
  type        = string
  description = "Instance type for database instance"
}

variable "skip_final_snapshot" {
  default     = true
  type        = bool
  description = "Flag to enable or disable a snapshot if the database instance is terminated"
}

variable "deletion_protection" {
  default     = false
  type        = bool
  description = "Flag to protect the database instance from deletion"
}

variable "publicly_accessible" {
  default     = true
  type        = bool
  description = "Flag to enable public access to the database"
}

variable "snapshot_identifier" {
  type        = string
  description = "The snapshot ID used to restore the DB instance"
  default     = null
}

variable "region" {
  type   = string
  description = "Selected AWS account region"
}

variable "account_id" {
  type   = string
  description = "AWS account id"
}
