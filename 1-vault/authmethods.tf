resource "vault_auth_backend" "approle" {
  type = "approle"
}

resource "vault_approle_auth_backend_role" "encryptah" {
  backend        = vault_auth_backend.approle.path
  role_name      = "encryptah"
  token_policies = ["default", "encryptah"]
  role_id        = uuid()
}

resource "vault_approle_auth_backend_role_secret_id" "id" {
  backend   = vault_auth_backend.approle.path
  role_name = vault_approle_auth_backend_role.encryptah.role_name
}