import allure
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage
from data import EMAIL_FOR_RESET_PASSWORD
from locators.reset_password_page_locators import ResetPasswordPageLocators


class ResetPasswordPage(BasePage):

    @allure.step('Проверка отображения страницы восстановления пароля')
    def check_visibility_reset_password_page(self):
        return self.find_element_with_wait(ResetPasswordPageLocators.RESET_PASSWORD_PAGE_HEADER)

    @allure.step('Ввод email и нажатие на кнопку "Восстановить"')
    def add_email_and_click_reset_button(self):
        self.add_text_to_element(ResetPasswordPageLocators.EMAIL_INPUT, EMAIL_FOR_RESET_PASSWORD)
        self.click_to_element(ResetPasswordPageLocators.RESET_BUTTON)

    @allure.step('Проверка отображения второго окна восстановления пароля после нажатия кнопки "Восстановить"')
    def check_visibility_of_new_password_page(self):
        return self.find_element_with_wait(ResetPasswordPageLocators.PASSWORD_INPUT)

    @allure.step('Переход на страницу ввода нового пароля и нажатие кнопки "Показать пароль"')
    def click_show_password_button(self):
        self.find_element_with_wait(ResetPasswordPageLocators.PASSWORD_INPUT)
        self.safe_click(ResetPasswordPageLocators.PASSWORD_VISIBILITY_BUTTON, HeaderLocators.OVERLAY_LOCATOR)

    @allure.step('Проверка подсветки поля нового пароля при нажатии "Показать пароль"')
    def check_highlight_new_password_input_in_focus(self):
        return self.find_element_with_wait(ResetPasswordPageLocators.PASSWORD_ACTIVE_INPUT)

