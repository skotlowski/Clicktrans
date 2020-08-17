"""
Szymon Kotlowski 2020

Test Case ID - 4

Test environment:
Windows 10 HOME
Google Chrome

Preconditions:
1. Load Google Chrome properly
2. Enter dev-1.clicktrans.pl/register-test/courier website

Test Steps:
1. Test Step 1 - 5 : Check the password field with password same as company name (fail).

Expected result:
After fill all fields with correct data except the password field (filled with company name) and push
the registration button, the registration form is refused (negative test).

Implementation: Szymon Kotlowski
Last edited by: Szymon Kotlowski
Last edit date: 16.08.2020
"""

# import region
from selenium import webdriver
from Libraries import selectors
from Libraries.operations import current_test, final_result, fill_fields,\
    clean_up, check_step_fail, test_steps
from time import sleep
from Libraries.values import negative_tests_password_companyname


class TC4_Check_Password_Field_With_Company_Name:

    def __init__(self, driver_path, adress):
        self.tc = __class__.__name__
        current_test(self.tc)

        # Preconditions region
        print("Precondition 1 : Wait for Chrome load properly")
        self.driver = webdriver.Chrome(driver_path)
        sleep(5)  # wait for chrome load properly

        print("Precondition 2 : Wait for webpage load properly")
        self.driver.get(adress)
        sleep(5)  # wait for website load properly

    def testcase(self):
        end_result = None

        # Test Steps region
        for index in range(test_steps(negative_tests_password_companyname)):
            print("Test Step {} : Check the password field with password same as a company name (fail)".format(index+1))
            fill_fields(self, selectors, negative_tests_password_companyname, index)
            step_result = self.driver.find_element_by_css_selector(selectors.result).text
            result = check_step_fail(step_result, negative_tests_password_companyname, index)

            if result is not None:  # Result is only not None when test had failed once or more
                end_result = result
            clean_up(self, selectors)

        final_result(self.tc, end_result)

        self.driver.close()

