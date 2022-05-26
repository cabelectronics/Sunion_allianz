#Work with web Pages & SELENIUM
from threading import current_thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import json
import sys
import os
import shutil
import glob
import base64
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
prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings),
            "download.default_directory": "downloads",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False}
#prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings), "download.default_directory":"C:\Tutorial\down"}
options.add_experimental_option('prefs', prefs)
options.add_argument('--kiosk-printing')

options.add_argument("--headless")

def GET_DOCUMENTS(USERNAME, PSWD, SINIESTRO):
    #driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=Options)
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

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


    WaitUntilFind(By.XPATH, "/html/body/div/div/app-root/app-private/app-private-footer/app-footer/footer/nx-footer-navigation/nx-footer-link/app-link")


    APL_ALLIANZ_element = driver.find_element_by_xpath('/html/body/div/div/app-root/app-private/app-private-footer/app-footer/footer/nx-footer-navigation/nx-footer-link/app-link')
    APL_ALLIANZ_element.click()

    #Finding MAP sometimes gives error, that's why it's triplicated.
    print('Searching for MAP')
    WaitUntilFind(By.XPATH, "/html/body/div/div/app-root/app-private/app-site-map/div[2]/div[3]/div/mat-tree/mat-tree-node[2]/a")
    WaitUntilFind(By.XPATH, "/html/body/div/div/app-root/app-private/app-site-map/div[2]/div[3]/div/mat-tree/mat-tree-node[2]/a")
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
    
    
    while True:
        i = i + 1
        id = 'row_'+ str(i) +'_llistadades'
        #llistadadesWM_1_0
        print(str(id))
        
        DOCUMENT_ELEMENTS = WaitUntilFind(By.ID, str(id))
        if DOCUMENT_ELEMENTS == False:
            print('Proccess Finished')
            break
        a_element = driver.find_element_by_id(str(id))
        

        DOCUMENT_NAME = a_element.text
        print('Document Name:', DOCUMENT_NAME)
        a_element.click()
        try:
            b_element = driver.find_element_by_id(str(id))
            b_element.click()
        except:
            pass
        
        #Si no es un autodescargable y ahi que descargarlo como PDF:
            
        if WaitUntilFind(By.XPATH, '//*[@id="sectionVariable"]/table/tbody/tr[1]/td/table/tbody/tr/td[2]') ==  True:
            print('Trying to save as PDF')
            #driver.execute_script("window.print();")
            pdf = driver.execute_cdp_cmd("Page.printToPDF", {
            "printBackground": True
            })

            

            with open("downloads/fichero.pdf", "wb") as f:
                f.write(base64.b64decode(pdf['data']))

        else:
            print('Second type download not founded')
            pass
            
            
        #time.sleep(3)
        #driver.back()
        driver.execute_script("window.history.go(-1)")
        
        
        time.sleep(3)
        source_dir = 'downloads'
        target_dir = 'download_2'
            
        file_names = os.listdir(source_dir)
        print(file_names)
        for file_name in file_names:
            shutil.move(os.path.join(source_dir, file_name), target_dir)
        
        #Rename file in the new directory
        
        new_file_name_pdf = 'download_2/Fichero_' + str(i) + '.PDF'
        new_file_name_eml = 'download_2/Fichero_' + str(i) + '.EML'
        new_file_name_html = 'download_2/Fichero_' + str(i) + '.HTML'
        try:
            os.rename('download_2/fichero.PDF', new_file_name_pdf)
            print('Renaming PDF file...')
        except:
            try:
                os.rename('download_2/fichero.EML', new_file_name_eml)
                print('Renaming EML file...')
            except:
                try:
                    os.rename('download_2/ficher.HTML', new_file_name_html)
                    print('Renaming HTML file...')
                except:
                    print('Format not COMPATIBLE')
                    pass

        print('Process finished')
        
        
    
    #a_element = driver.find_element_by_id('row_1_llistadades')
    #a_element.click()
    #time.sleep(3)
    #driver.execute_script('window.print();')


    #Descarga automatica de ficheros
    #archivo_random_element = driver.find_element_by_id('row_0_llistadades')
    #archivo_random_element.click()

    