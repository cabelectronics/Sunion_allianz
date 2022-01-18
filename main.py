USERNAME = 'p0010218'
PSWD = 'Anze016p'
SINIESTRO = '855230428'


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

webdriver.GET_DOCUMENTS(USERNAME, PSWD, SINIESTRO)