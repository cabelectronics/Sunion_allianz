
USERNAME = 'p0010218'
PSWD = 'Anze015p'
SINIESTRO = '855230428'

from selenium import webdriver

options = webdriver.ChromeOptions()
#options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=options)
#driver.get('https://www.e-pacallianz.com/ngx-epac-professional/public/home')
driver.get("https://www.e-pacallianz.com/ngx-epac-professional/private/home#:~:text=Aplic.-,Allianz,-Encargos%20Proveedores%20Allianz")

USR_element = driver.find_element_by_name("username")
USR_element.send_keys(USERNAME)

PSWD_element = driver.find_element_by_name("password")
PSWD_element.send_keys(PSWD)

LGIN_element = driver.find_element_by_xpath("/html/body/div/div/app-root/app-public/app-public-home/div/div/div/app-login/div/form/div[2]/div/button")
LGIN_element.click()


#APL_ALLIANZ_element = driver.fi("/html/body/div/div/app-root/app-private/app-private-header/div/nx-extended-navigation/div/div[1]/nx-extended-navigation-desktop/div[1]/div/div/ul/li[2]/a/span")
#APL_ALLIANZ_element.click()







