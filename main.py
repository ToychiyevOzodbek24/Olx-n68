from core.utils import main_menu, get_user_option


class Menu:
    @staticmethod
    def main_menu():
        option = get_user_option(menu=main_menu, max_option=4)

    def user_menu(self):
        pass

    def admin_menu(self):
        pass


if __name__ == '__main__':
    # execute_tables()
    Menu.main_menu()
