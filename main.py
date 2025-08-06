import logging

from apps.auth.views import RegisterView, LogoutView, LoginView
from core.utils import main_menu, get_user_option, execute_tables, user_menu

logging.basicConfig(level=logging.INFO, filename='logs.log')
logger = logging.getLogger(__name__)


class Menu:
    def main_menu(self):
        option = get_user_option(menu=main_menu, max_option=4)
        if option == "1":
            return self.main_menu()
        elif option == "2":
            result = RegisterView().register()
            if not result:
                print("Something get wrong, try again later")
        elif option == "3":
            user = LoginView().login()
            if user:
                return self.user_menu()
            print("Invalid phone number or password")
        return self.main_menu()

    def user_menu(self):
        option = get_user_option(menu=user_menu, max_option=5)
        if option == "1":
            self.PostMenu().show_posts()
        elif option == "2":
            self.PostMenu().add_posts()
        elif option == "3":
            self.PostMenu().delete_posts()
        elif option == "4":
            self.PostMenu().update_posts()
        return self.user_menu()

    def admin_menu(self):
        pass


if __name__ == '__main__':
    execute_tables()
    LogoutView.logout_all_users()
    Menu().main_menu()
