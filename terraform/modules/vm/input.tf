variable "admin_username" {
  type = string
}

variable "ssh_public_key" {
  type = string
  sensitive = true
}

variable "location" {
  type = string
}

variable "resource_group" {
  type = string
}

variable "application_type" {
  type = string
}

variable "resource_type" {
  type = string
}

variable "subnet_id" {
  type = string
}

variable "public_ip_address_id" {
  type = string
}

# variable "admin_username" {
#   type    = string
#   default = "azureuser"
# }

variable "vm_size" {
  type    = string
  default = "Standard_DS2_v2"
}

variable "vm_name" {
  type = string
}

variable "network_security_group_id" {
  type = string
}