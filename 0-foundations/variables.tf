variable "demo_purpose" {
  type        = string
  description = "(Optional) The purpose of the demo. This will be used as a prefix for the resources."
  default     = "hashitalks2024"
}

variable "gcp_artifact_registry_region" {
  type        = string
  description = "(Optional) The region in which the Artifact Registry will be created."
  default     = "us-east1"
}

variable "gcp_cloudsql_settings" {
  type = object({
    region           = optional(string, "us-east1")
    database_version = optional(string, "POSTGRES_15")
    tier             = optional(string, "db-g1-small")
    ipv4_enabled     = optional(bool, true)
    disk_type        = optional(string, "PD_HDD")
  })
  description = "(Optional) The settings for the Cloud SQL instance."
  default = {
    region           = "us-east1"
    database_version = "POSTGRES_15"
    tier             = "db-g1-small"
    ipv4_enabled     = true
    disk_type        = "PD_HDD"
  }
}

variable "gcp_project_id" {
  type        = string
  description = "(Required) The ID of the GCP project in which the resources will be created."
}

variable "hcp_hvn_settings" {
  type = object({
    region     = optional(string, "us-east-1")
    cidr_block = optional(string, "172.25.16.0/20")
  })
  description = "(Optional) The settings for the AWS network in HCP."
  default = {
    region     = "us-east-1"
    cidr_block = "172.25.16.0/20"
  }
}

variable "hcp_project" {
  type        = string
  description = "(Required) The ID of the HCP project in which the resources will be created."
}
