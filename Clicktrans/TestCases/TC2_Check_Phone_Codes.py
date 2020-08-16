"""
Szymon Kotlowski 2020

Test Case ID - 2

Test environment:
Windows 10 HOME
Google Chrome

Preconditions:
1. Load Google Chrome properly
2. Enter dev-1.clicktrans.pl/register-test/courier website

Test Steps:
1 - 227 Check phone codes.

Test objective:
All phone Codes are accepted by registration sheet when the rest of fields are correct.

Expected result:
The registration sheet accepted registration.

Implementation: Szymon Kotlowski
Last edited by: Szymon Kotlowski
Last edit date: 16.08.2020
"""

# import region
from selenium import webdriver
from Libraries import selectors
from Libraries.constants import FIRST_PHONE_CODE, LAST_PHONE_CODE
from Libraries.operations import check_step, \
    current_test, current_step, final_result, clean_up, phone_codes_test
from Libraries.values import positive_tests
from time import sleep


class TC2_Check_Phone_Codes:

    def __init__(self, driver_path, adress):
        self.tc = __class__.__name__
        current_test(self.tc)

        #Precondtions region
        print("Precondition 1 : Load Google Chrome properly")
        self.driver = webdriver.Chrome(driver_path)
        sleep(5)  # wait for chrome load properly

        print("Precondition 2 : Enter dev-1.clicktrans.pl/register-test/courier webside")
        self.driver.get(adress)
        sleep(5)  # wait for website load properly

    def testcase(self):
        result = None
        end_result = None

        # Test Steps region
        for index in range(FIRST_PHONE_CODE, LAST_PHONE_CODE):
            print("Test Step {} : Checking phone code: {}".format(index, current_step(self, selectors, index)))
            phone_codes_test(self, selectors, index)
            step_result = self.driver.find_element_by_css_selector(selectors.result).text
            result = check_step(step_result, positive_tests, 0)

            if result is not None:  # Result is only not None when test had failed once or more
                end_result = result

            clean_up(self, selectors)

        final_result(self.tc, end_result)

        self.driver.close()
