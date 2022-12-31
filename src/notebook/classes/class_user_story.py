from notebook.classes.class_file_manager import FileManager
from notebook.classes.class_user_interface import UserInterface
from notebook.usefull.constants import MENU


class UserStory(UserInterface):
    def __init__(self):
        self.file_manager = FileManager()

    @staticmethod
    def get_menu_items():
        return list(MENU.keys())

    def get_notebook(self):
        read_file_notebook = self.file_manager.read_file()
        return read_file_notebook

    def show_menu(self):
        self.send_user_message('-' * 50)
        for user_choice, data in MENU.items():
            self.send_user_message(f'{user_choice}. {data["name"]}')
        self.send_user_message('-' * 50)

    def show_notebook(self):
        self.send_user_message('-' * 50)
        file_data = self.file_manager.read_file()
        if len(file_data) == 0:
            self.send_user_message('Notebook is empty')
        else:
            self.send_user_message(f'Notebook contains {len(file_data)} record(s)')

    def turn_command(self, command, notebook):
        getattr(notebook(), MENU[command]['function'])()
        self.send_user_message('-' * 50)


