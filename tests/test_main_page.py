import allure
from pages.order_list_page import OrderListPage


class TestMainPage:

    @allure.title("Проверка перехода на страницу конструктора по кнопке 'Конструктор'")
    def test_click_and_check_transition_to_constructor(self, main_page_without_login):
        main_page_without_login.click_to_orders_list()
        order_list_page = OrderListPage(main_page_without_login.driver)
        order_list_page.click_to_constructor()
        assert main_page_without_login.check_transition_to_constructor_page(), 'Страница конструктора не отображается'

    @allure.title("Проверка отображения модального окна с информацией об ингредиенте")
    def test_click_to_ingredient_show_modal_ingredient_window(self, main_page_without_login):
        main_page_without_login.click_to_ingredient()
        assert main_page_without_login.check_modal_window_ingredient_visibility(), 'Модальное окно детальной информации об ингредиенте не отображается'

    @allure.title("Проверка закрытия модального окна ингредиента с помощью крестика")
    def test_close_modal_ingredient_window(self, main_page_without_login):
        main_page_without_login.click_to_ingredient()
        main_page_without_login.close_modal_window_ingredient()
        assert main_page_without_login.check_modal_window_ingredient_invisibility(), 'Модальное окно все еще отображается'

    @allure.title("Проверка изменения значения в каунтере при перетаскивании ингредиента")
    def test_check_ingredient_counter_after_add_ingredient_in_basket(self, main_page_without_login):
        main_page_without_login.add_ingredient_to_basket()
        assert main_page_without_login.check_ingredient_counter_after_add_in_basket() == '2', 'Каунтер ингредиента не поменял значение'

    @allure.title("Проверка оформления заказа авторизованным пользователем")
    def test_create_order_user_with_login(self, main_page_with_login):
        order = main_page_with_login.create_order()
        assert order is not None, 'Номер заказа не получен'