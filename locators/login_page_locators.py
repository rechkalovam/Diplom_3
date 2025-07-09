from selenium.webdriver.common.by import By
from locators.header_locators import HeaderLocators


class LoginPageLocators(HeaderLocators):
    LOGIN_PAGE_HEADER = By.XPATH, "//h2[text()='Вход']"
    EMAIL_INPUT = By.XPATH, "//input[@type='text']"
    PASSWORD_INPUT = By.XPATH, "//input[@type='password']"
    LOGIN_BUTTON = By.XPATH, "//button[text()='Войти']"
    RESET_PASSWORD_BUTTON = By.XPATH, "//a[text()='Восстановить пароль']"