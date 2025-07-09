import allure
from urls import LOGIN_PAGE_URL, RESET_PASSWORT_PAGE


class TestResetPassword:

    @allure.title("Проверка перехода на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    def test_click_to_reset_password_button_check_transition(self, driver, login_page, reset_password_page):
        login_page.go_to_url(LOGIN_PAGE_URL)
        login_page.go_to_reset_password_page()
        assert reset_password_page.check_visibility_reset_password_page(), 'Страница восстановления пароля не отображается'

    @allure.title("Проверка отображения второго окна восстановления пароля после ввода почты и клика по кнопке 'Восстановить'")
    def test_add_email_and_click_reset_button(self, reset_password_page):
        reset_password_page.go_to_url(RESET_PASSWORT_PAGE)
        reset_password_page.add_email_and_click_reset_button()
        assert reset_password_page.check_visibility_of_new_password_page(), 'Страница с вводом нового пароля не отображается'

    @allure.title("Проверка подсветки поля ввода пароля при клике на кнопку Показать/Скрыть пароль")
    def test_check_highlight_new_password_input_in_focus(self, reset_password_page):
        reset_password_page.go_to_url(RESET_PASSWORT_PAGE)
        reset_password_page.add_email_and_click_reset_button()
        reset_password_page.click_show_password_button()
        assert reset_password_page.check_highlight_new_password_input_in_focus(), 'Поле ввода нового пароля не подсвечивается'