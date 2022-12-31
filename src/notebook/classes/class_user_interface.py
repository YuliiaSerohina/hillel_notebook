from notebook.usefull.constants import NOTEBOOK_FIELDS
from tabulate import tabulate


class UserInterface:

    @staticmethod
    def ask_user(message):
        user_data = input(message).strip()
        return user_data

    @staticmethod
    def send_user_message(message):
        print(message)

    def show_output(self, output_data, headers=None):
        if headers is None:
            headers = list(NOTEBOOK_FIELDS.keys())
        if len(output_data) == 0:
            self.send_user_message('There are not records to show')
        else:
            self.send_user_message("-" * 50)
            tabulate_list = [items.values() for items in output_data]
            self.send_user_message(tabulate(tabulate_list, headers=headers))

