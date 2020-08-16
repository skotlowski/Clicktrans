class positive_tests:
    company_name = ['Company "company"', 'jfJKSDlx!12', 'FirmaTransportowa', '34', "That's All"]
    e_mail = ['anyemail23@wp.pl', 'example@example.pl', 'example@example.br', 'mail@asd.us', 'example@gmail.com']
    name_surname = ['Any Name', 'Alex Alex', 'Finlay McGraw', 'Jarret Roberts', 'Makena Woods']
    phone_number = ['435654234', '000000000', '987312476', '543765321', '765432358']
    password = ['Djg32zasd3!', 'TESTtestz', 'qwertyweg1!', 'lsfd345!sdfZ', 'kjhryf$#4!2']


class negative_tests_password:
    company_name = ['Company "company"', 'jfJKSDlx!12', 'FirmaTransportowa', '34', "That's All"]
    e_mail = ['anyemail23@wp.pl', 'example@example.pl', 'example@example.pl', 'mail@asd.pl', 'example@gmail.com']
    name_surname = ['Any Name', 'Alex Alex', 'Finlay McGraw', 'Jarret Roberts', 'Makena Woods']
    phone_number = ['435654234', '000000000', '987312476', '543765321', '765432358']
    password = ['aaaaaaaa', 'a', ' ', '        ', '--------']


class negative_tests_password_companyname:
    company_name = ['Company "company"', 'jfJKSDlx!12', 'FirmaTransportowa', 'Intel Technology', "That's All"]
    e_mail = ['anyemail23@wp.pl', 'example@example.pl', 'example@example.pl', 'mail@asd.pl', 'example@gmail.com']
    name_surname = ['Any Name', 'Alex Alex', 'Finlay McGraw', 'Jarret Roberts', 'Makena Woods']
    phone_number = ['435654234', '000000000', '987312476', '543765321', '765432358']
    password = ['Company "company"', 'jfJKSDlx!12', 'FirmaTransportowa', 'Intel Technology', "That's All"]
