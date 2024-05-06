from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

print(CHROMEDRIVER_EXEC)
chrome_options = webdriver.ChromeOptions()
chrome_services = Service(executable_path=CHROMEDRIVER_EXEC)
chrome_browser = webdriver.Chrome(
    service=chrome_services,
    options=chrome_options
)

chrome_browser.get('https://www.google.com')
