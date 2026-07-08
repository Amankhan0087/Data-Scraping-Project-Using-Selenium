import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

sys.stdout.reconfigure(encoding="utf-8")

driver = webdriver.Chrome()
query = "laptop"
driver.get(f"https://www.daraz.pk/catalog/?q={query}")

time.sleep(3)  # let JS render the search results

elems = driver.find_elements(By.CSS_SELECTOR, '[data-qa-locator="product-item"]')
print(f"Found {len(elems)} products")
for elem in elems:
    print(elems.get_attribute("outerhtml"))
    print("---")

time.sleep(3)
driver.close()