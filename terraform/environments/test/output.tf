output "vm_name" {
  value = module.vm.vm_name
}

output "vm_private_ip" {
  value = module.vm.private_ip_address
}

output "vm_public_ip" {
  description = "The public IP address of the VM"
  # value       = azurerm_public_ip.public_ip.ip_address
  # value = module.vm.public_ip_address_id
  value = module.publicip.public_ip_address
}