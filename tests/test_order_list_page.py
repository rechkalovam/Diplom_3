import allure
from pages.order_list_page import OrderListPage
from pages.profile_page import ProfilePage
from urls import ORDERS_LIST_PAGE


class TestOrderListPage:

    @allure.title("Проверка перехода на страницу ленты заказов по кнопке 'Лента заказов'")
    def test_click_and_check_transition_to_orders_list(self, main_page_without_login):
        main_page_without_login.click_to_orders_list()
        order_list_page = OrderListPage(main_page_without_login.driver)
        assert order_list_page.check_transition_to_orders_list_page(), 'Страница ленты заказов не отображается'

    @allure.title("Проверка отображения модального окна заказа в ленте заказов после клика на заказ")
    def test_click_and_check_order_modal_window_visibility(self, main_page_without_login):
        main_page_without_login.click_to_orders_list()
        order_list_page = OrderListPage(main_page_without_login.driver)
        order_list_page.click_to_order()
        assert order_list_page.check_order_modal_window_is_displayed(), 'Модальное окно заказа не отображается'

    @allure.title("Проверка отображения заказов пользователя из истории заказов на странице 'Лента заказов'")
    def test_orders_in_orders_history_displayed_in_orders_list_page(self, main_page_with_login):
        main_page_with_login.create_order()
        main_page_with_login.go_to_profile_page()
        profile_page = ProfilePage(main_page_with_login.driver)
        profile_page.go_to_orders_history()
        user_orders = profile_page.get_history_orders_list()
        profile_page.click_to_orders_list_page()
        orders_list_page = OrderListPage(profile_page.driver)
        all_orders = orders_list_page.get_orders_list_orders()
        assert set(user_orders) <= set(all_orders)

    @allure.title("Проверка увеличения счетчика заказов за все время после оформления заказа")
    def test_total_orders_count_updates_after_order_created(self, main_page_with_login):
        main_page_with_login.click_to_orders_list()
        orders_list = OrderListPage(main_page_with_login.driver)
        total_orders_count_before_order = orders_list.get_total_orders_count()
        orders_list.click_to_constructor()
        main_page_with_login.create_order()
        main_page_with_login.click_to_orders_list()
        total_orders_count_after_order = orders_list.get_total_orders_count()
        assert total_orders_count_before_order < total_orders_count_after_order

    @allure.title("Проверка увеличения счетчика заказов за все время после оформления заказа")
    def test_today_orders_count_updates_after_order_created(self, main_page_with_login):
        main_page_with_login.click_to_orders_list()
        orders_list = OrderListPage(main_page_with_login.driver)
        today_orders_count_before_order = orders_list.get_today_orders_count()
        orders_list.click_to_constructor()
        main_page_with_login.create_order()
        main_page_with_login.click_to_orders_list()
        today_orders_count_after_order = orders_list.get_today_orders_count()
        assert today_orders_count_before_order < today_orders_count_after_order

    @allure.title("Проверка появления номера заказа в разделе 'В работе' после оформления")
    def test_new_order_added_to_in_progress_orders_list(self, main_page_with_login):
        order = main_page_with_login.create_order()
        order_page = OrderListPage(main_page_with_login.driver)
        order_page.go_to_url(ORDERS_LIST_PAGE)
        assert order_page.check_order_in_work(order)






