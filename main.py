
USERNAME = 'p0010218'
PSWD = 'Anze015p'
SINIESTRO = '855230428'

from selenium import webdriver
import time
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

time.sleep(10)

APL_ALLIANZ_element = driver.find_element_by_xpath('/html/body/div/div/app-root/app-private/app-private-footer/app-footer/footer/nx-footer-navigation/nx-footer-link/app-link')
APL_ALLIANZ_element.click()

time.sleep(5)

bb = driver.find_element_by_xpath('/html/body/div/div/app-root/app-private/app-site-map/div[2]/div[3]/div/mat-tree/mat-tree-node[2]/a')
bb.click()

time.sleep(5)

MAP_element = driver.find_element_by_xpath('/html/body/div/div/app-root/app-private/app-site-map/div[2]/div[3]/div/mat-tree/mat-tree-node[6]/nx-link/a')
MAP_element.click()



