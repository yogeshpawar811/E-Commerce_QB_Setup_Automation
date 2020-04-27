from Applications.Workflows.QBSetup.AppResources import ElementLocators
from selenium import webdriver
import time

from selenium import webdriver


v_Browser = webdriver.Chrome("C:\SpsAutomation\SPS_Automation - QB Setup\BrowserDrivers\chromedriver.exe")
v_Browser.maximize_window()
v_Browser.get("http://www.google.com")

time.sleep(100)