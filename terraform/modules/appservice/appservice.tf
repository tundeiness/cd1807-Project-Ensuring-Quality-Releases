resource "random_id" "unique" {
  byte_length = 4
}

resource "azurerm_service_plan" "test" {
  name                = "${var.application_type}-${var.resource_type}-plan-${random_id.unique.hex}"
  location            = "East US 2"  # Use same location variable
  resource_group_name = var.resource_group
  os_type             = "Windows" # "Linux"
  sku_name            = "F1"
}

resource "azurerm_linux_web_app" "test" {
  name                = "${var.application_type}-${var.resource_type}-app-${random_id.unique.hex}"
  location            = "East US 2"  # same location as Service Plan
  resource_group_name = var.resource_group
  service_plan_id     = azurerm_service_plan.test.id

  app_settings = {
    "WEBSITE_RUN_FROM_PACKAGE" = 0
  }
  
  site_config {
    always_on = false  # for Y1/Consumption plan
  }
}