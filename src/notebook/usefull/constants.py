
MENU = {1: {'name': 'Show notebook',
            'function': 'show_notebook'},
        2: {'name': 'Add record',
            'function': 'add_record'},
        3: {'name': 'Remove record',
            'function': 'remove_record'},
        4: {'name': 'Change record',
            'function': 'change_record'},
        5: {'name': 'Search by name',
            'function': 'search_by_name'},
        6: {'name': 'Search by phone number',
            'function': 'search_by_phone_number'},
        7: {'name': 'Search by last name',
           'function': 'search_by_last_name'},
        8: {'name': 'Sort by name',
            'function': 'sort_by_name'},
        9: {'name': 'Sort by last name',
            'function': 'sort_by_last_name'},
        10: {'name': 'Exit',
            'function': 'turn_off'}
}

NOTEBOOK_FIELDS = {'name': 'required',
                   'last_name': 'required',
                   'phone_number': 'required',
                   'address': '',
                   'birthday': ''
                   }
