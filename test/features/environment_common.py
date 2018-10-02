#
# @see https://pypi.python.org/pypi/selenium
# @see https://github.com/actmd/elementium
# @see https://elliterate.github.io/capybara.py/
#

from enum import Enum
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from elementium.drivers.se import SeElements
import capybara

#---
# Chrome: headless (default) or gui mode?
#
webdriver_headless_mode = True

def use_headless_mode(on_or_off: bool):
    global webdriver_headless_mode
    webdriver_headless_mode = on_or_off


#---
# default high-level query engine for Chrome
#

class WebdriverWrapperType(Enum):
    RAW = 1
    ELEMENTIUM = 2  # https://github.com/actmd/elementium
    CAPYBARA = 3    # https://elliterate.github.io/capybara.py/

webdriver_wrapper = WebdriverWrapperType.CAPYBARA

def behave_use_capybara():
    global webdriver_wrapper
    webdriver_wrapper = WebdriverWrapperType.CAPYBARA

def behave_use_elementium():
    global webdriver_wrapper
    webdriver_wrapper = WebdriverWrapperType.ELEMENTIUM

def behave_use_raw():
    global webdriver_wrapper
    webdriver_wrapper = WebdriverWrapperType.RAW


#---
# setting for chrome webdriver
#
chrome_options = Options()
chrome_options.add_argument('headless')
chrome_options.add_argument('no-sandbox')
chrome_options.add_argument('disable-setuid-sandbox')
chrome_options.add_argument('window-size=1920,1080')
#CHROME_EXE_PATH='/usr/local/bin/chromedriver'


#---
# set remote webdriver addr, if necessary
#

remote_chrome_addr = "http://docker.for.mac.localhost:9515/wd/hub"  # from Docker container to host
#remote_chrome_addr = "http://127.0.0.1:9515/wd/hub"                # from host to the same host
def set_remote_chrome_addr(url: str):
    global remote_chrome_addr
    remote_chrome_addr = url


#---
# common hooks
#

def before_all(context):
    print("> Starting the browser")

    global chrome_options
    global webdriver_wrapper

    if webdriver_wrapper == WebdriverWrapperType.RAW:
        context.driver = webdriver.Chrome(
            #executable_path=CHROME_EXE_PATH,
            chrome_options=chrome_options)
    elif webdriver_wrapper == WebdriverWrapperType.ELEMENTIUM:
        context.driver = SeElements(
            webdriver.Chrome(
                #executable_path=CHROME_EXE_PATH,
                chrome_options=chrome_options))
    elif webdriver_wrapper == WebdriverWrapperType.CAPYBARA:
        if webdriver_headless_mode:
            capybara.current_driver = "selenium_chrome"         # headless
        else:
            capybara.current_driver = "selenium_remote_chrome"  # gui
        capybara.default_max_wait_time = 10
        capybara.current_session().current_window.resize_to(1920, 1080)


def after_all(context):
    print("< Closing the browser")
    if webdriver_wrapper == WebdriverWrapperType.RAW:
        context.driver.close()
        context.driver.quit()
    elif webdriver_wrapper == WebdriverWrapperType.ELEMENTIUM:
        context.driver.browser.quit()
    elif webdriver_wrapper == WebdriverWrapperType.CAPYBARA:
        pass


#---
# underlying selenium drivers
#

@capybara.register_driver("selenium_chrome")
def init_selenium_chrome_driver(app):
    from capybara.selenium.driver import Driver
    global chrome_options
    return Driver(app, browser="chrome",
                  #executable_path=CHROME_EXE_PATH,
                  chrome_options=chrome_options)


@capybara.register_driver("selenium_remote_chrome")
def init_selenium_chrome_driver(app):
    from capybara.selenium.driver import Driver
    return Driver(app, browser="remote",
                  command_executor=remote_chrome_addr,
                  desired_capabilities=DesiredCapabilities.CHROME)
