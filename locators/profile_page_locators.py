from selenium.webdriver.common.by import By
from locators.header_locators import HeaderLocators


class ProfilePageLocators(HeaderLocators):
    PROFILE_INFO = By.XPATH, "//div[contains(@class, 'Profile_profile')]"
    ORDER_HISTORY_BUTTON = By.XPATH, "//a[text()='История заказов']"
    ORDER_HISTORY_LIST = By.XPATH, "//p[contains(text(), '#')]"
    LOGOUT_BUTTON = By.XPATH, "//button[text()='Выход']"



