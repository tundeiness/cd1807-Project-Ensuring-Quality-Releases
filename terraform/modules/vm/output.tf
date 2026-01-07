output "vm_id" {
  value = azurerm_linux_virtual_machine.vm.id
}

output "vm_name" {
  value = azurerm_linux_virtual_machine.vm.name
}

output "private_ip_address" {
  value = azurerm_network_interface.vm_nic.private_ip_address
}

output "public_ip_address_id" {
  value = azurerm_network_interface.vm_nic.ip_configuration[0].public_ip_address_id
}