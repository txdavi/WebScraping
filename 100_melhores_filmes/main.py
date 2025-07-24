from bs4 import BeautifulSoup
import requests
import pandas as pd


# URL da página que contém a lista dos 100 melhores filmes do século 21
url = "https://www.cnnbrasil.com.br/entretenimento/the-new-york-times-elege-os-100-melhores-filmes-do-seculo-21-confira/"

# Faz uma requisição HTTP para baixar o conteúdo da página
pagina = requests.get(url)

# Cria um objeto BeautifulSoup com o conteúdo HTML da página
soup = BeautifulSoup(pagina.content, "html.parser")

## As tags <li> contêm os nomes dos filmes na página ##

# Busca todas as tags <li> que tenham a classe "mb-3"
filmes_encontrados = soup.find_all('li', class_="mb-3")


# ---------- Analisar e limpar os nomes dos filmes ----------

filmes = []  # Lista que armazenará os nomes dos filmes

for filme in filmes_encontrados:
    # Extrai o texto de cada <li> (nome do filme)
    filme = filme.get_text()

    # Substitui o caractere especial '\xa0' (espaço não quebrável) por nada
    filme = filme.replace("\xa0", "")

    # Remove espaços extras no início e no fim
    filme = filme.strip()

    # Adiciona o nome do filme limpo na lista
    filmes.append(filme)


# Cria um DataFrame vazio
data = pd.DataFrame()

# Adiciona a coluna "Nome dos Filmes" com os dados coletados ao DataFrame
data['Nome dos Filmes'] = filmes

# Exporta os dados para um arquivo Excel
data.to_excel('100 melhores filmes do seculo 21 - The New York Times.xlsx', index=False)
