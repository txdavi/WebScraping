# Web Scraping - 100 Melhores Filmes do Século 21 (The New York Times)

Este projeto faz a extração (web scraping) da lista dos **100 melhores filmes do século 21**, conforme publicado pela CNN Brasil (baseado no The New York Times).  
O resultado final é exportado para um arquivo **Excel (.xlsx)** contendo todos os nomes dos filmes.

## Funcionalidades
- Faz o download do conteúdo HTML de uma página da CNN Brasil.
- Extrai os nomes dos filmes listados.
- Limpa os dados para remover caracteres indesejados.
- Salva os nomes em um arquivo Excel.

## Tecnologias Utilizadas
- [Python 3](https://www.python.org/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
- [Requests](https://docs.python-requests.org/)
- [Pandas](https://pandas.pydata.org/)

## Como Usar

### 1. Clone este repositório
```bash
git clone https://github.com/seu-usuario/nome-do-projeto.git
cd nome-do-projeto
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o script
```bash
python main.py
```

### 5. Resultado
Um arquivo Excel será gerado no diretório do projeto.:
```
100 melhores filmes do seculo 21 - The New York Times.xlsx
```



## Licença
Este projeto é de uso educacional e está sob a licença MIT.
