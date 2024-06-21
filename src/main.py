
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from country_list import available_languages, countries_for_language
import os
import time

url = "https://www.jetpunk.com/quizzes/pays-du-monde"
options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
driver.get(url)
driver.implicitly_wait(10)




try:
    print("Début de l'attente pour le bouton des cookies...")
    wait = WebDriverWait(driver, 20)

    # Vérifiez si l'élément est dans un iframe
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    print(f"Nombre d'iframes sur la page : {len(iframes)}")
    if len(iframes) > 0:
        driver.switch_to.frame(iframes[0])
        print("Changement de contexte vers le premier iframe")

    # Vérifiez si l'élément existe
    elements = driver.find_elements(By.XPATH, '//*[@id="save"]')
    if len(elements) == 0:
        print("L'élément n'existe pas")
    else:
        print("L'élément existe")

    cookies = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="save"]')))
    print("Bouton trouvé et cliquable")

    # Faire défiler jusqu'à l'élément
    print("Défilement jusqu'à l'élément...")
    driver.execute_script("arguments[0].scrollIntoView(true);", cookies)
    time.sleep(1)  # Attendre un peu pour s'assurer que le défilement est terminé

    # Vérifier si l'élément est visible
    if cookies.is_displayed():
        print("L'élément est visible")
    else:
        print("L'élément n'est pas visible")

    # Méthode 1: Utiliser JavaScript pour cliquer sur l'élément
    try:
        print("Essai de clic avec JavaScript...")
        driver.execute_script("arguments[0].click();", cookies)
        print("Méthode 1: Bouton cliqué")
    except Exception as e1:
        print(f"Méthode 1 échouée: {e1}")


except Exception as e:
    print(f"Erreur : {e}")


try:
    driver.switch_to.default_content()
    print("Revenu au contexte principal")

    # Attendre que le bouton "start" soit cliquable
    start_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="start-button"]')))
    print("Bouton 'start' trouvé et cliquable")

    # Cliquer sur le bouton "start"
    print("Essai de clic sur le bouton 'start'...")
    start_button.click()
    print("Bouton 'start' cliqué")

except Exception as e:
    print(f"Erreur : {e}")

champs_texte = driver.find_element(By.XPATH, '//*[@id="txt-answer-box"]')


countries = dict(countries_for_language('fr'))
for country_code, country_name in countries.items():
    champs_texte.clear()
    champs_texte.send_keys(country_name)
    time.sleep(0.2)

time.sleep(5)





