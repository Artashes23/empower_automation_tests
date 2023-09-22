
from ast import Constant
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.remote_connection import RemoteConnection
from webdriver_manager.microsoft import  EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as Edge_Options
from webdriver_manager.opera import OperaDriverManager
import json
import requests
from selenium.webdriver.chrome.service import Service as ChromeService





def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")

chromedriver_path = "/usr/local/bin/chromedriver"
@pytest.fixture
def setup():
    chrome_options = Options()
    chrome_options.binary_location = "/usr/bin/google-chrome"
    chrome_options.add_argument("--capture=no")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("window-size=1920,1200")
    chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--no-sandbox")
    #chrome_options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
        
    
    yield browser
    browser.quit()

"""def pytest_addoption(parser):
    parser.addoption("--browser",action = "store", default = "chrome")

executable_path=ChromeDriverManager().install(),options = chrome_options
version="114.0.5735.90"
        
    
@pytest.fixture
def getBrowser(request):
    _browser = request.config.getoption("--browser")
    return _browser

@pytest.fixture
def new_browser(request,getBrowser):
    _driver = None
    print(getBrowser)
    if getBrowser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--capture=no")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--start-maximized")
        _driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options = chrome_options)
    elif getBrowser == "edge":
        edge_options = Edge_Options()  
        edge_options.add_argument("start-maximized")  
        _driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install(),options = edge_options)
    request.driver = _driver
    yield _driver"""

    
    




