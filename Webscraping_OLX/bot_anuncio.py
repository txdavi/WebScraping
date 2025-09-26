import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

while True:
    # ACESSAR PÁGINA DA OLX
    url = "https://www.olx.com.br/celulares/estado-rj?q=celular&sf=1"

    #C Abre navegador Chrome
    options = Options()
    # Desativa notificações
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # Aceitar cookies (se botão aparecer)
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="adopt-accept-all-button"]'))).click()
    except:
        pass
      
    # CAPTURAR ANÚNCIOS
    celulares = list(driver.find_elements(By.CLASS_NAME, "olx-adcard__link"))
    precos = list(driver.find_elements(By.CLASS_NAME, "olx-adcard__price"))

    # Verifica anúncios impulsionados (patrocinados)
    impulsionados = driver.find_elements(By.CLASS_NAME, "olx-adcard__primary-badge")
    anuncio_impulsionado= [impulsionado.get_attribute("aria-label") for impulsionado in impulsionados]

    # Monta lista de anúncios (nome, preço, link), ignorando impulsionados
    celulares_info = [(celular.text, preco.text, celular.get_attribute("href"),) for i, (celular, preco) in enumerate(zip(celulares, precos)) if not (i < len(anuncio_impulsionado) and anuncio_impulsionado[i])]

    # Se houver anúncios, pega apenas o mais recente (primeiro da lista)
    if celulares_info:
        celulares_info = [celulares_info[0]]  # transforma de volta em lista de 1 item
      
    
    celulares_info_novo = pd.DataFrame(celulares_info, columns=["nome", "preco", "link"])

    # SALVAR EM CSV
    try:
        # Carrega arquivo já existente
        arquivo_celulares_existente = pd.read_csv("celulares.csv", sep=";", encoding="utf-8-sig")
    except FileNotFoundError:
        # Se não existir, cria arquivo vazio
        arquivo_celulares_existente = pd.DataFrame(columns=["nome", "preco", "link"])

    # Filtra apenas anúncios novos (que ainda não estão no CSV)
    add_novo_celular = celulares_info_novo[~celulares_info_novo["link"].isin(arquivo_celulares_existente["link"])]
    # Junta anúncios antigos com novos e salva
    novos_celulares_atualizados =pd.concat([arquivo_celulares_existente, add_novo_celular], ignore_index=True)
    novos_celulares_atualizados.to_csv("celulares.csv", encoding="utf-8-sig", index=False, sep=";")
    # Fecha navegador
    driver.close()

    # Espera 30 minutos antes de repetir
    time.sleep(1800)
