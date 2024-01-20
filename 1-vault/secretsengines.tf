resource "vault_database_secrets_mount" "database" {
  path = "database"

  postgresql {
    name              = "postgresql_cloudsql"
    username          = var.postgresql_settings["username"]
    password          = var.postgresql_password
    connection_url    = format("postgresql://{{username}}:{{password}}@%s:5432/%s", var.postgresql_settings["hostname"], var.postgresql_settings["database"])
    verify_connection = var.postgresql_settings["verify_connection"]

    allowed_roles = [
      "encryptah",
    ]
  }
}

resource "vault_database_secret_backend_role" "encryptah" {
  name    = "encryptah"
  backend = vault_database_secrets_mount.database.path
  db_name = vault_database_secrets_mount.database.postgresql[0].name

  creation_statements = [
    "CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}';",
    "GRANT SELECT ON ALL TABLES IN SCHEMA public TO \"{{name}}\";",
  ]
}

resource "vault_mount" "transit" {
  path                      = "transit"
  type                      = "transit"
  default_lease_ttl_seconds = 3600
  max_lease_ttl_seconds     = 86400
}

resource "vault_transit_secret_backend_key" "aes256_key" {
  backend          = vault_mount.transit.path
  type             = "aes256-gcm96"
  name             = "aes256-gcm96-key"
  deletion_allowed = true
}

resource "vault_transit_secret_backend_key" "aes256_convergent_key" {
  backend               = vault_mount.transit.path
  type                  = "aes256-gcm96"
  name                  = "aes256-gcm96-convergent-key"
  convergent_encryption = true
  derived               = true
  deletion_allowed      = true
}