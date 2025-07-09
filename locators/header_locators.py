from selenium.webdriver.common.by import By


class HeaderLocators:
    CONSTRUCTOR_BUTTON = By.XPATH, "//a/p[text()='Конструктор']"
    ORDER_LIST_BUTTON = By.XPATH, "//a/p[text()='Лента Заказов']"
    PROFILE_BUTTON = By.XPATH, "//a/p[text()='Личный Кабинет']"
    OVERLAY_LOCATOR = By.XPATH, "//div[contains(@class, 'modal_overlay')]"