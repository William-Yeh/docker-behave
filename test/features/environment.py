#
#
# @see https://github.com/actmd/elementium
#

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from elementium.drivers.se import SeElements
import capybara

# #se = SeElements(webdriver.Chrome())
# se = SeElements(webdriver.Firefox())
# se.navigate("http://www.python.org").insist(lambda e: "Python" in e.title)
# se.find("q").write("selenium" + Keys.RETURN)


import os

#from xvfbwrapper import Xvfb


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
# if CHROME_BINARY_PATH:
#    chrome_options.binary_location = CHROME_BINARY_PATH


CHROME_BINARY_PATH = os.environ.get('CHROME_BINARY_PATH')


def before_all(context):
    #context.vdisplay = Xvfb()
    # context.vdisplay.start()
    print("> Starting the browser")
    #browser = context.config.userdata.get("browser")
    #context.driver = webdriver.Firefox()

    #chrome_options = Options()
    global chrome_options

    if USE_WEBDRIVER_WRAPPER == WebdriverWrapperType.RAW:
        context.driver = webdriver.Chrome(chrome_options=chrome_options)
    elif USE_WEBDRIVER_WRAPPER == WebdriverWrapperType.ELEMENTIUM:
        context.driver = SeElements(
            webdriver.Chrome(chrome_options=chrome_options))
    elif USE_WEBDRIVER_WRAPPER == WebdriverWrapperType.CAPYBARA:
        capybara.current_driver = "selenium_chrome"
        capybara.default_max_wait_time = 10
        context.driver = capybara


def after_all(context):
    print("< Closing the browser")
    if USE_WEBDRIVER_WRAPPER == WebdriverWrapperType.RAW:
        context.driver.close()  # selenium version
        context.driver.quit()   # selenium version
    elif USE_WEBDRIVER_WRAPPER == WebdriverWrapperType.ELEMENTIUM:
        context.driver.browser.quit()   # elementium version
    elif USE_WEBDRIVER_WRAPPER == WebdriverWrapperType.CAPYBARA:
        pass

    # context.vdisplay.stop()


@capybara.register_driver("selenium_chrome")
def init_selenium_chrome_driver(app):
    from capybara.selenium.driver import Driver
    global chrome_options
    return Driver(app, browser="chrome", chrome_options=chrome_options)
