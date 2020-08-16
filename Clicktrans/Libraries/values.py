class positive_tests:
    company_name = ['Kimpton Hotels & Restaurants', 'W. L. Gore & Associates', 'Empik', 'Helios S.A', "Jan Kowalski221"]
    e_mail = ['anyemail23@wp.pl', 'example@example.pl', 'brazil@example.br', 'mail@asd.us', 'vietnam@mail.vn']
    name_surname = ['Any Name', 'Alex Alex', 'Finlay McGraw', 'Jarret Roberts', 'Makena Woods']
    phone_number = ['435654234', '000000000', '987312476', '543765321', '765432358']
    password = ['Djg32zasd3!', 'TESTtestz', 'qwertyweg1!', 'lsfd345!sdfZ', 'kjhryf$#4!2']


class negative_tests_password:
    company_name = ['Kimpton Hotels & Restaurants', 'W. L. Gore & Associates', 'Empik', 'Helios S.A', "Jan Kowalski221"]
    e_mail = ['anyemail23@wp.pl', 'example@example.pl', 'brazil@example.br', 'mail@asd.us', 'vietnam@mail.vn']
    name_surname = ['Any Name', 'Alex Alex', 'Finlay McGraw', 'Jarret Roberts', 'Makena Woods']
    phone_number = ['435654234', '000000000', '987312476', '543765321', '765432358']
    password = ['aaaaaaaa', 'a', ' ', '        ', '--------']


class negative_tests_password_companyname:
    company_name = ['Kimpton Hotels & Restaurants', 'W. L. Gore & Associates', 'Empik', 'Helios S.A', "Jan Kowalski221"]
    e_mail = ['anyemail23@wp.pl', 'example@example.pl', 'example@example.pl', 'mail@asd.pl', 'example@gmail.com']
    name_surname = ['Any Name', 'Alex Alex', 'Finlay McGraw', 'Jarret Roberts', 'Makena Woods']
    phone_number = ['435654234', '000000000', '987312476', '543765321', '765432358']
    password = ['Kimpton Hotels & Restaurants', 'W. L. Gore & Associates', 'Empik', 'Helios S.A', "Jan Kowalski221"]
