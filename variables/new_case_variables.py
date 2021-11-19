import os


class NewCaseVariables():
    plaintiff_person = {
        'MainInfo': {
            'surname': 'Test',
            'firstname': 'TestF',
            'dob': '01-01-1990',  # template 'dd-mm-yyyy'
            'gender': 'Мужской',
            'pin': '11111122233352',
        },
        'PassportInfo': {
            'number': 'ID1234567',
            'issue': '01-01-2020',
            'expire': '01-01-2030',
            'authority': 'SRS'
        }
    }
    # Plaintiff variables
    plaintiff_surname = 'Test'
    plaintiff_firstname = 'Test'
    plaintiff_date_of_birth = '01-01-1990'  # template 'dd-mm-yyyy'
    plaintiff_gender = 'Мужской'
    plaintiff_pin = '11111122233352'
    plaintiff_passport_number = 'ID1234567'
    plaintiff_passport_date_issue = '01-01-2020'
    plaintiff_passport_expire_date = '01-01-2030'
    plaintiff_passport_authority = 'SRS'

    # Claim variables
    claim_text = 'Исковое заявление о взыскании денежной компенсации за задержку выплаты заработной платы. Образец ' \
                 'искового заявления о взыскании денежной компенсации за задержку выплаты заработной платы. Истец ' \
                 'указывает в исковом заявлении, что уволился из организации по собственному желанию, однако, ' \
                 'работодатель выплатил причитающуюся заработную плату истцу не в день увольнения, а позднее, ' \
                 'чем нарушил требования норм Трудового кодекса РФ. Истцом заявлены требования о взыскании с ' \
                 'организации - работодателя в пользу работника (истца) денежной компенсации за задержку выплаты ' \
                 'зарплаты. '

    # Common info variables
    name_of_the_claim = 'Test name'
    applicable_right = 'Международное Право'
    standing_order = 'Простой (1 арбитр)'
    base_of_dispute = 'Расторжение договора'
    language = 'Испанский'

    # Payment info variables
    amount_of_claim = '1000'
    amount_of_claim_valute_name = 'Доллар'
    arbitration_fee = '1000'
    arbitration_fee_valute_name = 'Доллар'
    registration_fee = '1000'
    registration_fee_valute_name = 'Доллар'
    surcharge = '1000'
    surcharge_valute_name = 'Доллар'
    deadline_for_payment_of_the_arbitration_fee = '01-01-2021'
    deadline_for_additional_payment_of_the_arbitration_fee = '01-01-2021'

    # Document variables
    document = os.path.join('/home/gulida/Desktop/Worklog/check.pdf')
    document_description = 'Some descriptions'
    document_issue_date = '01-01-2021'
    document_file_type = 'pdf'
    document_type = 'Иное'

    # Document variables
    document_10 = os.path.join('/home/gulida/Desktop/Worklog/final.pdf')
    document_description_10 = 'Исковое заявление'
    document_issue_date_10 = '01-01-2021'
    document_file_type_10 = 'pdf'
    document_type_10 = 'Исковое заявление'