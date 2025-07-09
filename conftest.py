import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from helpers import HelpersMethods
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.reset_password_page import ResetPasswordPage
from urls import USERS_API_URL, MAIN_PAGE_URL, LOGIN_PAGE_URL


@pytest.fixture(params = ['Chrome', 'Firefox'])
def driver(request):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    if request.param == 'Google':
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()

@pytest.fixture()
def create_user():
    user_data = HelpersMethods.generate_user_data()
    response = requests.post(f'{MAIN_PAGE_URL}/api{USERS_API_URL}/register', json=user_data)
    token = response.json()['accessToken']
    yield user_data["email"], user_data["password"]
    requests.delete(f'{MAIN_PAGE_URL}/api{USERS_API_URL}/user', headers={'Authorization': f'{token}'})

@pytest.fixture()
def login_user(create_user, driver):
    login_page = LoginPage(driver)
    login_page.go_to_url(LOGIN_PAGE_URL)
    email, password = create_user
    login_page.login_user(email, password)
    return login_page

@pytest.fixture()
def main_page_with_login(login_user):
    page = MainPage(login_user.driver)
    page.check_login_user()
    return page

@pytest.fixture()
def main_page_without_login(driver):
    page = MainPage(driver)
    page.go_to_url(MAIN_PAGE_URL)
    return page

@pytest.fixture()
def login_page(driver):
    page = LoginPage(driver)
    return page

@pytest.fixture()
def reset_password_page(driver):
    page = ResetPasswordPage(driver)
    return page

@pytest.fixture()
def profile_page(main_page_with_login):
    main_page_with_login.go_to_profile_page()
    page = ProfilePage(main_page_with_login.driver)
    page.check_visibility_of_profile_page()
    return page