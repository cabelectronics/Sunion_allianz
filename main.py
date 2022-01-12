
USERNAME = 'p0010218'
PSWD = 'Anze015p'
SINIESTRO = '855230428'

from selenium import webdriver

options = webdriver.ChromeOptions()
#options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.e-pacallianz.com/ngx-epac-professional/public/home')


USR_element = driver.find_element_by_name("username")
USR_element.send_keys(USERNAME)

PSWD_element = driver.find_element_by_name("password")
PSWD_element.send_keys(PSWD)

LGIN_element = driver.find_element_by_xpath("/html/body/div/div/app-root/app-public/app-public-home/div/div/div/app-login/div/form/div[2]/div/button")
LGIN_element.click()

APL_ALLIANZ_element = driver.find_element_by_name('Aplic. Allianz')
APL_ALLIANZ_element.click()







