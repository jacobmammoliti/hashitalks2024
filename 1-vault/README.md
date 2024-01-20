## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | 1.7.0 |
| <a name="requirement_vault"></a> [vault](#requirement\_vault) | 3.23.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_vault"></a> [vault](#provider\_vault) | 3.23.0 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [vault_approle_auth_backend_role.encryptah](https://registry.terraform.io/providers/hashicorp/vault/3.23.0/docs/resources/approle_auth_backend_role) | resource |
| [vault_approle_auth_backend_role_secret_id.id](https://registry.terraform.io/providers/hashicorp/vault/3.23.0/docs/resources/approle_auth_backend_role_secret_id) | resource |
| [vault_auth_backend.approle](https://registry.terraform.io/providers/hashicorp/vault/3.23.0/docs/resources/auth_backend) | resource |
| [vault_database_secret_backend_role.encryptah](https://registry.terraform.io/providers/hashicorp/vault/3.23.0/docs/resources/database_secret_backend_role) | resource |
| [vault_database_secrets_mount.database](https://registry.terraform.io/providers/hashicorp/vault/3.23.0/docs/resources/database_secrets_mount) | resource |
| [vault_mount.transit](https://registry.terraform.io/providers/hashicorp/vault/3.23.0/docs/resources/mount) | resource |
| [vault_policy.admin_ns_policies](https://registry.terraform.io/providers/hashicorp/vault/3.23.0/docs/resources/policy) | resource |
| [vault_transit_secret_backend_key.aes256_convergent_key](https://registry.terraform.io/providers/hashicorp/vault/3.23.0/docs/resources/transit_secret_backend_key) | resource |
| [vault_transit_secret_backend_key.aes256_key](https://registry.terraform.io/providers/hashicorp/vault/3.23.0/docs/resources/transit_secret_backend_key) | resource |
| [vault_approle_auth_backend_role_id.encryptah](https://registry.terraform.io/providers/hashicorp/vault/3.23.0/docs/data-sources/approle_auth_backend_role_id) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_postgresql_password"></a> [postgresql\_password](#input\_postgresql\_password) | (Required) Password for initial PostgreSQL login. | `string` | n/a | yes |
| <a name="input_postgresql_settings"></a> [postgresql\_settings](#input\_postgresql\_settings) | (Optional) Settings for PostgreSQL. | <pre>object({<br>    username          = optional(string, "postgres")<br>    hostname          = optional(string, "127.0.0.1")<br>    database          = optional(string, "postgres")<br>    verify_connection = optional(bool, true)<br>  })</pre> | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_role_id"></a> [role\_id](#output\_role\_id) | Role ID for Encryptah's AppRole. |
| <a name="output_secret_id"></a> [secret\_id](#output\_secret\_id) | Secret ID for Encryptah's AppRole. |
