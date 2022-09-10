from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from subprocess import CREATE_NO_WINDOW
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

dwn_path = os.getcwd()
dwn_path = dwn_path + '\downloads'
print(dwn_path)
prefs = {
'download.default_directory': dwn_path,
'download.prompt_for_download': True,
'download.extensions_to_open': 'xsd',
'safebrowsing.enabled': True,
}

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs',prefs)
options.add_argument("start-maximized")
options.add_argument("--headless")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--safebrowsing-disable-download-protection")
options.add_argument("--safebrowsing-disable-extension-blacklist")



service = Service(ChromeDriverManager().install())
service.creationflags = CREATE_NO_WINDOW
driver = webdriver.Chrome(service=service,options=options)
driver.get("http://www.landxmlproject.org/file-cabinet")
#time.sleep(20)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="JOT_FILECAB_container_wuid:gx:27e097a33d866e64"]/td[3]/span[2]/a[2]'))).click()
time.sleep(20)
print("COMPLETED")