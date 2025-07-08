from selenium.webdriver.common.by import By
from locators.header_locators import HeaderLocators


class OrderListPageLocators(HeaderLocators):
    ORDER_LIST_HEADER = By.XPATH, "//h1[text()='Лента заказов']"
    ORDER_ITEM = By.XPATH, "//p[contains(text(), '#')]"
    TOTAL_ORDER_COUNT = By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"
    TODAY_ORDERS_COUNT = By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    ALL_ORDERS_LIST = By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]"
    MODAL_ORDER_WINDOW = By.XPATH, "//section[contains (@class, 'modal_opened')]"
    ORDER_IN_WORK_LIST_ITEM = By.XPATH, "//ul[contains(@class, 'orderListReady')]/li"