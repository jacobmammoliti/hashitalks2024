output "vault_public_endpoint_url" {
  description = "The public endpoint URL for HCP Vault."
  value       = hcp_vault_cluster.main.vault_public_endpoint_url
}
