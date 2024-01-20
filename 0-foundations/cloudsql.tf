module "postgresql" {
  source     = "github.com/GoogleCloudPlatform/cloud-foundation-fabric.git//modules/cloudsql-instance?ref=v28.0.0"
  project_id = var.gcp_project_id

  name             = format("%s-postgresql", var.demo_purpose)
  region           = var.gcp_cloudsql_settings["region"]
  database_version = var.gcp_cloudsql_settings["database_version"]
  tier             = var.gcp_cloudsql_settings["tier"]
  ipv4_enabled     = var.gcp_cloudsql_settings["ipv4_enabled"]
  disk_type        = var.gcp_cloudsql_settings["disk_type"]
  network          = module.vpc.self_link

  authorized_networks = {
    internet = "0.0.0.0/0"
  }

  deletion_protection         = false
  deletion_protection_enabled = false
}