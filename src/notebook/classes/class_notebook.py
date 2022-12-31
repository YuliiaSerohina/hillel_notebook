from notebook.classes.class_user_story import UserStory
from notebook.usefull.constants import NOTEBOOK_FIELDS
from notebook.usefull.validation import is_fild_valid


class Notebook:

    def __init__(self):
        self.user_story = UserStory()

    def __create_new_record(self):
        local_record = {field: "" for field in NOTEBOOK_FIELDS.keys()}
        for field, required in NOTEBOOK_FIELDS.items():
            is_valid = False
            while not is_valid:
                is_required = '*' if required == 'required' else ''
                row = self.user_story.ask_user(f'Please enter your {field.title()} {is_required}:')

                is_valid, message = is_fild_valid(field, row)
                if not is_valid:
                    self.user_story.send_user_message(f'Error {message}')
                else:
                    local_record[field] = row
        return local_record

    def __create_notebook_ordered_list(self):
        notebook_new = self.user_story.file_manager.read_file()
        if len(notebook_new) > 0:
            output_data = []
            for index in range(len(notebook_new)):
                elem = {'idx': index}
                elem.update(notebook_new[index])
                output_data.append(elem)
            headers = ['index']
            headers.extend(list(NOTEBOOK_FIELDS.keys()))
            self.user_story.show_output(output_data, headers=headers)
            return notebook_new
        else:
            self.user_story.send_user_message('There are no rows')
            return []

    def __get_list_by_param(self, param):
        notebook_list = self.user_story.file_manager.read_file()
        output_data = sorted(notebook_list, key=lambda r:[param])
        return output_data

    def add_record(self):
        local_record = self.__create_new_record()
        self.user_story.file_manager.write_file(local_record)
        self.user_story.send_user_message('-' * 50)
        self.user_story.send_user_message('New record was successfully added')

    def change_record(self):
        create_ordered_list = self.__create_notebook_ordered_list()
        if not create_ordered_list:
            return
        while True:
            try:
                idx_selection = int(self.user_story.ask_user('Please, select idx record to change'))
                create_ordered_list.pop(idx_selection)
                self.user_story.file_manager.create_new_file(create_ordered_list)
                local_record = self.__create_new_record()
                self.user_story.file_manager.write_file(local_record)
                self.user_story.send_user_message('-' * 50)
                self.user_story.send_user_message('Record was successfully changed')
                break
            except ValueError:
                self.user_story.send_user_message("Sorry, incorrect input")
            except IndexError:
                self.user_story.send_user_message('Please, select idx from data')

    def remove_record(self):
        create_ordered_list = self.__create_notebook_ordered_list()
        if not create_ordered_list:
            return
        while True:
            try:
                idx_selection = int(self.user_story.ask_user('Please, select idx record to remove'))
                create_ordered_list.pop(idx_selection)
                self.user_story.send_user_message('Done')
                self.user_story.file_manager.create_new_file(create_ordered_list)
                break
            except ValueError:
                self.user_story.send_user_message("Sorry, incorrect input")
            except IndexError:
                self.user_story.send_user_message('Please, select idx from data')

    def search_by_last_name(self):
        show_notebook_search = []
        notebook_list = self.user_story.file_manager.read_file()
        self.user_story.send_user_message('You can enter a full or partial last name.'
                                          ' To search by part of the last name, use the combination A*')
        user_input = self.user_story.ask_user('Please, enter the last name:').lower()
        is_valid = False
        while not is_valid:
            user_input = self.user_story.ask_user('Please, enter the last name:').lower()
            is_valid, message = is_fild_valid('last_name', user_input)
            if not is_valid:
                self.user_story.send_user_message(message)
        for items in notebook_list:
            if items['last_name'].lower() == user_input:
                show_notebook_search.append(items)
        self.user_story.show_output(show_notebook_search)

    def search_by_name(self):
        show_notebook = []
        is_valid = False
        while not is_valid:
            search_by_name = self.user_story.ask_user('Please, enter the name:').lower()
            is_valid, message = is_fild_valid('name', search_by_name)
            if not is_valid:
                self.user_story.send_user_message(message)
        file_data = self.user_story.file_manager.read_file()
        for items in file_data:
            if items['name'].lower() == search_by_name:
                show_notebook.append(items)
        self.user_story.show_output(show_notebook)

    def search_by_phone_number(self):
        show_notebook = []
        is_valid = False
        while not is_valid:
            search_by_phone_number = self.user_story.ask_user('Please, enter phone number:')
            is_valid, message = is_fild_valid('phone_number', search_by_phone_number)
            if not is_valid:
                self.user_story.send_user_message(message)
        file_data = self.user_story.file_manager.read_file()
        for items in file_data:
            if items['phone_number'] == search_by_phone_number:
                show_notebook.append(items)
        self.user_story.show_output(show_notebook)

    def show_notebook(self):
        self.user_story.show_output(self.user_story.file_manager.read_file())

    def sort_by_last_name(self):
        output_data = self.__get_list_by_param('last_name')
        self.user_story.show_output(output_data)

    def sort_by_name(self):
        output_data = self.__get_list_by_param('name')
        self.user_story.show_output(output_data)

    def turn_off(self):
        self.user_story.send_user_message('See you')
        exit(0)

