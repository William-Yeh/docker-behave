# Docker image for behave and other Python-based SBE/BDD tools.
#
# URL: https://github.com/William-Yeh/docker-behave
#
# References: 
#   - https://eshlox.net/2016/11/22/dockerize-behave-selenium-tests/
#   - https://gist.github.com/ziadoz/3e8ab7e944d02fe872c3454d17af31a5
#
# Version     1.0.0
#


# pull base image
FROM python:3.6

MAINTAINER William Yeh <william.pjyeh@gmail.com>

ENV CHROME_DRIVER_VERSION 2.33
ENV CHROME_DRIVER_TARBALL http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip

RUN \
    echo "==> Add Google repo for Chrome..."   && \
    wget -q -O- https://dl.google.com/linux/linux_signing_key.pub | apt-key add -  && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/google.list  && \
    \
    \
    echo "==> Install prerequisite stuff..."   && \
    apt-get update            && \
    apt-get install -y           \
        python3-dev              \
        python3-pip              \
        xvfb                     \
        google-chrome-stable  && \
    \
    \
    echo "==> Install ChromeDriver..."   && \
    wget -qO- $CHROME_DRIVER_TARBALL | zcat > /usr/local/bin/chromedriver  && \
    chown root:root /usr/local/bin/chromedriver  && \
    chmod 0755 /usr/local/bin/chromedriver       && \
    \
    \
    echo "==> Install behave and other stuff..."   && \
    pip3 install --no-cache-dir \
        requests                \
        unittest-xml-reporting  \
        nose                    \
        behave                  \
        selenium                \
        elementium              \
        capybara-py             \
        xvfbwrapper



ENV PATH /usr/lib/chromium/:$PATH

WORKDIR    /behave
ENV        REQUIREMENTS_PATH  /behave/features/steps/requirements.txt

COPY       wrapper.sh  /tmp
ENTRYPOINT ["/tmp/wrapper.sh"]
