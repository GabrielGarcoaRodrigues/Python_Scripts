from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'
TIME_TO_WAIT = 10

# print(CHROMEDRIVER_EXEC)
chrome_options = webdriver.ChromeOptions()
chrome_services = Service(executable_path=CHROMEDRIVER_EXEC)
chrome_browser = webdriver.Chrome(
    service=chrome_services,
    options=chrome_options
)

#Abre navegador
chrome_browser.get('https://www.google.com')

#Busca input de pesquisa
search_input = WebDriverWait(chrome_browser, TIME_TO_WAIT).until(
    EC.presence_of_element_located(
        (By.NAME, 'q')
    )
)

search_input.send_keys('Python') # Digitar Python
search_input.submit() # Apertar Enter de outra maneira
# search_input.send_keys(Keys.ENTER) # Apertar Enter

sleep(10)