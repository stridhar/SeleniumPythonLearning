from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

data={"url":"https://www.google.co.in","browser":"chrome","search":"Selenium jobs"}
if data["browser"]=="chrome":
    path = "../driver/chromedriver.exe"
    driver = Chrome(executable_path=path)
driver.maximize_window()
driver.get(data["url"])
driver.find_element_by_name("q").send_keys(data["search"],Keys.ENTER)
driver.close()


