#
# @see https://pypi.python.org/pypi/selenium
# @see https://github.com/actmd/elementium
# @see https://elliterate.github.io/capybara.py/
#

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from elementium.drivers.se import SeElements
import capybara

# #se = SeElements(webdriver.Chrome())
# se = SeElements(webdriver.Firefox())
# se.navigate("http://www.python.org").insist(lambda e: "Python" in e.title)
# se.find("q").write("selenium" + Keys.RETURN)


from enum import Enum


class WebdriverWrapperType(Enum):
    RAW = 1
    ELEMENTIUM = 2  # https://github.com/actmd/elementium
    CAPYBARA = 3    # https://elliterate.github.io/capybara.py/


USE_WEBDRIVER_WRAPPER = WebdriverWrapperType.CAPYBARA
#USE_WEBDRIVER_WRAPPER = WebdriverWrapperType.RAW
#USE_WEBDRIVER_WRAPPER = WebdriverWrapperType.ELEMENTIUM


# setting for chrome webdriver
chrome_options = Options()
chrome_options.add_argument('headless')
chrome_options.add_argument('no-sandbox')
chrome_options.add_argument('disable-setuid-sandbox')
chrome_options.add_argument('window-size=1920,1080')


# set remote webdriver addr, if necessary
REMOTE_CHROME_ADDR = "http://docker.for.mac.localhost:9515/wd/hub"  # from Docker container to host
#REMOTE_CHROME_ADDR = "http://127.0.0.1:9515/wd/hub"                # from host to the same host


def before_all(context):
    print("> Starting the browser")

    global chrome_options

    if USE_WEBDRIVER_WRAPPER == WebdriverWrapperType.RAW:
        context.driver = webdriver.Chrome(chrome_options=chrome_options)
    elif USE_WEBDRIVER_WRAPPER == WebdriverWrapperType.ELEMENTIUM:
        context.driver = SeElements(
            webdriver.Chrome(chrome_options=chrome_options))
    elif USE_WEBDRIVER_WRAPPER == WebdriverWrapperType.CAPYBARA:
        capybara.current_driver = "selenium_chrome"          # headless
        #capybara.current_driver = "selenium_remote_chrome"  # gui
        capybara.default_max_wait_time = 10
        capybara.current_session().current_window.resize_to(1920, 1080)


def after_all(context):
    print("< Closing the browser")
    if USE_WEBDRIVER_WRAPPER == WebdriverWrapperType.RAW:
        context.driver.close()  # selenium version
        context.driver.quit()   # selenium version
    elif USE_WEBDRIVER_WRAPPER == WebdriverWrapperType.ELEMENTIUM:
        context.driver.browser.quit()   # elementium version
    elif USE_WEBDRIVER_WRAPPER == WebdriverWrapperType.CAPYBARA:
        pass


@capybara.register_driver("selenium_chrome")
def init_selenium_chrome_driver(app):
    from capybara.selenium.driver import Driver
    global chrome_options
    return Driver(app, browser="chrome", chrome_options=chrome_options)


@capybara.register_driver("selenium_remote_chrome")
def init_selenium_chrome_driver(app):
    from capybara.selenium.driver import Driver
    return Driver(app, browser="remote",
                  command_executor=REMOTE_CHROME_ADDR,
                  desired_capabilities=DesiredCapabilities.CHROME)
