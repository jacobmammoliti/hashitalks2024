data "hcp_project" "main" {
  project = var.hcp_project
}

resource "hcp_hvn" "main" {
  hvn_id         = format("%s-network", var.demo_purpose)
  project_id     = data.hcp_project.main.resource_id
  cloud_provider = "aws"
  region         = var.hcp_hvn_settings["region"]
  cidr_block     = var.hcp_hvn_settings["cidr_block"]
}

resource "hcp_vault_cluster" "main" {
  project_id      = data.hcp_project.main.resource_id
  cluster_id      = format("%s-vault", var.demo_purpose)
  hvn_id          = hcp_hvn.main.hvn_id
  tier            = "dev"
  public_endpoint = true
}