import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time


#Doesn't solve captchas 
def scrape_website(website): 
    print("Launching browser...")

    # Chrome Driver and Options
    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()

    #Setup Web Driver
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Page Loaded...")
        html = driver.page_source
        time.sleep(10)

        return html
    
    finally:
        driver.quit()

# Replaces above code to bypass Captchas
# from selenium.webdriver import Remote, ChromeOptions
# from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
# from bs4 import BeautifulSoup
# from dotenv import load_dotenv
# import os

# load_dotenv()

# SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER")


# def scrape_website(website):
#     print("Connecting to Scraping Browser...")
#     sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
#     with Remote(sbr_connection, options=ChromeOptions()) as driver:
#         driver.get(website)
#         print("Waiting captcha to solve...")
#         solve_res = driver.execute(
#             "executeCdpCommand",
#             {
#                 "cmd": "Captcha.waitForSolve",
#                 "params": {"detectTimeout": 10000},
#             },
#         )
#         print("Captcha solve status:", solve_res["value"]["status"])
#         print("Navigated! Scraping page content...")
#         html = driver.page_source
#         return html