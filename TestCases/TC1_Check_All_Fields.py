"""
Szymon Kotlowski 2020

Test Case ID - 1

Test environment:
Windows 10 HOME
Google Chrome

Preconditions:
1. Load Google Chrome properly.
2. Enter dev-1.clicktrans.pl/register-test/courier website.

Test Steps:
1. Check all fields with correct data.

Test objective:
After fill all fields with correct data and push the registration button, the registration form
accepted registration.

Expected result:
The registration form accepted registration.

Implementation: Szymon Kotlowski
Last edited by: Szymon Kotlowski
Last edit date: 16.08.2020
"""

# import region
from selenium import webdriver
from Libraries import selectors
from Libraries.operations import current_test, final_result,\
    fill_fields, clean_up, check_step, test_steps
from time import sleep
from Libraries.values import positive_tests


class TC1_Check_All_Fields:

    def __init__(self, driver_path, adress):
        self.tc = __class__.__name__
        current_test(self.tc)

        # Preconditions region
        print("Precondition 1 : Load Google Chrome properly.")
        self.driver = webdriver.Chrome(driver_path)
        sleep(5)  # wait for chrome load properly

        print("Precondition 2 : Enter dev-1.clicktrans.pl/register-test/courier website.")
        self.driver.get(adress)
        sleep(5)  # wait for website load properly

    def testcase(self):
        end_result = None

        # Test Steps region
        for index in range(test_steps(positive_tests)):
            print("Test Step {} : Check fields with correct data".format(index+1))
            fill_fields(self, selectors, positive_tests, index)
            step_result = self.driver.find_element_by_css_selector(selectors.result).text
            result = check_step(step_result, positive_tests, index)

            if result is not None:  # Result is only not None when test had failed once or more
                end_result = result

            clean_up(self, selectors)

        final_result(self.tc, end_result)

        self.driver.close()
