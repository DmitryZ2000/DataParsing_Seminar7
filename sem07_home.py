from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import csv

import time

options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)

driver.get("https://zstandart.ru/catalog/tekhnika/noutbuki_i_kompyutery/noutbuki/")
# driver.get("https://zstandart.ru/catalog/tekhnika/naruchnye_chasy/")
time.sleep(2)


time.sleep(2)

while True:
    wait = WebDriverWait(driver, timeout=10)
    # Находим все элементы, скролим до конца
    cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='inner_wrap TYPE_1']")))

    print(len(cards))

    try:
        time.sleep(2)
        next_button = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='ajax_load_btn rounded3 colored_theme_hover_bg']")))
        next_button.click()
    except:
        break

cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='inner_wrap TYPE_1']")))
print(len(cards))
goods_list   = []

for count, card in enumerate(cards):  
    info = card.find_element(By.XPATH, "./div[@class='item_info']").text.split('\nВ наличии\n')
    name = info[0]
    price = info[1][:-2] # Убрали символ ' ₽'
    url = card.find_element(By.XPATH, ".//a").get_attribute('href')
    goods_list.append([count, name, price, url])
    print(f'{count+1}, {name}, {price = }, {url}')

# print(goods_list)

driver.close()

# Запись данных в csv
with open("lzs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=';') 
    writer.writerow(["count", "name", "price", "url"])
    writer.writerows(goods_list)    
