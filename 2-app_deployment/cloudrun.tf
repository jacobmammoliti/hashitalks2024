module "cloud_run" {
  source = "github.com/GoogleCloudPlatform/cloud-foundation-fabric.git//modules/cloud-run?ref=v28.0.0"

  project_id = var.project_id
  name       = "encryptah"
  region     = var.region

  containers = {
    encryptah = {
      image = "jacobmammoliti/encryptah:latest"
      env = {
        VAULT_NAMESPACE = var.environment_variables["vault_namespace"]
        VAULT_ADDR      = var.environment_variables["vault_addr"]
        VAULT_ROLE_ID   = var.environment_variables["vault_role_id"]
        VAULT_SECRET_ID = var.vault_secret_id
        PSQL_HOST       = var.environment_variables["psql_addr"]
        FLASK_HOST      = var.environment_variables["flask_addr"]
      }
      ports = {
        main = {
          container_port = 5000
        }
      }
    }
  }
  service_account_create = true

  ingress_settings = "all"
}