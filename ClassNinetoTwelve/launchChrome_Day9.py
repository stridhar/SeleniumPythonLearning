from selenium.webdriver import Chrome,ChromeOptions

path="../driver/chromedriver.exe"

ops=ChromeOptions()
ops.add_argument('--ignore--certificate-errors')
ops.add_argument("--disable--notifications")
driver=Chrome(executable_path=path,options=ops)
driver.fullscreen_window()
