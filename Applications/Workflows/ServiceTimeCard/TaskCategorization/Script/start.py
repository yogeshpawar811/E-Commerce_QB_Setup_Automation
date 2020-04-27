from selenium import webdriver

Browser = webdriver.Chrome("D:/all desktop/SPS_Automation/BrowserDrivers/chromedriver.exe")
Browser.maximize_window()
Browser.get("http://www.google.com")
Browser.find_element_by_xpath("//*[@id='gbw']/div/div/div[1]/div[1]/a").click()

