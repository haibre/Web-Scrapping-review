from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

url = input("Masukan URL")

if url :
    options = webdriver.ChromeOptions()
    options.add_argument("__start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    data = []
    for i in range (0, 9):
        soup = BeautifulSoup(driver.page_source, "html.parser")
        containers = soup.findAll('article', attrs={'class':'css-1pr2lii'})
        
        for container in containers:
            try:
                review = container.find('span', attrs = {'data-testid' : 'lblItemUlasan'}).text
                username = container.find('span', attrs = {'class' : 'name'}).text
                data.append(
                    (review, username)
                )
            except AttributeError:
                continue
        
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "button[aria-label='Laman berikutnya']").click()
        time.sleep(3)


    print(data)
    df = pd.DataFrame(data, columns=["Ulasan", "username"])
    df.to_csv("Tokpedreview(1).csv", index=False)

    