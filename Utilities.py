#file for utility methods

import json
from selenium import webdriver as driver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import QueryLA as LA

# method to open the configuration (config.json) file in read mode
def GetParameters(parameter):
    with open('config.json', 'r', encoding="utf-8") as file:
        configuracao = json.load(file)

    return configuracao[parameter]

def createDriverChrome():
    try:

        servico = Service(ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {
            "intl.accept_languages": "pt-BR",
            "disable-popup-blocking": "true",
            "plugins.always_open_pdf_externally": "true",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
        })
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--lang=pt")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--log-level=3")

        chrome_options.accept_insecure_certs = True
        
        print(f'Iniciando Chrome')

        #abre chrome
        chrome = driver.Chrome(service=servico, options=chrome_options)

        return chrome
    
    except Exception as e:
        print(f'Erro Chrome {e}')

        return False

def subjectQuery(text):
    try:
        
        LA.searchLA(text)

    except Exception as e:
        print(f'Erro na automação {e}')