import allure
from pages.base_page import BasePage
from locators.header_locators import HeaderLocators
from locators.main_page_locators import MainPageLocators
from urls import MAIN_PAGE_URL


class MainPage(BasePage):

    @allure.step('Переход на страницу Личного кабинета')
    def go_to_profile_page(self):
        self.safe_click(HeaderLocators.PROFILE_BUTTON, HeaderLocators.OVERLAY_LOCATOR)

    @allure.step('Проверка успешного логина пользователя и появления кнопки "Оформить заказ"')
    def check_login_user(self):
        return self.find_element_with_wait(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Клик на "Лента заказов"')
    def click_to_orders_list(self):
        self.safe_click(HeaderLocators.ORDER_LIST_BUTTON, HeaderLocators.OVERLAY_LOCATOR)

    @allure.step('Проверка перехода на страницу конструктора при клике на "Конструктор"')
    def check_transition_to_constructor_page(self):
        return self.find_element_with_wait(MainPageLocators.CONSTRUCTOR_HEADER)

    @allure.step('Клик на ингредиент в конструкторе бургеров')
    def click_to_ingredient(self):
        self.click_to_element(MainPageLocators.INGREDIENT)

    @allure.step('Проверка отображения модального окна ингредиента')
    def check_modal_window_ingredient_visibility(self):
        return self.find_element_with_wait(MainPageLocators.INGREDIENT_MODAL_WINDOW)

    @allure.step('Закрытие модального окна ингредиента с помощью крестика')
    def close_modal_window_ingredient(self):
        self.click_to_element(MainPageLocators.CLOSE_MODAL_BUTTON)

    @allure.step('Проверка закрытия модального окна ингредиента')
    def check_modal_window_ingredient_invisibility(self):
        return self.wait_until_element_is_invisible(MainPageLocators.INGREDIENT_MODAL_WINDOW)

    @allure.step('Добавление ингредиента в заказ')
    def add_ingredient_to_basket(self):
        self.drag_and_drop(MainPageLocators.INGREDIENT, MainPageLocators.BASKET)

    @allure.step('Нажатие кнопки "Оформить заказ"')
    def click_order_button(self):
        self.safe_click(MainPageLocators.CREATE_ORDER_BUTTON, HeaderLocators.OVERLAY_LOCATOR)

    @allure.step('Проверка каунтера элемента после добавления в заказ')
    def check_ingredient_counter_after_add_in_basket(self):
        self.wait_change_text_in_element(MainPageLocators.INGREDIENT_COUNTER, '0')
        return self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Проверка отображения модального окна оформления заказа')
    def check_order_modal_window_visibility(self):
        return self.find_element_with_wait(MainPageLocators.ORDER_MODAL_WINDOW)

    '''
    тут вместо перехода по урлу на главную должно быть закрытие модалки крестиком, но оверлей
    так долго висит на этой модалке, что я не успевала поймать свой заказ в работе в одном из тестов
    '''
    @allure.step('Оформление заказа')
    def create_order(self):
        self.add_ingredient_to_basket()
        self.wait_until_element_is_invisible(HeaderLocators.OVERLAY_LOCATOR)
        self.click_order_button()
        self.check_order_modal_window_visibility()
        self.wait_change_text_in_element(MainPageLocators.ORDER_NUMBER, '9999')
        order_number = self.get_text_from_element(MainPageLocators.ORDER_NUMBER)
        self.go_to_url(MAIN_PAGE_URL)
        return order_number