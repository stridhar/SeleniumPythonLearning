from selenium.webdriver import Chrome
import time
path = "D:\python\chromedriver.exe"
driver = Chrome(executable_path=path)

driver.get("https://www.wikipedia.org/")
driver.maximize_window()

listOfLang = driver.find_elements_by_xpath("//select[@id='searchLanguage']/option")
print("Total no of Lang: ", len(listOfLang))
time.sleep(2)
driver.close()

