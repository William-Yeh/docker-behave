Docker image for Python-based SBE/BDD tools
===


[![Circle CI](https://circleci.com/gh/William-Yeh/docker-behave.svg?style=shield)](https://circleci.com/gh/William-Yeh/docker-behave) [![Build Status](https://travis-ci.org/William-Yeh/docker-behave.svg?branch=master)](https://travis-ci.org/William-Yeh/docker-behave)


## Summary

Repository name in Docker Hub: **[williamyeh/behave](https://hub.docker.com/r/williamyeh/behave/)**

This repository contains Dockerized Python tools for SBE/BDD, published to the public [Docker Hub](https://hub.docker.com/) via **automated build** mechanism.


## Configuration

This docker image contains the following software stack:

- Base image: Debian jessie + [Python 3](https://hub.docker.com/_/python/).

- [Behave](https://pypi.python.org/pypi/behave): behavior-driven development, Python style.

- [Selenium WebDriver](http://www.seleniumhq.org/projects/webdriver/): a suite of tools to automate web browsers across many platforms.

- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/): a standalone server which implements WebDriver's wire protocol for Chromium.

- Selenium wrapper for Python:
  - [Elementium](https://github.com/actmd/elementium): jQuery-style syntactic sugar for Selenium.
  - [Capybara](https://elliterate.github.io/capybara.py/): a port of [Capybara from Ruby](https://en.wikipedia.org/wiki/Capybara_(software)).



## Usage


**Given** a `features` sub-directory as follows:

```
.
└── features
    ├── environment.py
    ├── requirements.txt
    ├── xxx.feature
    ├── yyy.feature
    └── steps
        ├── xxx_step.py
        └── yyy_step.py
```

**When** I invoke the program as follows:

```
$ docker run -it --rm -v "$(pwd):/behave:ro"  williamyeh/behave
```

**Then** I can see the output as follows:

```
Feature: ...
[...]
1 feature passed, 0 failed, 0 skipped
7 scenarios passed, 0 failed, 0 skipped
21 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m11.532s
```


Note: `requirements.txt` in `features` directory.



## TODO

1. Browser in GUI mode.
2. Detailed document.
4. Firefox?
5. Flow with Jenkins.



## Tutorial

*Behave*

 - [Behave tutorial](https://pythonhosted.org/behave/tutorial.html)


*Selenium*

- https://intoli.com/blog/running-selenium-with-headless-chrome/


*Elementium*





*Capybara*




## License

Author: William Yeh <william.pjyeh@gmail.com>

Licensed under the Apache License V2.0. See the [LICENSE file](LICENSE) for details.
