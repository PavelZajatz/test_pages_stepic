import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ec or fr")


@pytest.fixture(scope="class")
def browser(request):
    print("\nstart chrome browser for test..")
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
        # browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        browser = webdriver.Remote('http://0.0.0.0:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        #browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=fp)
        browser = webdriver.Remote('http://0.0.0.0:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
    else:
        print("Browser <browser_name> is still not implemented")
    yield browser
    print("\nquit browser..")
    time.sleep(2)
    browser.quit()
