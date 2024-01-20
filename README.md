# HashiTalks 2024: Changing the Way Your Applications Interact With Databases

This repository contains all the code used in my HashiTalks 2024 demo.

## Setting Up the Environment

The environment for this demo comprises of two three components provisioned with Terraform:

1. An HCP Vault instance
2. A CloudSQL instance (running in Google Cloud Platform)
3. The demo application

Prerequisites:

- An HCP organization and a service principal with "Contributor" privileges
- A GCP project and "Editor" role

Switch into the foundations directory (0-foundations) to deploy HCP Vault and CloudSQL. Set the environment variables `HCP_CLIENT_ID` and `HCP_CLIENT_SECRET` for Terraform to authenticate to HCP. Use [Google's Cloud SDK](https://cloud.google.com/sdk?hl=en) to authenticate to GCP.

Create a file `terraform.tfvars` and supply the HCP Project ID via the `hcp_project` variable as well as the GCP Project ID via the `gcp_project_id` variable.

> Note: If Terraform fails when trying to create the Artifact Registry, just re-run it. This is because we are also enabling the API in the same run so it sometimes isn't ready in time.

```bash
terraform init

terraform apply
```

Output:

```bash
vault_public_endpoint_url = "https://hashitalks2024-vault-public-vault-6d255f4e.a9de0fe8.z1.hashicorp.cloud:8200"
```

Once deployed, retrieve the public URL and in HCP, generate a new admin token.

Switch into the Vault directory (1-vault) to roll out the Secrets Engines, App Role Auth Method, and policies. Set the environment variables `VAULT_ADDR`, `VAULT_TOKEN`, `VAULT_NAMESPACE`.

Create a file `terraform.tfvars` and supply the PostgreSQL hostname via the `postgresql_settings` variable as well as the initial root login via the `postgresql_password` variable.

```bash
terraform init

terraform apply
```

Output:

```bash
role_id = "41bbf65a-8669-71b2-30da-2da06ff51e13"
secret_id = <sensitive>
```

> Note: When using App Role authentication, the secret ID should be generated as close to usage as possible and should not be created this way via Terraform. I am creating it this way for demo purposes only.

This role ID and secret ID will be used by the application to authenticate to Vault.
