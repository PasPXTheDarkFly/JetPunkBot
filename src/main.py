from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os
from selenium.webdriver.common.by import By
import time

url = "https://www.jetpunk.com/quizzes/pays-du-monde"
options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
driver.get(url)

time.sleep(2)

try:
    cookies = driver.find_element(By.ID, "save")
    time.sleep(2)
    cookies.click()
except:
    print("Cookies non trouvé")




