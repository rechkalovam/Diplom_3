import allure
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage

class TestProfilePage:

    @allure.title("Проверка перехода в личный кабинет с главной страницы")
    def test_go_to_user_profile(self, main_page_with_login):
        main_page_with_login.go_to_profile_page()
        profile_page = ProfilePage(main_page_with_login.driver)
        assert profile_page.check_visibility_of_profile_page(), 'Раздел "Личный кабинет" не отображается'

    @allure.title("Проверка перехода в раздел 'История заказов' в личном кабинете")
    def test_go_to_orders_history(self, main_page_with_login):
        main_page_with_login.create_order()
        main_page_with_login.go_to_profile_page()
        profile_page = ProfilePage(main_page_with_login.driver)
        profile_page.go_to_orders_history()
        assert profile_page.check_orders_history_visibility(), 'Раздел "История заказов" не отображается'

    @allure.title("Проверка отображения окна авторизации после логаута пользователя")
    def test_check_user_logout(self, profile_page):
        profile_page.logout()
        login_page = LoginPage(profile_page.driver)
        assert login_page.check_visibility_of_login_page(), 'Окно авторизации не отображается'