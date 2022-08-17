# Python + Selenium Test Project

Project created to test a simple web application using Python + Selenium and PyTest as a test framework using the Google Chrome browser

# Prerequisites

This project uses Python 3.10.6 and PIP 22.2.1 in order to run the tests

## Python
Python can be download [here](https://www.python.org/downloads/)

## PIP
Usually, PIP comes with the Python default installation from python.org, if for some reason you do not have PIP installed when installing Python, you can install it from [here](https://pip.pypa.io/en/stable/installation/)

## Requirements

In order to run the tests, Selenium, PyTest and PyTest html report need to be installed. They can be installed using PIP:
```
git clone https://github.com/BrunoFBarbosa/python-selenium.git
cd python-selenium
pip install -r requirements.txt
```

## Chromedriver
Chromedriver needs to be download depending on your google chrome installation, more info [here](https://chromedriver.chromium.org/downloads)

After the download, edit the utils/constants.py file to reflect your chromedriver location, for example:

```
CHROME_DRIVER_PATH = "/home/user/downloads/chromedriver"
```

# Running The Tests

The tests can be executed using the PyTest command:
```
pytest file.py
```

You can also generate a html report using the --html flag and specifing the file path to be saved
```
pytest file.py --html=report.html
```
