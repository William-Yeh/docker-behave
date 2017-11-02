# -- FILE: features/steps/google_steps.py
import requests
import re
from behave import given, when, then, step
from capybara.dsl import *
from selenium.webdriver.common.keys import Keys


URL_GOOGLE_TW = 'https://www.google.com.tw/?gl=tw'
URL_GOOGLE_TW_SEARCH = 'https://www.google.com.tw/search?gl=tw'


@given('I am on the Google TW page')
def step_impl(context):
    r = requests.get(URL_GOOGLE_TW)
    assert (r.status_code / 100) == 2


@when('I search \'{keyword}\'')
def step_impl(context, keyword):
    payload = {'q': keyword}
    r = requests.get(URL_GOOGLE_TW_SEARCH, params=payload)
    assert (r.status_code / 100) == 2
    # print(r.text)
    context.result_count = count_search_results(r.text)


@then('I can see many results.')
def step_impl(context):
    assert context.failed is False
    print(context.result_count)
    assert len(context.result_count) > 0
    assert context.result_count != 0


#
# invoke with browser...
#

@given(u'I navigate the Google TW page')
def step_impl(context):
    #--> selenium version
    # context.driver.get(URL_GOOGLE_TW)

    #--> elementium version
    # context.driver.navigate(URL_GOOGLE_TW)

    #--> capybara version
    visit(URL_GOOGLE_TW)


@when(u'I summit with \'{keyword}\'')
def step_impl(context, keyword):
    #--> elementium version
    # search_box = context.driver.find('#lst-ib', wait=True)[0]
    # search_box.write(keyword).write(Keys.RETURN)
    # result_text = context.driver.find("#resultStats", wait=True).item.text

    #--> capybara version
    fill_in("lst-ib", keyword)
    # find('[name=btnK]').click
    find("#lst-ib").native.send_keys(Keys.RETURN)
    # save_screenshot("screenshot.png")
    result_text = find("#resultStats").text

    context.result_count = count_search_results(result_text)


def count_search_results(result_text: str) -> str:
    """Count the number of Google search results.

    Args:
        result_text (str): text containing the count string.

    Returns:
        str: The extracted count.
    """
    m = re.search(u'約有\s*([\d\,]+)\s*項結果', result_text)
    return m.group(1)
