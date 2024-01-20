## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | 1.7.0 |
| <a name="requirement_google"></a> [google](#requirement\_google) | 5.12.0 |
| <a name="requirement_hcp"></a> [hcp](#requirement\_hcp) | 0.80.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_hcp"></a> [hcp](#provider\_hcp) | 0.80.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_docker_artifact_registry"></a> [docker\_artifact\_registry](#module\_docker\_artifact\_registry) | github.com/GoogleCloudPlatform/cloud-foundation-fabric.git//modules/artifact-registry | v28.0.0 |
| <a name="module_postgresql"></a> [postgresql](#module\_postgresql) | github.com/GoogleCloudPlatform/cloud-foundation-fabric.git//modules/cloudsql-instance | v28.0.0 |
| <a name="module_vpc"></a> [vpc](#module\_vpc) | github.com/GoogleCloudPlatform/cloud-foundation-fabric.git//modules/net-vpc | v28.0.0 |

## Resources

| Name | Type |
|------|------|
| [hcp_hvn.main](https://registry.terraform.io/providers/hashicorp/hcp/0.80.0/docs/resources/hvn) | resource |
| [hcp_vault_cluster.main](https://registry.terraform.io/providers/hashicorp/hcp/0.80.0/docs/resources/vault_cluster) | resource |
| [hcp_project.main](https://registry.terraform.io/providers/hashicorp/hcp/0.80.0/docs/data-sources/project) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_demo_purpose"></a> [demo\_purpose](#input\_demo\_purpose) | (Optional) The purpose of the demo. This will be used as a prefix for the resources. | `string` | `"hashitalks2024"` | no |
| <a name="input_gcp_artifact_registry_region"></a> [gcp\_artifact\_registry\_region](#input\_gcp\_artifact\_registry\_region) | (Optional) The region in which the Artifact Registry will be created. | `string` | `"us-east1"` | no |
| <a name="input_gcp_cloudsql_settings"></a> [gcp\_cloudsql\_settings](#input\_gcp\_cloudsql\_settings) | (Optional) The settings for the Cloud SQL instance. | <pre>object({<br>    region           = optional(string, "us-east1")<br>    database_version = optional(string, "POSTGRES_15")<br>    tier             = optional(string, "db-g1-small")<br>    ipv4_enabled     = optional(bool, true)<br>    disk_type        = optional(string, "PD_HDD")<br>  })</pre> | <pre>{<br>  "database_version": "POSTGRES_15",<br>  "disk_type": "PD_HDD",<br>  "ipv4_enabled": true,<br>  "region": "us-east1",<br>  "tier": "db-g1-small"<br>}</pre> | no |
| <a name="input_gcp_project_id"></a> [gcp\_project\_id](#input\_gcp\_project\_id) | (Required) The ID of the GCP project in which the resources will be created. | `string` | n/a | yes |
| <a name="input_hcp_hvn_settings"></a> [hcp\_hvn\_settings](#input\_hcp\_hvn\_settings) | (Optional) The settings for the AWS network in HCP. | <pre>object({<br>    region     = optional(string, "us-east-1")<br>    cidr_block = optional(string, "172.25.16.0/20")<br>  })</pre> | <pre>{<br>  "cidr_block": "172.25.16.0/20",<br>  "region": "us-east-1"<br>}</pre> | no |
| <a name="input_hcp_project"></a> [hcp\_project](#input\_hcp\_project) | (Required) The ID of the HCP project in which the resources will be created. | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_vault_public_endpoint_url"></a> [vault\_public\_endpoint\_url](#output\_vault\_public\_endpoint\_url) | The public endpoint URL for HCP Vault. |
