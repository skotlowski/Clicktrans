company_name = '#user_register_company_name'
email = '#user_register_email'
name = '#user_register_name'
phone_number = '#user_register_phone'
password = '#user_register_plainPassword'
agreement_one = '#user_register_settings_agreementRegulations'  # checkbox
agreement_two = '#user_register_settings_agreementPersonalData'  # checkbox
agreement_three = '#user_register_settings_agreementMarketing'  # checkbox
register_button = '#user_register_submit'  # button
result = 'body > div.ui.container.flashmsg > div'
communique = 'body > div.ui.container.flashmsg > div > i'  # button


def phone_code(count):
    return '#user_register_phoneCode > option:nth-child({})'.format(count)
