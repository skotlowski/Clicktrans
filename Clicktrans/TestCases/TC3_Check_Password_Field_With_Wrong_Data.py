"""
Szymon Kotlowski 2020

Test Case ID - 3

Test environment:
Windows 10 HOME
Google Chrome

Preconditions:
1. Load Google Chrome properly
2. Enter dev-1.clicktrans.pl/register-test/courier webside

Test Steps:
1. Check password field with one character repeated eight times (fail).
2. Check password field with one character (fail).
3. Check password field with one blank space (fail).
4. Check password field with eight blank spaces (fail).
5. Check password field with eight dashes (fail).


Test objective:

After fill all fields with correct data except the password field and push
the registration button, the registration sheet rejected registration (negative test).


Expected result:
The registration sheet rejected registration (negative test).

Implementation: Szymon Kotlowski
Last edited by: Szymon Kotlowski
Last edit date: 16.08.2020
"""

# import region
from selenium import webdriver
from Libraries import selectors
from Libraries.operations import current_test, \
    final_result, fill_fields, clean_up, check_step_fail
from time import sleep
from Libraries.values import negative_tests_password


class TC3_Check_Password_Field_With_Wrong_Data:

    def __init__(self, driver_path, adress):
        self.tc = __class__.__name__
        current_test(self.tc)

        # Preconditions region
        print("Precondition 1 : Load Google Chrome properly")
        self.driver = webdriver.Chrome(driver_path)
        sleep(5)  # wait for chrome load properly

        print("Precondition 2 : Enter dev-1.clicktrans.pl/register-test/courier webside")
        self.driver.get(adress)
        sleep(1)  # wait for website load properly

    def testcase(self):
        result = None
        end_result = None

        # Test Steps region
        print("Test Step 1 : Check password field with one character repeated eight times (fail).")
        fill_fields(self, selectors, negative_tests_password, 0)
        step_result = self.driver.find_element_by_css_selector(selectors.result).text
        result = check_step_fail(step_result, negative_tests_password, 0)

        if result is not None:  # Result is only not None when test had failed once or more
            end_result = result

        clean_up(self, selectors)

        print("Test Step 2 : Check password field with one character (fail).")
        fill_fields(self, selectors, negative_tests_password, 1)
        step_result = self.driver.find_element_by_css_selector(selectors.result).text
        result = check_step_fail(step_result, negative_tests_password, 1)

        if result is not None:  # Result is only not None when test had failed once or more
            end_result = result

        clean_up(self, selectors)

        print("Test Step 3 : Check password field with one blank space (fail).")
        fill_fields(self, selectors, negative_tests_password, 2)
        step_result = self.driver.find_element_by_css_selector(selectors.result).text
        result = check_step_fail(step_result, negative_tests_password, 2)

        if result is not None:  # Result is only not None when test had failed once or more
            end_result = result

        clean_up(self, selectors)

        print("Test Step 4 : Check password field with eight blank spaces (fail).")
        fill_fields(self, selectors, negative_tests_password, 3)
        step_result = self.driver.find_element_by_css_selector(selectors.result).text
        result = check_step_fail(step_result, negative_tests_password, 3)

        if result is not None:  # Result is only not None when test had failed once or more
            end_result = result

        clean_up(self, selectors)

        print("Test Step 5 : Check password field with eight dashes (fail).")
        fill_fields(self, selectors, negative_tests_password, 4)
        step_result = self.driver.find_element_by_css_selector(selectors.result).text
        result = check_step_fail(step_result, negative_tests_password, 4)

        if result is not None:  # Result is only not None when test had failed once or more
            end_result = result

        clean_up(self, selectors)

        final_result(self.tc, end_result)
        self.driver.close()
