import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    @allure.step('Войти в аккаунт')
    def login_user(self, email, password):
        self.find_element_with_wait(LoginPageLocators.LOGIN_PAGE_HEADER)
        self.add_text_to_element(LoginPageLocators.EMAIL_INPUT, email)
        self.add_text_to_element(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_to_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Перейти к странице восстановления пароля')
    def go_to_reset_password_page(self):
        self.click_to_element(LoginPageLocators.RESET_PASSWORD_BUTTON)

    @allure.step('Отображение окна авторизации после логаута')
    def check_visibility_of_login_page(self):
        return self.find_element_with_wait(LoginPageLocators.LOGIN_PAGE_HEADER)
