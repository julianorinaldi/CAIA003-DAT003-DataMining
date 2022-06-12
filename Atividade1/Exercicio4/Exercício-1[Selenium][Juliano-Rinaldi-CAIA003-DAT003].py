# No arquivo Selenium-Install-Package.sh tem os pacotes que precisam ser instalados (Considerado SO Ubuntu)
# Não foi possível fazer com o Google Colab por causa do chrome.

# 4- Crie uma aplicação que usa o Selenium para abrir o site https://www.uol.com.br/ e rolar a página para baixo até o fim do conteúdo.
# Autor: Juliano Tiago Rinaldi

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()

# Parâmetro para abrir sem tela, usado normalmente para console.
#chrome_options.add_argument('--headless')

chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
driver.get("https://www.uol.com.br/")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
