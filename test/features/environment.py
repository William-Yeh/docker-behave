#
# The environment.py module may define code to run
# before and after certain events during your testing.
#
#
# @see https://behave.readthedocs.io/en/latest/api.html?highlight=environment#environment-file-functions
# @see https://elliterate.github.io/capybara.py/
#

from environment_common import before_all
from environment_common import after_all
from environment_common import init_selenium_chrome_driver
from environment_common import behave_use_capybara
from environment_common import use_headless_mode
from environment_common import set_remote_chrome_addr

print('------------------')
#use_headless_mode(False)
#behave_use_capybara()
#set_remote_chrome_addr('http://127.0.0.1:9515/wd/hub')                 # from host to the same host
#set_remote_chrome_addr('http://docker.for.mac.localhost:9515/wd/hub')  # from Docker container to Mac host
#set_remote_chrome_addr('http://docker.for.win.localhost:9515/wd/hub')  # from Docker container to Windows host