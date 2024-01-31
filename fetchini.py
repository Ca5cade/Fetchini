import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import InvalidArgumentException,NoSuchElementException

def find_cheapest_website(item_name):
    filew = open('prices.txt', 'w')
    filer = open('sites.txt', 'r')
    driver = webdriver.Edge()
    driver.maximize_window()
    for i in range(20):
        site=filer.readline()
        driver.get(site)
        time.sleep(2)
        search_bar=driver.find_element(By.CSS_SELECTOR,filer.readline())
        search_bar.send_keys(item_name)
        search_bar.send_keys(Keys.RETURN)
        time.sleep(2)
        try:
            the_item=driver.find_element(By.CSS_SELECTOR,filer.readline())
            print(the_item)
            the_item.send_keys(Keys.RETURN)
            time.sleep(2)
            price=driver.find_element(By.CSS_SELECTOR,filer.readline())
            filew.write(f"From {site} the price of {item_name} is {price.text}\n")
        except InvalidArgumentException:
            continue
    filer.close()
    filew.close()
if __name__ == "__main__":
    item_name = "souris"
    find_cheapest_website(item_name)

