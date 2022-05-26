USERNAME = 'p0010218'
PSWD = 'Anze019p'
SINIESTRO1 = '855230428'
SINIESTRO2 = '587568195'

#Interaction with GUI
from flask import Flask, request
from flask_cors import CORS

#GUI Web Browser libraries
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

#Webdriver libraries for downloading necessary data from webpage
import webdriver

print('Seleccione Siniestro:')
print('1: 855230428')
print('2: 587568195')
siniestro_entry = input('> ')

if siniestro_entry == '1':
    SINIESTRO = SINIESTRO1
else:
    SINIESTRO = SINIESTRO2

print('Loading...')

if __name__ == '__main__':

    #
    app_ = QApplication(sys.argv)

    app_.setApplicationName("Qtπ")
    app_.setOrganizationName("Base")
    app_.setApplicationDisplayName("Qtπ - Base")

    browser = QWebEngineView()

    interceptor = Interceptor()
    browser.page().profile().setUrlRequestInterceptor(interceptor)

    webdriver.GET_DOCUMENTS(USERNAME, PSWD, SINIESTRO)