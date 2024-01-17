from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()
print(driver)

driver.implicitly_wait(5)

language = driver.find_element(By.ID, "langSelect-EN")
language.click()
cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1, -1, -1)]




actions = ActionChains(driver)
actions.click(cookie)

# for i in range(5000):
#     actions.perform()

for i in range(5000):
    actions.click(cookie).perform()
    time.sleep(0.01)
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()


time.sleep(300)