
USERNAME = 'p0010218'
PSWD = 'Anze015p'

from selenium import webdriver

options = webdriver.ChromeOptions()
#options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=options)
driver.get('http://www.google.com')
print(driver.title)