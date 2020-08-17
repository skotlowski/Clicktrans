# import region
from time import sleep
from colorama import Fore as fore
from Libraries.values import positive_tests
from Libraries.constants import TEST_STARTED, TEST_FAILED, TEST_PASSED, RESULT_OK, RESULT_ERROR, PASS, FAIL


def check_step(result, test_type, index):
    if result == RESULT_OK:
        print(fore.GREEN + PASS)
    else:
        print(fore.RED + FAIL, error_source(test_type, index))
        return TEST_FAILED


def check_step_fail(result, test_type, index):
    if result == RESULT_ERROR:
        print(fore.GREEN + PASS)
    else:
        print(fore.RED + FAIL, error_source(test_type, index))
        return TEST_FAILED


def error_source(test_type, index):
    return "Error occurred at following values: " \
           "Company name: {} | " \
           "E-mail: {} | " \
           "Name and Surname: {} | " \
           "Phone number: {} | " \
           "Password: {} ".format(test_type.company_name[index],
                                  test_type.e_mail[index],
                                  test_type.name_surname[index],
                                  test_type.phone_number[index],
                                  test_type.password[index])


def final_result(class_name, result):
    print()
    if result is None:
        print(fore.GREEN + class_name, TEST_PASSED)
    elif result == RESULT_ERROR:
        print(fore.RED + class_name, FAIL, result)
    else:
        print(fore.RED + class_name, result)


def current_step(test, selectors, index):
    return test.driver.find_element_by_css_selector(selectors.phone_code(index)).text


def current_test(name):
    print()
    print(fore.RESET + name, TEST_STARTED)


def fill_fields(test, selectors, values, index):
    test.driver.find_element_by_css_selector(selectors.company_name).send_keys(values.company_name[index])
    test.driver.find_element_by_css_selector(selectors.email).send_keys(values.e_mail[index])
    test.driver.find_element_by_css_selector(selectors.name).send_keys(values.name_surname[index])
    test.driver.find_element_by_css_selector(selectors.phone_number).send_keys(values.phone_number[index])
    test.driver.find_element_by_css_selector(selectors.password).send_keys(values.password[index])
    test.driver.find_element_by_css_selector(selectors.agreement_one).click()
    test.driver.find_element_by_css_selector(selectors.agreement_two).click()
    test.driver.find_element_by_css_selector(selectors.register_button).click()


def phone_codes_test(test, selectors, index):
    test.driver.find_element_by_css_selector(selectors.company_name).send_keys(positive_tests.company_name[0])
    test.driver.find_element_by_css_selector(selectors.email).send_keys(positive_tests.e_mail[0])
    test.driver.find_element_by_css_selector(selectors.name).send_keys(positive_tests.name_surname[0])
    test.driver.find_element_by_css_selector(selectors.phone_code(index)).click()
    test.driver.find_element_by_css_selector(selectors.phone_number).send_keys(positive_tests.phone_number[0])
    test.driver.find_element_by_css_selector(selectors.password).send_keys(positive_tests.password[0])
    test.driver.find_element_by_css_selector(selectors.agreement_one).click()
    test.driver.find_element_by_css_selector(selectors.agreement_two).click()
    test.driver.find_element_by_css_selector(selectors.register_button).click()


def clean_up(test, selectors):
    test.driver.find_element_by_css_selector(selectors.company_name).clear()
    test.driver.find_element_by_css_selector(selectors.name).clear()
    test.driver.find_element_by_css_selector(selectors.email).clear()
    test.driver.find_element_by_css_selector(selectors.phone_number).clear()
    test.driver.find_element_by_css_selector(selectors.password).clear()
    test.driver.find_element_by_css_selector(selectors.agreement_one).click()
    test.driver.find_element_by_css_selector(selectors.agreement_two).click()
    test.driver.find_element_by_css_selector(selectors.communique).click()
    __reset_colour()
    sleep(1)


def __reset_colour():
    print(fore.RESET, "")


def test_steps(test_type):
    return len(test_type.company_name)
