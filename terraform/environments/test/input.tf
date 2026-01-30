
# Resource Group/Location
variable "location" {}
variable "resource_group" {}
variable "application_type" {}

# Network
variable virtual_network_name {}
variable address_prefix_test {}
variable address_space {}

# VM Inputs
variable "vm_name" {
  type = string
}

# Pipeline Variables

variable admin_username {
  type = string
  default = "azureuser"
}

variable ssh_public_key {
  type = string
  default = file("/Users/tunde/Desktop/udrsa/.ssh/id_rsa.pub")
  # default = public_key = var.ssh_public_key
  description = "Path to SSH public key file"
}

