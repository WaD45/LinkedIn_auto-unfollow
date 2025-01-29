import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Charger la liste des exclusions
with open("excluded_list.txt", "r") as f:
    excluded_names = [line.strip() for line in f.readlines()]

email = input("Entrez votre email LinkedIn : ")
password = input("Entrez votre mot de passe LinkedIn : ")

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://www.linkedin.com/login")
wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(email)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
print("Connexion réussie !")
time.sleep(5)

driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
time.sleep(5)

def scrollToLoadAllConnections():
    print("Chargement des connexions...")
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    print("Toutes les connexions sont chargées.")

scrollToLoadAllConnections()

connection_cards = driver.find_elements(By.CLASS_NAME, "mn-connection-card__details")

for card in connection_cards:
    try:
        name = card.find_element(By.CLASS_NAME, "mn-connection-card__name").text.strip()
        if name not in excluded_names:
            print(f"Suppression de {name}...")
            more_button = card.find_element(By.XPATH, ".//button[contains(@class, 'artdeco-dropdown__trigger')]")
            more_button.click()
            time.sleep(1)

            remove_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Supprimer la relation')]")))
            remove_button.click()
            time.sleep(1)

            confirm_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Supprimer')]")))
            confirm_button.click()
            time.sleep(2)

            print(f"{name} supprimé(e) avec succès.")
        else:
            print(f"Connexion conservée : {name}")
    except Exception as e:
        print(f"Erreur lors de la suppression de {name}: {e}")

print("Processus terminé.")
driver.quit()
