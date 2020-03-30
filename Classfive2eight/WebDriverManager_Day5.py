from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = Chrome(ChromeDriverManager().install())

driver.get("https://www.wikipedia.org/")
driver.maximize_window()

ListOfLang = driver.find_elements_by_xpath("//select[@id='searchLanguage']/option")
print("The total no of Languages: ", len(ListOfLang))

empty = []

for ref in ListOfLang:
    empty.append(ref.text)

print("Before sort: ",empty)
empty.sort()
print("After sort: ",empty)

time.sleep(2)
driver.close()
