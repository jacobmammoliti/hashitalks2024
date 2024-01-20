module "docker_artifact_registry" {
  source = "github.com/GoogleCloudPlatform/cloud-foundation-fabric.git//modules/artifact-registry?ref=v28.0.0"

  project_id = var.gcp_project_id
  location   = var.gcp_artifact_registry_region
  name       = format("%s-registry", var.demo_purpose)
  format = {
    docker = {}
  }
}