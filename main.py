USERNAME = 'p0010218'
PSWD = 'Anze019p'
SINIESTRO1 = '855230428'
SINIESTRO2 = '587568195'

import os
import sys

#Interaction with GUI
from flask import Flask, request
from flask_cors import CORS

#GUI Web Browser libraries
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor
from PyQt5.QtWebEngineWidgets import QWebEngineView

#Webdriver library for downloading necessary data from webpage
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

############################################################################################################
class Interceptor(QWebEngineUrlRequestInterceptor):
    def interceptRequest(self, info):
        info.setHttpHeader(b"Accept-Language", b"en-US,en;q=0.9,es;q=0.8,de;q=0.7")

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(CURRENT_DIR, "public/login.html")
print(filename)

############################################################################################################

if __name__ == '__main__':

    #
    app_ = QApplication(sys.argv)

    app_.setApplicationName("Mission Software SVP Aerospace")
    app_.setOrganizationName("SVP Aerospace")
    app_.setApplicationDisplayName("Mission Software SVP Aerospace")
    
    app_.setWindowIcon(QIcon("public/images/items/svp_logo.png"))
    
    browser = QWebEngineView()

    interceptor = Interceptor()
    browser.page().profile().setUrlRequestInterceptor(interceptor)

    
    browser.load(QUrl.fromLocalFile(filename))
    browser.showMaximized()

    
    #####################
    #Flask and Flask_CORS configuration
    app = Flask(__name__)
    CORS(app, support_credentials=True)

    @app.route('/bego', methods=["POST", "GET"])
    def bego():
        
        #Get the login data from the HTML
        #Login Data: [Username, Password, Siniestro, Path]
        if request.method == 'POST':
            
            username = request.form['username']
            password = request.form['password']
            if bool(username) ==  True:
                pass
            #siniestro
            print('[Data received from Forms]:', username, password)
            #Tenemos ya todo


            #Webdriver 
            webdriver.GET_DOCUMENTS(USERNAME, PSWD, SINIESTRO)
            
            #Si el username o password son incorrectos recibiremos un error
    


    app_.exec()

sys.exit()