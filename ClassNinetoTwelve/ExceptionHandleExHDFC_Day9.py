from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

path = "../driver/chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("https://www.hdfcbank.com/")
driver.maximize_window()
driver.implicitly_wait(10)
try:
    driver.find_element_by_xpath("//a[@id='popupBoxClose']").click()
    print("Pop up appeared and closed")
except:
    print("pop up not appeared")
driver.find_element_by_xpath("(//button[@type='button' and text()='Login'])[2]").click()





