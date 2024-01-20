module "project" {
  source = "github.com/GoogleCloudPlatform/cloud-foundation-fabric.git//modules/project?ref=v28.0.0"

  name           = var.gcp_project_id
  project_create = false
  services = [
    "artifactregistry.googleapis.com",
  ]
}