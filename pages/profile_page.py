import allure
from helpers import HelpersMethods
from locators.header_locators import HeaderLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):

    @allure.step('Проверка отображения личного кабинета')
    def check_visibility_of_profile_page(self):
        return self.find_element_with_wait(ProfilePageLocators.PROFILE_INFO)

    @allure.step('Переход в раздел истории заказов')
    def go_to_orders_history(self):
        self.safe_click(ProfilePageLocators.ORDER_HISTORY_BUTTON, overlay_locator=HeaderLocators.OVERLAY_LOCATOR)

    @allure.step('Проверка отображения списка истории заказов')
    def check_orders_history_visibility(self):
       return self.find_element_with_wait(ProfilePageLocators.ORDER_HISTORY_LIST)

    @allure.step('Получение списка заказов в истории заказов')
    def get_history_orders_list(self):
        elements = self.find_elements_with_wait(ProfilePageLocators.ORDER_HISTORY_LIST)
        return [HelpersMethods.clean_order_number(el.text) for el in elements]

    @allure.step('Переход в раздел "Лента заказов"')
    def click_to_orders_list_page(self):
        self.click_to_element(HeaderLocators.ORDER_LIST_BUTTON)

    @allure.step('Выход из аккаунта')
    def logout(self):
        self.wait_until_element_is_invisible(HeaderLocators.OVERLAY_LOCATOR)
        self.click_to_element(ProfilePageLocators.LOGOUT_BUTTON)