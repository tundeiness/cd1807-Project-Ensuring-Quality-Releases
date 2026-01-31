variable "admin_username" {
  description = "Admin username for the VM"
  type = string
}

variable "ssh_public_key" {
  description = "SSH public key for VM authentication"
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


variable "vm_size" {
  type    = string
  default = "Standard_DS1_v2"

}

variable "vm_name" {
  type = string
}

variable "network_security_group_id" {
  type = string
}