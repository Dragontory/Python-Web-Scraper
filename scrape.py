import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrape_website(website): 
    print("Launching browser...")

    # Chrome Driver and Options
    chrome_driver_path = ""
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