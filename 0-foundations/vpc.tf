module "vpc" {
  source = "github.com/GoogleCloudPlatform/cloud-foundation-fabric.git//modules/net-vpc?ref=v28.0.0"

  project_id = var.gcp_project_id
  name       = format("%s-vpc", var.demo_purpose)
  psa_config = {
    ranges = { psa-range = "10.1.0.0/20" } # 10.1.0.0 - 10.1.15.254
    routes = null
  }
}