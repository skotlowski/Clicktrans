# import region
from Libraries.constants import CHROME_DRIVER_PATH, HTML
from TestCases.TC1_Check_All_Fields import TC1_Check_All_Fields as TC1
from TestCases.TC2_Check_Phone_Codes import TC2_Check_Phone_Codes as TC2
from TestCases.TC3_Check_Password_Field_With_Wrong_Data import TC3_Check_Password_Field_With_Wrong_Data as TC3
from TestCases.TC4_Check_Password_Field_With_Company_Name import TC4_Check_Password_Field_With_Company_Name as TC4


class StartPoint:

        TC1(CHROME_DRIVER_PATH, HTML).testcase()
        #TC2(CHROME_DRIVER_PATH, HTML).testcase()
        #TC3(CHROME_DRIVER_PATH, HTML).testcase()
        #TC4(CHROME_DRIVER_PATH, HTML).testcase()

