#!/usr/bin/env python3
"""
Selenium UI Test Suite for SauceDemo
Comprehensive test that adds all products to cart and removes them
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import datetime


class SauceDemoTest:
    """Test suite for SauceDemo website"""
    
    def __init__(self):
        """Initialize the test suite"""
        print("=" * 80)
        print("SELENIUM UI TEST SUITE - SAUCEDEMO")
        print("=" * 80)
        print(f"Test Start Time: {datetime.datetime.now()}")
        print("=" * 80)
        
        # Configure Chrome options
        options = ChromeOptions()
        # Uncomment these lines when running in Azure DevOps
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        
        print("Initializing Chrome WebDriver...")
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
        print("✓ WebDriver initialized successfully")
        
        self.base_url = "https://www.saucedemo.com/"
        self.username = "standard_user"
        self.password = "secret_sauce"
        
    def login(self):
        """Test user login functionality"""
        print("\n" + "-" * 80)
        print("TEST 1: User Login")
        print("-" * 80)
        
        try:
            print(f"Navigating to {self.base_url}")
            self.driver.get(self.base_url)
            print("✓ Page loaded successfully")
            
            print(f"Attempting to log in as user: {self.username}")
            
            # Find and fill username field
            username_field = self.driver.find_element(By.ID, "user-name")
            username_field.send_keys(self.username)
            print("✓ Username entered")
            
            # Find and fill password field
            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys(self.password)
            print("✓ Password entered")
            
            # Click login button
            login_button = self.driver.find_element(By.ID, "login-button")
            login_button.click()
            print("✓ Login button clicked")
            
            # Wait for inventory page to load
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
            print(f"✓ Login successful for user: {self.username}")
            print("✓ Redirected to inventory page")
            
            return True
            
        except Exception as e:
            print(f"✗ Login failed: {str(e)}")
            return False
    
    def add_all_products_to_cart(self):
        """Add all products to the shopping cart"""
        print("\n" + "-" * 80)
        print("TEST 2: Add All Products to Cart")
        print("-" * 80)
        
        try:
            # Find all inventory items
            inventory_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
            product_count = len(inventory_items)
            
            print(f"Found {product_count} products on the page")
            
            # Get product names and add to cart
            added_products = []
            
            for i, item in enumerate(inventory_items, 1):
                # Get product name
                product_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
                
                # Find and click the "Add to cart" button for this item
                add_button = item.find_element(By.CSS_SELECTOR, "button.btn_inventory")
                add_button.click()
                
                added_products.append(product_name)
                print(f"✓ Added to cart [{i}/{product_count}]: {product_name}")
                time.sleep(0.3)  # Small delay for stability
            
            # Verify cart badge count
            cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            cart_count = int(cart_badge.text)
            
            print(f"\n✓ All products added to cart successfully")
            print(f"✓ Cart contains {cart_count} items")
            
            # Assertion to verify cart count matches product count
            assert cart_count == product_count, f"Cart count mismatch: Expected {product_count}, Got {cart_count}"
            print(f"✓ ASSERTION PASSED: Cart count matches product count ({cart_count}/{product_count})")
            
            return True
                
        except AssertionError as e:
            print(f"✗ ASSERTION FAILED: {str(e)}")
            return False
        except Exception as e:
            print(f"✗ Failed to add products to cart: {str(e)}")
            return False
    
    def view_cart(self):
        """Navigate to shopping cart"""
        print("\n" + "-" * 80)
        print("TEST 3: View Shopping Cart")
        print("-" * 80)
        
        try:
            # Click shopping cart icon
            cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
            cart_icon.click()
            print("✓ Clicked shopping cart icon")
            
            # Wait for cart page to load
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_list")))
            print("✓ Shopping cart page loaded")
            
            # Get cart items
            cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
            print(f"✓ Cart contains {len(cart_items)} items")
            
            # List all items in cart
            print("\nItems in cart:")
            for i, item in enumerate(cart_items, 1):
                item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
                print(f"  [{i}] {item_name}")
            
            return True
            
        except Exception as e:
            print(f"✗ Failed to view cart: {str(e)}")
            return False
    
    def remove_all_products_from_cart(self):
        """Remove all products from the shopping cart"""
        print("\n" + "-" * 80)
        print("TEST 4: Remove All Products from Cart")
        print("-" * 80)
        
        try:
            # Get initial count
            cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
            initial_count = len(cart_items)
            
            print(f"Starting with {initial_count} items in cart")
            
            # Get product names before removal
            product_names = []
            for item in cart_items:
                product_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
                product_names.append(product_name)
            
            # Remove each item
            for i, product_name in enumerate(product_names, 1):
                # Re-find remove buttons to avoid stale element
                remove_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button.cart_button")
                
                if remove_buttons:
                    remove_buttons[0].click()  # Always click the first remove button
                    print(f"✓ Removed from cart [{i}/{initial_count}]: {product_name}")
                    time.sleep(0.3)  # Small delay for stability
            
            # Verify cart is empty
            time.sleep(1)
            cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
            
            if len(cart_items) == 0:
                print(f"\n✓ All products removed from cart successfully")
                print(f"✓ Cart is now empty")
                print("✓ ASSERTION PASSED: Cart is empty")
                return True
            else:
                print(f"✗ ASSERTION FAILED: Cart still contains {len(cart_items)} items")
                return False
                
        except Exception as e:
            print(f"✗ Failed to remove products from cart: {str(e)}")
            return False
    
    def logout(self):
        """Logout from the application"""
        print("\n" + "-" * 80)
        print("TEST 5: User Logout")
        print("-" * 80)
        
        try:
            # Navigate back to inventory if on cart page
            try:
                continue_shopping = self.driver.find_element(By.ID, "continue-shopping")
                continue_shopping.click()
                print("✓ Navigated back to inventory page")
                time.sleep(1)
            except:
                pass  # Already on inventory page
            
            # Open hamburger menu
            menu_button = self.driver.find_element(By.ID, "react-burger-menu-btn")
            menu_button.click()
            print("✓ Opened navigation menu")
            time.sleep(1)
            
            # Click logout link
            logout_link = self.wait.until(
                EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
            )
            logout_link.click()
            print("✓ Clicked logout link")
            
            # Verify we're back on login page
            self.wait.until(EC.presence_of_element_located((By.ID, "login-button")))
            print(f"✓ Logout successful for user: {self.username}")
            print("✓ Redirected to login page")
            
            return True
            
        except Exception as e:
            print(f"✗ Logout failed: {str(e)}")
            return False
    
    def run_all_tests(self):
        """Execute all test cases"""
        results = {
            "login": False,
            "add_products": False,
            "view_cart": False,
            "remove_products": False,
            "logout": False
        }
        
        try:
            # Run tests in sequence
            results["login"] = self.login()
            
            if results["login"]:
                results["add_products"] = self.add_all_products_to_cart()
                results["view_cart"] = self.view_cart()
                results["remove_products"] = self.remove_all_products_from_cart()
                results["logout"] = self.logout()
            
        except Exception as e:
            print(f"\n✗ Test suite encountered an error: {str(e)}")
        
        finally:
            self.print_summary(results)
            self.cleanup()
    
    def print_summary(self, results):
        """Print test execution summary"""
        print("\n" + "=" * 80)
        print("TEST EXECUTION SUMMARY")
        print("=" * 80)
        
        total_tests = len(results)
        passed_tests = sum(1 for result in results.values() if result)
        failed_tests = total_tests - passed_tests
        
        print(f"Total Tests: {total_tests}")
        print(f"Passed: {passed_tests}")
        print(f"Failed: {failed_tests}")
        print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        print("-" * 80)
        
        for test_name, result in results.items():
            status = "PASS" if result else "FAIL"
            symbol = "✓" if result else "✗"
            print(f"{symbol} {test_name.replace('_', ' ').title()}: {status}")
        
        print("=" * 80)
        print(f"Test End Time: {datetime.datetime.now()}")
        print("=" * 80)
    
    def cleanup(self):
        """Clean up resources"""
        print("\nClosing browser...")
        if self.driver:
            self.driver.quit()
            print("✓ Browser closed successfully")


def main():
    """Main entry point"""
    test_suite = SauceDemoTest()
    test_suite.run_all_tests()


if __name__ == "__main__":
    main()
