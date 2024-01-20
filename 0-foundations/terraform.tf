terraform {
  required_version = "1.7.0"

  required_providers {
    hcp = {
      source  = "hashicorp/hcp"
      version = "0.80.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "5.12.0"
    }
  }
}