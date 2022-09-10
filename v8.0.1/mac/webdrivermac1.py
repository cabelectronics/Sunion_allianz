#Work with web Pages & SELENIUM
from lib2to3.pgen2.token import OP
from pickle import FALSE, TRUE
from tkinter import N
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import subprocess
import time
import json
import os
import shutil
import base64
from pathlib import Path
from webdriver_manager.chrome import ChromeDriverManager

#NEW NEW Chrome settings
options = Options()

#needed option setting for working
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument("--disable-extensions")
options.add_argument('--disable-dev-shm-usage')    
options.add_argument("--disable-gpu")
options.add_argument('--disable-software-rasterizer')
options.add_argument("--disable-notifications")
options.add_argument("--safebrowsing-disable-download-protection")
options.add_argument("disable-infobars")
options.add_argument("--safebrowsing-disable-extension-blacklist")


#Save Webpage as HTML
settings = {
       "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2
    }

dwn_path = os.getcwd()
dwn_path = dwn_path + '\downloads'
print(dwn_path)

prefs = {   
            "safebrowsing.enabled": True,
            'printing.print_preview_sticky_settings.appState': json.dumps(settings),
            "download.default_directory": dwn_path,
            "download.prompt_for_download": True,
            'download.extensions_to_open': 'eml',
            

            #"safebrowsing_for_trusted_sources_enabled": False,
            
        }
#prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings), "download.default_directory":"C:\Tutorial\down"}
options.add_experimental_option('prefs', prefs)
options.add_argument('--kiosk-printing')




def GET_DOCUMENTS(USERNAME, PSWD, SINIESTRO, PATH):
    #driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=Options)
    service = Service(ChromeDriverManager().install())
    

    driver = webdriver.Chrome(service=service,options=options)

    driver.get('https://www.e-pacallianz.com/ngx-epac-professional/public/home')
    #driver.fullscreen_window()
    

    USR_element = driver.find_element_by_name("username")
    USR_element.send_keys(USERNAME)

    PSWD_element = driver.find_element_by_name("password")
    PSWD_element.send_keys(PSWD)

    LGIN_element = driver.find_element_by_xpath("/html/body/div/div/app-root/app-public/app-public-home/div/div/div/app-login/div/form/div[2]/div/button")
    LGIN_element.click()

    #if gets error --> send gui error with credentials

    def WaitUntilFind(form, locator):
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((form, locator))
            )
            print("finded")
            return True
        except:
            print("not finded")
            return False


    
    try:
        WaitUntilFind(By.XPATH, "/html/body/div/div/app-root/app-private/app-private-footer/app-footer/footer/nx-footer-navigation/nx-footer-link/app-link")
        APL_ALLIANZ_element = driver.find_element_by_xpath('/html/body/div/div/app-root/app-private/app-private-footer/app-footer/footer/nx-footer-navigation/nx-footer-link/app-link')
        APL_ALLIANZ_element.click()
    except:
        os.system('python3 UIs/invalid.py')

    #Finding MAP sometimes gives error, that's why it's triplicated.
    print('Searching for MAP')
    WaitUntilFind(By.XPATH, "/html/body/div/div/app-root/app-private/app-site-map/div[2]/div[3]/div/mat-tree/mat-tree-node[2]/a")
    #WaitUntilFind(By.XPATH, "/html/body/div/div/app-root/app-private/app-site-map/div[2]/div[3]/div/mat-tree/mat-tree-node[2]/a")
    #WaitUntilFind(By.XPATH, "/html/body/div/div/app-root/app-private/app-site-map/div[2]/div[3]/div/mat-tree/mat-tree-node[2]/a")
    MAP_SEARCH = WaitUntilFind(By.XPATH, "/html/body/div/div/app-root/app-private/app-site-map/div[2]/div[3]/div/mat-tree/mat-tree-node[2]/a")
    if MAP_SEARCH == False:
        print('MAP not found Reloading page')
        driver.refresh()
    else:
        print('Map not found') #Display alert to user
        
   
    
    WaitUntilFind(By.XPATH, "/html/body/div/div/app-root/app-private/app-site-map/div[2]/div[3]/div/mat-tree/mat-tree-node[2]/a")
    print('MAP Founded')
    

    MAP_element = driver.find_element_by_xpath('/html/body/div/div/app-root/app-private/app-site-map/div[2]/div[3]/div/mat-tree/mat-tree-node[2]/a')
    MAP_element.click()

    WaitUntilFind(By.XPATH, "/html/body/div/div/app-root/app-private/app-site-map/div[2]/div[3]/div/mat-tree/mat-tree-node[6]/nx-link/a")


    PLAT_element = driver.find_element_by_xpath('/html/body/div/div/app-root/app-private/app-site-map/div[2]/div[3]/div/mat-tree/mat-tree-node[6]/nx-link/a')
    PLAT_element.click()

    WaitUntilFind(By.XPATH, "/html/body/div/div/app-root/app-private/app-application-launch/div[2]/app-iframe-application/div/iframe")
   
    #SINIESTRO FRAME
    iframe = driver.find_element_by_xpath('/html/body/div/div/app-root/app-private/app-application-launch/div[2]/app-iframe-application/div/iframe')
    driver.switch_to.frame(iframe)
    SINIESTRO_ENTRY_element = driver.find_element_by_id('claimNumber')
    SINIESTRO_ENTRY_element.click()
    
    SINIESTRO_ENTRY_element.send_keys(SINIESTRO)
    ENVIAR_element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/table/tbody/tr[1]/td/form[1]/div[1]/div/table/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr/td[2]/div')
    ENVIAR_element.click()

    WaitUntilFind(By.ID, "ordersList_0_0")

    ESTADO_element = driver.find_element_by_id("ordersList_0_0")
    ESTADO_element.click()

    WaitUntilFind(By.XPATH, '//*[@id="FG"]/div[1]')

    FICHAGESTION_element = driver.find_element_by_xpath('//*[@id="FG"]/div[1]')
    FICHAGESTION_element.click()
    
    ##################################
    #Switch TAB
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])

    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "row_0_llistadades"))
        )
        print("swithced")
    except:
        time.sleep(10)
        driver.switch_to.window(driver.window_handles[1])
        print("not switched")

    #Already Switched
    ##################################
    i=-1
    n=1
    
    while True:
        if n == 1:
            pass
        elif n == 0:
            print("done")
            print(i)
            break
            
        print(i)
        i = i + 1
        id = 'row_'+ str(i) +'_llistadades'
        #llistadadesWM_1_0
        
        DOCUMENT_ELEMENTS = WaitUntilFind(By.ID, str(id))
        #llistadadesWM_1_0
        if DOCUMENT_ELEMENTS == False:
            print('Another page?')
            #look for another page
            
        
            NEW_PAGE = WaitUntilFind(By.XPATH, '//*[@id="o_4" and @class="sectionButton"]')
            if NEW_PAGE == True :
                RENAME_I= WaitUntilFind(By.XPATH, '//*[@id="ListaSectionBar"]/table/tbody/tr/td/table/tbody/tr/td[2]')
                OPEN_NEW = driver.find_element_by_xpath('//*[@id="ListaSectionBar"]/table/tbody/tr/td/table/tbody/tr/td[2]')
                OPEN_NEW.click()
                if RENAME_I == True:
                    i = -1
                n=1
                print('downloading next page') 
                continue
                
            elif NEW_PAGE == False:
                n=0
            
        print(id)
        if i == -1:
            print("broken")
            continue
        else:
            print("im here")
            





#'//*[@id="o_4" and @class="sectionButton"'