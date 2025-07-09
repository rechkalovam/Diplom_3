from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_elements_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def click_to_element(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator)).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def wait_until_element_is_invisible(self, locator):
        return self.wait.until(expected_conditions.invisibility_of_element_located(locator))

    #использую его там, где обычные клики не работают из-за оверлея
    def safe_click(self, click_locator, overlay_locator=None, retries=2):
        last_exception = None
        for attempt in range(retries):
            try:
                if overlay_locator:
                    try:
                        self.wait.until(
                            expected_conditions.invisibility_of_element_located(overlay_locator)
                        )
                    except TimeoutException:
                        try:
                            overlay = self.find_element_with_wait(overlay_locator)
                            self.wait.until(expected_conditions.staleness_of(overlay))
                        except TimeoutException:
                            pass
                element = self.find_element_with_wait(click_locator)
                self.driver.save_screenshot(f"debug_click_attempt_{attempt}.png")
                try:
                    ActionChains(self.driver).move_to_element(element).click().perform()
                except ElementClickInterceptedException:
                    self.driver.execute_script("arguments[0].click();", element)
                return True
            except Exception as e:
                last_exception = e
        raise TimeoutException(f"Ошибка клика на элемент {click_locator} после {retries} попыток") from last_exception

    def wait_change_text_in_element(self, locator, text):
        try:
            self.wait.until_not(expected_conditions.text_to_be_present_in_element(locator, text))
            return True
        except TimeoutException:
            return False

    def wait_text_in_element(self, locator, text):
        try:
            self.wait.until(expected_conditions.text_to_be_present_in_element(locator, text))
            return True
        except TimeoutException:
            return False

    def drag_and_drop(self, source, target):
        js_code = """
            const sourceNode = arguments[0];
            const destinationNode = arguments[1];

            if (!(sourceNode instanceof HTMLElement) || !(destinationNode instanceof HTMLElement)) {
                throw new Error("One or both arguments are not DOM elements");
            }

            const dataTransfer = new DataTransfer();

            const dragStartEvent = new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer
            });
            sourceNode.dispatchEvent(dragStartEvent);

            const dropEvent = new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer
            });
            destinationNode.dispatchEvent(dropEvent);

            const dragEndEvent = new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer
            });
            sourceNode.dispatchEvent(dragEndEvent);
        """
        source = self.driver.find_element(*source)
        target = self.driver.find_element(*target)
        self.driver.execute_script(js_code, source, target)

