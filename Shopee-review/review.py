from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

url = "https://shopee.co.id/Nashir-Care-Cream-Salep-Obat-Pengempes-Ambeien-Stadium-1-2-3-4-Alami-Paling-Ampuh-i.1051008660.21093204965?sp_atk=4c0446a3-98e7-4cee-9f26-7485b986f5bc&xptdk=4c0446a3-98e7-4cee-9f26-7485b986f5bc&is_from_login=true"

options = webdriver.ChromeOptions()
options.add_argument("__start-maximized")
driver = webdriver.Chrome(options=options)
driver.get(url)
""""
data = []
"""
for i in range (0, 10):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    containers = soup.find_all('div', attrs={'class':'shopee-product-rating__main'})

print(containers)
    
"""
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
"""
