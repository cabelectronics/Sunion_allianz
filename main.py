USERNAME = 'p0010218'
PSWD = 'Anze019p'
SINIESTRO1 = '855230428'
SINIESTRO2 = '587568195'

<<<<<<< HEAD
driver = webdriver.Chrome(chrome_options=options)
#driver.get('https://www.e-pacallianz.com/ngx-epac-professional/public/home')
driver.get("https://www.e-pacallianz.com/ngx-epac-professional/private/home#:~:text=Aplic.-,Allianz,-Encargos%20Proveedores%20Allianz")
=======
#Interaction with GUI
from flask import Flask, request
from flask_cors import CORS

#GUI Web Browser libraries
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
>>>>>>> f63adfb5ec816c2992a5375d67c11ea029d5ccbf

#Webdriver libraries for downloading necessary data from webpage
import webdriver

<<<<<<< HEAD
print('Seleccione Siniestro:')
print('1: 855230428')
print('2: 587568195')
siniestro_entry = input('> ')

if siniestro_entry == '1':
    SINIESTRO = SINIESTRO1
else:
    SINIESTRO = SINIESTRO2

print('Loading...')

webdriver.GET_DOCUMENTS(USERNAME, PSWD, SINIESTRO)
=======
<<<<<<< HEAD
PSWD_element = driver.find_element_by_name("password")
PSWD_element.send_keys(PSWD)

LGIN_element = driver.find_element_by_xpath("/html/body/div/div/app-root/app-public/app-public-home/div/div/div/app-login/div/form/div[2]/div/button")
LGIN_element.click()

<<<<<<< HEAD

#APL_ALLIANZ_element = driver.fi("/html/body/div/div/app-root/app-private/app-private-header/div/nx-extended-navigation/div/div[1]/nx-extended-navigation-desktop/div[1]/div/div/ul/li[2]/a/span")
#APL_ALLIANZ_element.click()
=======
time.sleep(10)

APL_ALLIANZ_element = driver.find_element_by_xpath('/html/body/div/div/app-root/app-private/app-private-footer/app-footer/footer/nx-footer-navigation/nx-footer-link/app-link')
APL_ALLIANZ_element.click()
>>>>>>> a1d6782bf99233918fdd90d52d9334831f03c9af

time.sleep(5)

MAP_element = driver.find_element_by_xpath('/html/body/div/div/app-root/app-private/app-site-map/div[2]/div[3]/div/mat-tree/mat-tree-node[2]/a')
MAP_element.click()

time.sleep(5)

PLAT_element = driver.find_element_by_xpath('/html/body/div/div/app-root/app-private/app-site-map/div[2]/div[3]/div/mat-tree/mat-tree-node[6]/nx-link/a')
PLAT_element.click()

time.sleep(20)

SINTRO_element = driver.find_element_by_id('claimNumber.input-text')
SINTRO_element.send_keys(SINIESTRO)

ENVIAR_element = driver.find_element_by_id("0_10")
ENVIAR_element.click()

print("FINISH")
=======
webdriver.GET_DOCUMENTS(USERNAME, PSWD, SINIESTRO)
>>>>>>> f63adfb5ec816c2992a5375d67c11ea029d5ccbf
>>>>>>> 4f41647e521d62c0e9518c741b4538fa28061d60
