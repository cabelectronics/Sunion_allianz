#Work with web Pages & SELENIUM
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
options = webdriver.ChromeOptions()
#options.add_argument("--headless")

def GET_DOCUMENTS(USERNAME, PSWD, SINIESTRO):
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://www.e-pacallianz.com/ngx-epac-professional/public/home')


    USR_element = driver.find_element_by_name("username")
    USR_element.send_keys(USERNAME)

    PSWD_element = driver.find_element_by_name("password")
    PSWD_element.send_keys(PSWD)

    LGIN_element = driver.find_element_by_xpath("/html/body/div/div/app-root/app-public/app-public-home/div/div/div/app-login/div/form/div[2]/div/button")
    LGIN_element.click()

    #if gets error --> send gui error with credentials
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/app-root/app-private/app-private-footer/app-footer/footer/nx-footer-navigation/nx-footer-link/app-link"))
        )
        print('Finded')
    except:
        #Send msg to gui of error in login
        print('Not finded')
        driver.quit()

    APL_ALLIANZ_element = driver.find_element_by_xpath('/html/body/div/div/app-root/app-private/app-private-footer/app-footer/footer/nx-footer-navigation/nx-footer-link/app-link')
    APL_ALLIANZ_element.click()

    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/app-root/app-private/app-site-map/div[2]/div[3]/div/mat-tree/mat-tree-node[2]/a"))
        )
        print('Finded')
    except:
        #Send msg to gui of error in login
        print('Not finded')
        driver.quit()

    MAP_element = driver.find_element_by_xpath('/html/body/div/div/app-root/app-private/app-site-map/div[2]/div[3]/div/mat-tree/mat-tree-node[2]/a')
    MAP_element.click()


    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/app-root/app-private/app-site-map/div[2]/div[3]/div/mat-tree/mat-tree-node[6]/nx-link/a"))
        )
        print('Finded')
    except:
        #Send msg to gui of error in login
        print('Not finded')
        driver.quit()


    PLAT_element = driver.find_element_by_xpath('/html/body/div/div/app-root/app-private/app-site-map/div[2]/div[3]/div/mat-tree/mat-tree-node[6]/nx-link/a')
    PLAT_element.click()

    
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/app-root/app-private/app-application-launch/div[2]/app-iframe-application/div/iframe"))
        )
        print('Finded')
    except:
        #Send msg to gui of error in login
        print('Not finded')
        driver.quit()
   
    iframe = driver.find_element_by_xpath('/html/body/div/div/app-root/app-private/app-application-launch/div[2]/app-iframe-application/div/iframe')
    driver.switch_to.frame(iframe)
    SINIESTRO_ENTRY_element = driver.find_element_by_id('claimNumber')
    SINIESTRO_ENTRY_element.click()
    time.sleep(10)
    SINIESTRO_ENTRY_element.send_keys(SINIESTRO)
    ENVIAR_element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/table/tbody/tr[1]/td/form[1]/div[1]/div/table/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr/td[2]/div')
    ENVIAR_element.click()
    
    
    
   

    
    #SINTRO_element = driver.find_element_by_id('claimNumber.input-text')
    #SINTRO_element.send_keys(SINIESTRO)

    

    print("FINISH")