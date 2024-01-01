import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:5000/')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def wait_for_result_element(self):
        return self.wait_for_element(By.NAME, 'result', timeout=10)

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def test_addition_operation(self):
        var_1_input = self.driver.find_element(By.NAME, 'var_1')
        var_2_input = self.driver.find_element(By.NAME, 'var_2')
        operation_select = Select(self.driver.find_element(By.NAME, 'operation'))

        var_1_input.send_keys('5')
        var_2_input.send_keys('3')

        # Select 'Addition' from the dropdown
        operation_select.select_by_visible_text('Addition')

        # Explicit wait for the submit button to be clickable
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.btn-success'))
        )

        submit_button.click()

        # Explicit wait for the result element
        result_entry = self.wait_for_result_element()

        # Extract the result text
        result_text = result_entry.get_attribute('placeholder')
        print(f"Result: {result_text}")

        # Assert the result
        expected_result = '8'
        self.assertEqual(result_text, expected_result, f"Expected result: {expected_result}, Actual result: {result_text}")

        # Quit the driver
        self.driver.quit()
    
    def test_subtraction_operation(self):
        var_1_input = self.driver.find_element(By.NAME, 'var_1')
        var_2_input = self.driver.find_element(By.NAME, 'var_2')
        operation_select = Select(self.driver.find_element(By.NAME, 'operation'))

        var_1_input.send_keys('5')
        var_2_input.send_keys('3')

        # Select 'Addition' from the dropdown
        operation_select.select_by_visible_text('Subtraction')

        # Explicit wait for the submit button to be clickable
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.btn-success'))
        )

        submit_button.click()

        # Explicit wait for the result element
        result_entry = self.wait_for_result_element()

        # Extract the result text
        result_text = result_entry.get_attribute('placeholder')
        print(f"Result: {result_text}")

        # Assert the result
        expected_result = '2'
        self.assertEqual(result_text, expected_result, f"Expected result: {expected_result}, Actual result: {result_text}")

        # Quit the driver
        self.driver.quit()

    def test_multiplication_operation(self):
        var_1_input = self.driver.find_element(By.NAME, 'var_1')
        var_2_input = self.driver.find_element(By.NAME, 'var_2')
        operation_select = Select(self.driver.find_element(By.NAME, 'operation'))

        var_1_input.send_keys('5')
        var_2_input.send_keys('3')

        # Select 'Addition' from the dropdown
        operation_select.select_by_visible_text('Multiplication')

        # Explicit wait for the submit button to be clickable
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.btn-success'))
        )

        submit_button.click()

        # Explicit wait for the result element
        result_entry = self.wait_for_result_element()

        # Extract the result text
        result_text = result_entry.get_attribute('placeholder')
        print(f"Result: {result_text}")

        # Assert the result
        expected_result = '15'
        self.assertEqual(result_text, expected_result, f"Expected result: {expected_result}, Actual result: {result_text}")

        # Quit the driver
        self.driver.quit()

    def test_division_operation(self):
        var_1_input = self.driver.find_element(By.NAME, 'var_1')
        var_2_input = self.driver.find_element(By.NAME, 'var_2')
        operation_select = Select(self.driver.find_element(By.NAME, 'operation'))

        var_1_input.send_keys('16')
        var_2_input.send_keys('2')

        # Select 'Addition' from the dropdown
        operation_select.select_by_visible_text('Division')

        # Explicit wait for the submit button to be clickable
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.btn-success'))
        )

        submit_button.click()

        # Explicit wait for the result element
        result_entry = self.wait_for_result_element()

        # Extract the result text
        result_text = result_entry.get_attribute('placeholder')
        print(f"Result: {result_text}")

        # Assert the result
        expected_result = 8.0
        self.assertEqual(result_text, expected_result, f"Expected result: {expected_result}, Actual result: {result_text}")

        # Quit the driver
        self.driver.quit()
    
    
if __name__ == '__main__':
    unittest.main()
