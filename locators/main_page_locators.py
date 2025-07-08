from selenium.webdriver.common.by import By
from locators.header_locators import HeaderLocators


class MainPageLocators(HeaderLocators):
    GO_TO_PROFILE_BUTTON = By.XPATH, "//button[text()='Войти в аккаунт']"
    CREATE_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"
    CONSTRUCTOR_HEADER = By.XPATH, "//h1[text()='Соберите бургер']"
    INGREDIENT = By.XPATH, '//a[contains(@class, "BurgerIngredient_ingredient")]'
    INGREDIENT_MODAL_WINDOW = By.XPATH, "//section[contains(@class, 'modal_opened')]"
    INGREDIENT_COUNTER = By.XPATH, '//p[contains(@class, "counter_counter__num")]'
    BASKET = By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket')]"
    ORDER_NUMBER = By.XPATH, "//h2[contains(@class, 'modal__title_shadow')]"
    ORDER_MODAL_WINDOW = By.XPATH, "//div[contains(@class, 'modal_opened')]"
    CLOSE_MODAL_BUTTON = By.XPATH, "//button[contains(@class, 'modal__close')]"




