# WebScraping

import requests
from bs4 import BeautifulSoup 

url = "https://discord.com"
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

if response.status_code == 200:
    print("Requisição bem sucedida!")

    # print(parsed_html.prettify())
    print(parsed_html.title.text)

    title = parsed_html.select_one("body > div:nth-child(1) > div.section-hero-imagine.home-2023 > div > div > div.w-layout-grid.grid-branding.imagine-new > h1")
    print(title.text)

    div = title.parent
    print(div.prettify())



else:
    print(f"Requisição mal sucedida! {response.status_code}")