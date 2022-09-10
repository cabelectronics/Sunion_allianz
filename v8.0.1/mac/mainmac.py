#USERNAME = 'p0010218'
#PSWD = 'Anze020p'
#SINIESTRO1 = '855230428'
#SINIESTRO2 = '587568195'



import os
import subprocess

#subprocess.call('netstat -ano | findstr :5029', creationflags=0x08000000)


import sys
from threading import Thread
#Interaction with GUI
from flask import Flask, request
from flask_cors import CORS

import requests

#GUI Web Browser libraries
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtGui import *
from PyQt5.QtCore import *

#Webdriver library for downloading necessary data from webpage
import webdrivermac2
import random

############################################################################################################
class Interceptor(QWebEngineUrlRequestInterceptor):
    def interceptRequest(self, info):
        info.setHttpHeader(b"Accept-Language", b"en-US,en;q=0.9,es;q=0.8,de;q=0.7")

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(CURRENT_DIR, "public/login.html")


############################################################################################################
PORT_NUMBER = random.randint(1000, 6000)
print(PORT_NUMBER)
new_form = '''
console.log('[System] Forms works!')
$(document).ready(function() 
{
    $('form').on('submit', function(event)
    {
        $.ajax
        (
            {
                data : 
                {
                    
                    //username : $('#username').val(),
                    //username : ('hello')
                    username : $('input[name="username"').val(),
                    password : $('input[name="password"').val(),
                    case : $('input[name="case"').val()
                    
                },
                
                type : 'POST',
                url: 'http:127.0.0.1:'''+str(PORT_NUMBER)+'''/bego',
            }
        );
        console.log('Send succesfully')

        event.preventDefault();

    });
});
'''

form_file = open('public/js/form.js', 'w')
form_file.write(new_form)
form_file.close()



if __name__ == '__main__':

    #QT App Config
    app_ = QApplication(sys.argv)

    app_.setApplicationName("QTπ - Base")
    app_.setOrganizationName("QTπ - Base")
    app_.setApplicationDisplayName("QTπ - Base")
    
    #app_.setWindowIcon(QIcon("public/images/items/base_logo.png"))
    
    browser = QWebEngineView()

    interceptor = Interceptor()
    browser.page().profile().setUrlRequestInterceptor(interceptor)

    
    browser.load(QUrl.fromLocalFile(filename))
    browser.showMaximized()
    ###################################################
    
    #####################
    #Flask and Flask_CORS configuration
    app = Flask(__name__)
    CORS(app, support_credentials=True)

    @app.route('/bego', methods=['POST', 'GET'])
    def bego():
        
        #Get the login data from the HTML
        #Login Data: [Username, Password, Siniestro, Path]
        if request.method == 'POST':
            
            username = request.form['username']
            password = request.form['password']
            siniestro = request.form['case']
            
            
            if bool(username) ==  True:
                print('Data received')
           
            #print('[Data received from Forms]:', username, password, siniestro, file=sys.stderr)
            

            #Open file Dialog
            
            #os.system('python3 path_gui.py')
            #os.system('python path_gui.py')
            #subprocess.call('python3 path_gui.py', creationflags=0x08000000)
            os.system("python3 path_gui.py")

            file_path = open('path.txt', 'r')
            path = file_path.read()
            
            #Your download is starting dialog
            #os.system('python3 UIs/downloading.py')
            #os.system('python UIs/downloading.py')
            #subprocess.call('python3 UIs/downloading.py', creationflags=0x08000000)
            os.system('python3 UIs/downloading.py')
	        

            #Webdriver 
            webdrivermac2.GET_DOCUMENTS(username, password, siniestro, path)

            
            
            return 'wakamole'

            #Si el username o password son incorrectos recibiremos un error
    
        return 'hi'

    kwargs = {'host': '0.0.0.0', 'port': int(PORT_NUMBER), 'threaded': True, 'use_reloader': False, 'debug': False}
    flaskThread = Thread(target=app.run, daemon=True, kwargs=kwargs).start()

    app_.exec()


sys.exit()