variable "postgresql_password" {
  type        = string
  description = "(Required) Password for initial PostgreSQL login."
}

variable "postgresql_settings" {
  type = object({
    username          = optional(string, "postgres")
    hostname          = optional(string, "127.0.0.1")
    database          = optional(string, "postgres")
    verify_connection = optional(bool, true)
  })
  description = "(Optional) Settings for PostgreSQL."
}
