variable "environment_variables" {
  type = map(string)
  default = {
    vault_namespace = "admin"
    vault_addr      = "http://127.0.0.1:8200"
    vault_role_id   = "0000-0000-0000-0000"
    psql_addr       = "127.0.0.1"
    flask_addr      = "127.0.0.1"
  }
  description = "(Optional) Map of environment variables to assign to Cloud Run."
}

variable "project_id" {
  type        = string
  description = "(Required) The ID of the GCP project in which the resources will be created."
}

variable "region" {
  type        = string
  description = "(Optional) The region to deploy the Cloud Run instance."
  default     = "us-east1"
}

variable "vault_secret_id" {
  type        = string
  description = "(Required) The Vault secret ID to use for authentication."
}
