chrome_options = webdriver.ChromeOptions()
chrome_services = Service(executable_path=CHROMEDRIVER_EXEC)
chrome_browser = webdriver.Chrome(
    service=chrome_services,
    options=chrome_options
)

chrome_browser.get('https://www.google.com')