output "role_id" {
  description = "Role ID for Encryptah's AppRole."
  value       = vault_approle_auth_backend_role.encryptah.role_id
}

output "secret_id" {
  description = "Secret ID for Encryptah's AppRole."
  value       = vault_approle_auth_backend_role_secret_id.id.secret_id
  sensitive   = true
}
