from selenium.webdriver.common.by import By
from locators.header_locators import HeaderLocators


class ResetPasswordPageLocators(HeaderLocators):
    RESET_PASSWORD_PAGE_HEADER = By.XPATH, "//h2[text()='Восстановление пароля']"
    EMAIL_INPUT = By.XPATH, "//input[@type='text']"
    RESET_BUTTON = By.XPATH, "//button[text()='Восстановить']"
    PASSWORD_INPUT = By.XPATH, "//input[@type='password']"
    PASSWORD_VISIBILITY_BUTTON = By.XPATH, "//div[contains(@class, 'input__icon-action')]"
    PASSWORD_ACTIVE_INPUT = By.XPATH, "//label[contains(@class, 'input__placeholder-focused') and text()='Пароль']"