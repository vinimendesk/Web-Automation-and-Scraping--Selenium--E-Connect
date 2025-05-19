from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

import time
import pandas as pd
import os
import csv

# Abre o navegador e faz o login no sistema do gestão.
def abrir_gestao(usuario, senha):   

    # Configurações do Chrome.
    chrome_options = Options() 
    chrome_options.add_argument("--force-device-scale-factor=0.5") # Ajusta o zoom para 50%
    # chrome_options.add_argument("--headless") # Executa o Chrome em modo headless (sem interface gráfica)
    
    global navegador

    # Navegador abre o Chrome.
    navegador = webdriver.Chrome(options=chrome_options)
    navegador.maximize_window()

    # Abre o site do gestão.
    navegador.get("https://areconnect.gestao.plus/ui/auth/login")

    # Procura pelo input do usuário e insere a credencial.
    navegador.find_element(By.XPATH, '//*[@id="InputEmail"]').send_keys("06151282205")

    # Procura pelo input da senha e insere a credencial.
    navegador.find_element(By.XPATH, '//*[@id="InputPassword"]').send_keys("M@riane8291")

    # Procura pelo botão de login e clica.
    navegador.find_element(By.XPATH, '//*[@id="app"]/section/div/div/div[1]/div/div/button').click()

    time.sleep(3)

    # Atualiza a página para exibir as informações.
    navegador.refresh()

    time.sleep(1)

    # Clica em pular tour.
    navegador.find_element(By.XPATH, '//*[@id="v-step-5f866267"]/div[3]/div/button[1]').click()

    time.sleep(1)

    navegador.find_element(By.XPATH, '//*[@id="v-step-8676b12a"]/div[3]/div/button[1]').click()

    # Clica no botão "Vendas".
    navegador.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div[2]/div/div').click()
<<<<<<< HEAD
<<<<<<< HEAD
=======
    
abrir_gestao()
>>>>>>> ea536f6 (First Commit for UI)
=======
>>>>>>> 6257821 (Final version UI)

# Registra os dados coletas no arquivo "Output/log.csv".
def registrar_(dados):
    # Certifica se há um diretório "Output", se não, cria um.
    os.makedirs('Output', exist_ok=True)
    # Define o caminho do arquivo.
    pathOutput = os.path.join('Output', 'log.csv')
    # Titulos do arquivo csv.
    titulos = ['Codigo', 'Parceiro', 'Unidade']

    with open(pathOutput, mode='a', encoding='utf-8', newline='') as file:
        # Cria um objeto writer para escrever no arquivo CSV.
        writer = csv.writer(file)
        # Verifica se o arquivo já existe. Se não existir, escreve os títulos.
        if not os.path.exists(pathOutput):
            writer.writerow(titulos)
        
        # Escreve a mensagem no arquivo.
        writer.writerow(dados)

# Já dentro do sistema, procura o filtra e busca os dados.
def procurar_parceiro(codigo, dados):
    try:
        # Volta para o conteúdo principal (fora de qualquer iframe)
        navegador.switch_to.default_content()

        # Acessa o iframe novamente
        iframe = navegador.find_element(By.CSS_SELECTOR, "iframe.iframeTab")
        navegador.switch_to.frame(iframe)
        print("Iframe encontrado.")

        time.sleep(6)

        # Clica no botão de filtro
        navegador.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div[3]/div[2]/button').click()

        # Digita o código
        # Aguarda o input do código aparecer
        input_code = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="modal-options___BV_modal_body_"]/div/div/div/div/div/div/div/input'))
        )
        input_code.clear()  # Limpa o campo de entrada antes de inserir o código
        input_code.send_keys(codigo)

        # Clica em pesquisar
        navegador.find_element(By.XPATH, '//*[@id="modal-options___BV_modal_footer_"]/button[2]').click()

        time.sleep(5)

        # Aguarda os elementos atualizarem
        WebDriverWait(navegador, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.h-100.d-flex.align-items-center"))
        )

        # Tenta capturar os elementos até 3 vezes, caso fiquem obsoletos.
        for tentativa in range(3):
            try:
                celulas = navegador.find_elements(By.CSS_SELECTOR, "div.h-100.d-flex.align-items-center")
                # Armazena os dados
                dados["Codigo"].append(codigo)
                dados["Parceiro"].append(celulas[15].text)
                dados["Unidade"].append(celulas[20].text)
                break  # Sai do loop se der certo

            except StaleElementReferenceException:
                print("⚠️ Elemento ficou obsoleto. Tentando novamente...")
                time.sleep(2)

        dados_mensagem = [codigo, celulas[15].text, celulas[20].text]

        registrar_(dados_mensagem)
        print(f"✅{codigo}, registrado com sucesso, sem erros")
        return dados

    except Exception as e:
        print(f"❌{codigo}, erro ao buscar código, {e}")
        return dados
