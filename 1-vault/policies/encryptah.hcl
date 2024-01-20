path "database/creds/encryptah" {
  capabilities = [ "read" ]
}

path "transit/encrypt/aes256-gcm96-key" {
  capabilities = [ "update" ]
}

path "transit/decrypt/aes256-gcm96-key" {
  capabilities = [ "update" ]
}

path "transit_convergent/encrypt/aes256-gcm96-convergent-key" {
  capabilities = [ "update" ]
}

path "transit_convergent/decrypt/aes256-gcm96-convergent-key" {
  capabilities = [ "update" ]
}