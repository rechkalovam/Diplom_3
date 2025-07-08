import allure
from pages.base_page import BasePage
from locators.header_locators import HeaderLocators
from locators.order_list_page_locators import OrderListPageLocators
from helpers import HelpersMethods


class OrderListPage(BasePage):

    @allure.step('Клик на "Конструктор"')
    def click_to_constructor(self):
        self.click_to_element(HeaderLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Проверка перехода на страницу ленты заказов при клике на "Лента заказов"')
    def check_transition_to_orders_list_page(self):
        return self.find_element_with_wait(OrderListPageLocators.ORDER_LIST_HEADER)

    @allure.step('Клик на заказ в списке заказов')
    def click_to_order(self):
        self.click_to_element(OrderListPageLocators.ORDER_ITEM)

    @allure.step('Проверка открытия модального окна подробной информации о заказе')
    def check_order_modal_window_is_displayed(self):
        return self.find_element_with_wait(OrderListPageLocators.MODAL_ORDER_WINDOW)

    @allure.step('Получение списка заказов в ленте заказов')
    def get_orders_list_orders(self):
        elements = self.find_elements_with_wait(OrderListPageLocators.ORDER_ITEM)
        return [HelpersMethods.clean_order_number(el.text.split('\n')[0]) for el in elements]

    @allure.step('Получить количество заказов за все время')
    def get_total_orders_count(self):
        return self.get_text_from_element(OrderListPageLocators.TOTAL_ORDER_COUNT)

    @allure.step('Получить количество заказов за сегодня')
    def get_today_orders_count(self):
        return self.get_text_from_element(OrderListPageLocators.TODAY_ORDERS_COUNT)

    @allure.step('Проверить, что заказ в работе')
    def check_order_in_work(self, order):
        return self.wait_text_in_element(OrderListPageLocators.ORDER_IN_WORK_LIST_ITEM, f'0{order}')