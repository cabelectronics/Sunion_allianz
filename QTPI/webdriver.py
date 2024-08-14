#Work with web Pages & SELENIUM

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
import subprocess
import time
import json
import os
import sys
import shutil
import base64
from pathlib import Path
from webdriver_manager.chrome import ChromeDriverManager
import glob


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

options.add_argument("--headless")

def GET_DOCUMENTS(USERNAME, PSWD, SINIESTRO, PATH):
    #driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=Options)
    service = Service(ChromeDriverManager().install())
    service.creationflags = CREATE_NO_WINDOW

    driver = webdriver.Chrome(service=service,options=options)

    driver.get('https://www.e-pacallianz.com/ngx-epac-professional/public/home')
    #driver.fullscreen_window()
    

    #USR_element = driver.find_element_by_name("username")
    USR_element = driver.find_element(By.NAME, "username")
    USR_element.send_keys(USERNAME)

    #PSWD_element = driver.find_element_by_name("password")
    PSWD_element = driver.find_element(By.NAME, "password")
    PSWD_element.send_keys(PSWD)

    LGIN_element = driver.find_element(By.XPATH,"/html/body/div/div/app-root/app-public/app-public-home/div/div/div/app-login/div/form/div[2]/div/button")
    LGIN_element.click()

    #if gets error --> send gui error with credentials

    def WaitUntilFind(form, locator):
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((form, locator))
            )
            print("found")
            return True
        except:
            print("not found")
            return False


    
    try:
        WaitUntilFind(By.XPATH, "/html/body/div/div/app-root/app-private/app-private-footer/app-footer/footer/nx-footer-navigation/nx-footer-link/app-link")
        APL_ALLIANZ_element = driver.find_element(By.XPATH, '/html/body/div/div/app-root/app-private/app-private-footer/app-footer/footer/nx-footer-navigation/nx-footer-link/app-link')
        APL_ALLIANZ_element.click()
    except:
        subprocess.call('UIs/Invalid/dist/invalid/invalid.exe', creationflags=0x08000000)

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
    print('MAP Found')
    

    MAP_element = driver.find_element(By.XPATH, '/html/body/div/div/app-root/app-private/app-site-map/div[2]/div[2]/div/nx-link[1]')
    MAP_element.click()

    WaitUntilFind(By.XPATH, "/html/body/div/div/app-root/app-private/app-site-map/div[2]/div[3]/div/mat-tree/mat-tree-node[6]/nx-link/a")


    PLAT_element = driver.find_element(By.XPATH,'/html/body/div/div/app-root/app-private/app-site-map/div[2]/div[3]/div/mat-tree/mat-tree-node[5]/nx-link/a')
    PLAT_element.click()

    WaitUntilFind(By.XPATH, "/html/body/div/div/app-root/app-private/app-application-launch/div[2]/app-iframe-application/div/iframe")
   
    #SINIESTRO FRAME
    iframe = driver.find_element(By.XPATH,'/html/body/div/div/app-root/app-private/app-application-launch/div[2]/app-iframe-application/div/iframe')
    driver.switch_to.frame(iframe)
    SINIESTRO_ENTRY_element = driver.find_element(By.ID,'claimNumber')
    SINIESTRO_ENTRY_element.click()
    
    SINIESTRO_ENTRY_element.send_keys(SINIESTRO)
    ENVIAR_element = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/table/tbody/tr[1]/td/form[1]/div[1]/div/table/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr/td[2]/div')
    ENVIAR_element.click()

    WaitUntilFind(By.ID, "ordersList_0_0")

    ESTADO_element = driver.find_element(By.ID,"ordersList_0_0")
    ESTADO_element.click()

    WaitUntilFind(By.XPATH, '//*[@id="FG"]/div[1]')

    FICHAGESTION_element = driver.find_element(By.XPATH,'//*[@id="FG"]/div[1]')
    FICHAGESTION_element.click()
    
    ##################################
    #Switch TAB
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])

    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "row_0_llistadades"))
        )
        print("switched")
    except:
        time.sleep(10)
        driver.switch_to.window(driver.window_handles[1])
        print("not switched")

    ###################################################################################
    #Clean /downloads folder just in case previous download didn't finish
    #Delete content of downloads

    #get current directory and select target directory
    downloads_cwd = os.getcwd()

    src_path = str(downloads_cwd) + '/downloads'
    

    folder = src_path
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    ###################################################################################
    ###################################################################################
    #Clean /download_2 folder just in case previous download didn't finish
    #Delete content of downloads

    #get current directory and select target directory
    download_2_cwd = os.getcwd()

    src_path = str(download_2_cwd) + '/download_2'
    

    folder = src_path
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    ###################################################################################



    #Already Switched
    ##################################
    
    LLISTADADES_NUMBER = -1
    FILA_FILE_NUMBER = 0
    LLISTADADES_TOTAL_NUMBER = -1
    while True:
        

        LLISTADADES_NUMBER = LLISTADADES_NUMBER + 1
        LLISTADADES_TOTAL_NUMBER = LLISTADADES_TOTAL_NUMBER + 1
        
        time.sleep(3)
        VER_MAS1_element =  WaitUntilFind(By.XPATH, "/html/body/div[1]/div/app-root/file-management/app-listfilemanagement/div/div/div[1]/app-ngx-load-more/div/div/div/button")
        while VER_MAS1_element == True:
            try:
                VER_MAS_element = driver.find_element(By.XPATH,'/html/body/div[1]/div/app-root/file-management/app-listfilemanagement/div/div/div[1]/app-ngx-load-more/div/div/div/button')
                VER_MAS_element.click()
            except:
                try:
                    time.sleep(3)
                    VER_MAS_element = driver.find_element(By.XPATH,'/html/body/div[1]/div/app-root/file-management/app-listfilemanagement/div/div/div[1]/app-ngx-load-more/div/div/div/button')
                    VER_MAS_element.click()
                except:
                    pass

            VER_MAS1_element =  WaitUntilFind(By.XPATH, "/html/body/div[1]/div/app-root/file-management/app-listfilemanagement/div/div/div[1]/app-ngx-load-more/div/div/div/button")

        print('LLISTADADES_NUMBER:' + str(LLISTADADES_NUMBER))
        print('LLISTADADES_TOTAL_NUMBER:' + str(LLISTADADES_TOTAL_NUMBER))
        #id = 'row_'+ str(i) +'_llistadades'
        id = 'filaFile_' + str(FILA_FILE_NUMBER) +'_'+ str(LLISTADADES_NUMBER)
        print("The ID searching for is:", str(id))
        DOCUMENT_ELEMENTS = WaitUntilFind(By.ID, str(id))
        


        if DOCUMENT_ELEMENTS == False:
            FILA_FILE_NUMBER = FILA_FILE_NUMBER + 1
            LLISTADADES_NUMBER = 0
            id = 'filaFile_' + str(FILA_FILE_NUMBER) +'_'+ str(LLISTADADES_NUMBER)
            print(id)
            DOCUMENT_ELEMENTS = WaitUntilFind(By.ID, str(id))
            LLISTADADES_NUMBER = -1


        if DOCUMENT_ELEMENTS == False and LLISTADADES_NUMBER:
            break

        else:
            #Replace INAVILD Windows/Linux/MAC OS ASCII characters for folders and files
            INVALID1_id_name = driver.find_element(By.ID, id)
            INVALID_id_name = INVALID1_id_name.find_elements(By.TAG_NAME, 'td')[3].text
            id_name = str(INVALID_id_name).replace(':', '')
            id_name = str(id_name).replace('<', '')
            id_name = str(id_name).replace('/', '')
            id_name = str(id_name).replace('>', '')
            id_name = str(id_name).replace('"', '')
            id_name = str(id_name).replace("'\'", '')
            id_name = str(id_name).replace('|', '')
            id_name = str(id_name).replace('?', '')
            id_name = str(id_name).replace('*', '')
            id_name = id_name + '_' + str(LLISTADADES_TOTAL_NUMBER)
            print(id_name)


            WaitUntilFind(By.ID, str(id))
            #a_element.click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, str(id)))).click()
            #A veces no hace click en el a la primera, por eso lo intentamos varias veces
            '''try:
                b_element = driver.find_element(By.ID,str(id))
                b_element.click()
                
                print("DOUBLE CLICKED")
                try:
                    b_element = driver.find_element(By.ID,str(id))
                    b_element.click()
                    print("triple clicked")
                except:
                    try:
                        b_element = driver.find_element(By.ID,str(id))
                        b_element.click()
                        print("Cuatriple clicked")
                    except:
                        pass
            except:
                pass '''
            print("CLICKED")

            time.sleep(3) 

            ACCESO_DETALLE_element1=WaitUntilFind(By.XPATH, "/html/body/div[1]/div/app-root/file-management/app-listfilemanagement/div/div/div[2]/nx-tab-group/div/nx-tab-body/div/div[6]/div/button")
            while ACCESO_DETALLE_element1 == False:
                time.sleep(3)
                ACCESO_DETALLE_element1=WaitUntilFind(By.XPATH, "/html/body/div[1]/div/app-root/file-management/app-listfilemanagement/div/div/div[2]/nx-tab-group/div/nx-tab-body/div/div[6]/div/button")
            ACCESO_DETALLE_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/app-root/file-management/app-listfilemanagement/div/div/div[2]/nx-tab-group/div/nx-tab-body/div/div[6]/div/button")
            ACCESO_DETALLE_element.click()
            #Si no es un autodescargable y ahi que descargarlo como PDF:    
            if WaitUntilFind(By.XPATH, '//*[@id="sectionVariable"]/table/tbody/tr[1]/td/table/tbody/tr/td[2]') ==  True:
                print('No es autodescargable')
                print('Saving as PDF')
                #driver.execute_script("window.print();")
                frame = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/table/tbody/tr[1]/td/form[1]/div[3]/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/textarea')
                text_content = frame.text

                with open("downloads/" + str(id_name) + ".txt", "w") as f:
                    f.write(text_content)
                
            
            elif WaitUntilFind(By.XPATH,'/html/body/div[1]/div[2]/table/tbody/tr[1]/td/form[3]/div[2]/div/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td/input') == True:    
                DESCARGAR_ARCHIVO = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/table/tbody/tr[1]/td/table[7]/tbody/tr[2]/td/table/tbody/tr/td[4]/div')
                DESCARGAR_ARCHIVO.click()
    

            else:
                print('Es autodescargable')
                pass
               
            
            #Selenium goes back again to the page off all files so to select a new one when the loop starts again
            #driver.execute_script("window.history.go(-1)")
            #Click en volver
            driver.execute_script("window.history.go(-1)")
            
            time.sleep(3)

            #Check if download is complete and if not give it more time to download so to don't have .crdownload files
            
            cwd = os.getcwd()
            src_path_downloads = str(cwd) + '/downloads'
            for file in os.listdir(src_path_downloads):
                if file.endswith(".crdownload"):
                    print('file still downloading')
                    time.sleep(10)
                    log = open('log.txt', 'w')
                    log.write('File still downloading..')

        
            
            src_path_download_2 = str(cwd) + '/download_2'
            for file in os.listdir(src_path_download_2):
                if file.endswith(".crdownload"):
                    print('file still downloading')
                    time.sleep(10)
                    log = open('log.txt', 'w')
                    log.write('File still downloading..')
                    

            source_dir = 'downloads'
            target_dir = 'download_2'
           
            file_names = os.listdir(source_dir)
            print(file_names)
            for file_name in file_names:
                shutil.move(os.path.join(source_dir, file_name), target_dir)
            
            #Rename file in the new directory
            
            new_file_name_pdf = 'download_2/'+ str(id_name) + '.PDF'
            new_file_name_eml = 'download_2/' + str(id_name) + '.EML'
            new_file_name_html = 'download_2/'+ str(id_name) + '.HTML'
            new_file_name_msg = 'download_2/' + str(id_name) + '.MSG'
            new_file_name_docx = 'download_2/' + str(id_name) + '.DOCX'
            try:
                os.rename('download_2/fichero.PDF', new_file_name_pdf)
                print('Renaming PDF file...')
            except:
                
                try:
                    os.rename('download_2/fichero.EML', new_file_name_eml)
                    print('Renaming EML file...')
                except:
                    
                    try:
                        os.rename('download_2/fichero.HTML', new_file_name_html)
                        print('Renaming HTML file...')
                    except:
                        try:
                            os.rename('download_2/fichero.MSG', new_file_name_msg)
                            print('Renaming MSG file...')
                        except:
                            try:
                                os.rename('download_2/fichero.DOCX', new_file_name_docx)
                                print('Renaming DOCX file...')
                            except:
                                pass

            print('Process finished')

            #get current directory and select target directory
            cwd = os.getcwd()

            src_path = str(cwd) + '/download_2'
            trg_path = str(PATH)
            file_names = os.listdir(src_path)


            for src_file in Path(src_path).glob('*.*'):
                shutil.copy(src_file, trg_path)

            #Delete content of download_2
            folder = src_path
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))

            print("Intentamos volver para atras")
            '''WaitUntilFind(By.XPATH, '/html/body/div[1]/div[2]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td[3]') 
            volver_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td[3]')
            volver_btn.click()'''
            print("Ir para atras ha sido todo un exito")

    

    #Download Completed msg

    subprocess.call('UIs/Finished/dist/finished/finished.exe', creationflags=0x08000000)
    
    
   
    
        
        
    
    #a_element = driver.find_element_by_id('row_1_llistadades')
    #a_element.click()
    #time.sleep(3)
    #driver.execute_script('window.print();')


    #Descarga automatica de ficheros
    #archivo_random_element = driver.find_element_by_id('row_0_llistadades')
    #archivo_random_element.click()

    
