from notebook.classes.class_notebook import Notebook
from notebook.classes.class_user_story import UserStory

if __name__ == "__main__":
    user_story = UserStory()
    user_story.show_notebook()
    while True:
        user_story.show_menu()
        try:
            user_choice = int(user_story.ask_user('Please, make your choice:'))
            if user_choice not in user_story.get_menu_items():
                user_story.send_user_message('Please, select data from menu')
            user_story.turn_command(user_choice, Notebook)
        except ValueError:
            user_story.send_user_message('Please, select data from menu')
            continue
