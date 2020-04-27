from selenium import webdriver


driver = webdriver.Chrome("D:\PycharmProjects\SPSAutomation\BrowserDrivers\chromedriver.exe")
driver.implicitly_wait(10000)
driver.get("https://wet-boew.github.io/v4.0-ci/demos/tables/tables-en.html")



lt = driver.find_elements_by_xpath("//*[@id='wb-auto-1']/tbody/tr").__sizeof__()
#print(lt.__len__())
print(lt)

