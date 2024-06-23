#

import Utilities as DAO
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def searchLA(text):
    
    ret = None

    try:
        wait = int(DAO.GetParameters("Wait"))

        driver = DAO.createDriverChrome()

        if driver is False:
            print(f'Error Chrome {e}')
            return False

        driver.get(DAO.GetParameters("UrlSite"))
        print(f'Successful accessing website')

        WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.XPATH, DAO.GetParameters("XpathButtonSearech"))))
        ret = DAO.SendClick(driver, DAO.GetParameters("XpathButtonSearech"), By.XPATH)
        if ret == 1:
            print(f'Erro on send click {e}')
            return False
        
        WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.XPATH, DAO.GetParameters("XpathInputSearch"))))
        ret = DAO.SendText(driver, DAO.GetParameters("XpathInputSearch"), By.XPATH, text)
        if ret == 1:
            print(f'Erro on send text {e}')
            return False
        
        WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.XPATH, DAO.GetParameters("XpathFormSearch"))))
        ret = DAO.SendText(driver, DAO.GetParameters("XpathFormSearch"), By.XPATH, text)
        if ret == 1:
            print(f'Erro on send text {e}')
            return False
        
        driver.quit()

    except Exception as e:
        print(f'Erro on system {e}')
        return False