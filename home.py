import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

link = "https://www.divan.ru/category/kartiny"

driver.get(link)

time.sleep(6)

kartiny = driver.find_elements(
    By.CSS_SELECTOR,
    '[data-testid="product-card"]'
)
print(f"{kartiny=}")
parsed_data = []

for kartina in kartiny:
    try:
        title = kartina.find_element(
            By.CSS_SELECTOR,
            '[itemprop="name"]').text
        price = kartina.find_element(By.CSS_SELECTOR, '[itemprop="price"]').get_attribute('content')
        link = kartina.find_element(By.CSS_SELECTOR, '[itemprop="url"]').get_attribute('href')
        parsed_data.append([title, price, link])
    except Exception as e:
        print("Произошла ошибка при парсинге:", e)

driver.quit()

with open("kartiny.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)

print("Данные сохранены в 'kartiny.csv'")