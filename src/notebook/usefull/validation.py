import re
from datetime import datetime


def is_fild_valid(field, data):
    match field:
        case 'name':
            return (data != "" and data.isalpha()==True,
                    'Please, enter the field. The field can only contain letters')
        case 'last_name':
            return (data != "" and data.isalpha()==True,
                    'Please, enter the field. The field can only contain letters')
        case 'phone_number':
            return (data != "" and re.match("^\\d{10}$", data) is not None,
                    'Please, enter phone number in forman +38XXXXXXXXXX')
        case 'address':
            return True, ""
        case 'birthday':
            if data != '':
                try:
                    datetime.strptime(data, '%Y-%m-%d')
                    return True, ""
                except ValueError:
                    return False, 'Please, enter data in format YYYY-MM-DD'
            return True, ""
