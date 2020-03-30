from selenium.webdriver import Chrome
import time
path = "../driver/chromedriver.exe"
driver=Chrome(executable_path=path)

driver.get("https://www.wikipedia.org/")
driver.maximize_window()

ListOfLang = driver.find_elements_by_xpath("//select[@id='searchLanguage']/option")
print("The total no of Languages: ", len(ListOfLang))

time.sleep(2)
driver.close()

