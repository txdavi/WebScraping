# 📱 Bot de Monitoramento de Anúncios OLX – Celulares  

Este projeto automatiza a busca de **novos anúncios de celulares na OLX (RJ)**, ignora anúncios **impulsionados**, salva os resultados em um arquivo `.csv` e envia notificações de **novos produtos** para um **Bot do Telegram**.  

---

## 🚀 Como funciona  

O projeto é composto por dois arquivos principais:  

1. **`bot_anuncio.py`**  
   - Acessa a página da OLX de celulares no RJ.  
   - Coleta os anúncios, ignorando os impulsionados.  
   - Salva os anúncios em `celulares.csv`, garantindo que **apenas novos anúncios** sejam adicionados.  
   - Executa o processo a cada **30 minutos**.  

2. **`bot_telegram.py`**  
   - Lê o arquivo `celulares.csv`.  
   - Compara os anúncios com o histórico (`produtos_enviados.csv`) para **evitar duplicatas**.  
   - Envia os anúncios novos diretamente para um chat do Telegram, utilizando a API do Bot.  
   - Repete a verificação a cada **31 minutos**.  

---

## 🛠️ Tecnologias utilizadas  

- **Python 3.x**  
- **Selenium** → Automação do navegador para capturar anúncios.  
- **Pandas** → Manipulação e armazenamento de dados em CSV.  
- **Telegram Bot API** → Envio de notificações para o Telegram.  
- **dotenv** → Leitura de variáveis de ambiente (`TOKEN` e `CHAT_ID`).  

---

## 📂 Estrutura do projeto  

```
📁 projeto-bot-olx
 ┣ 📜 bot_anuncio.py
 ┣ 📜 bot_telegram.py
 ┣ 📜 celulares.csv               # Anúncios coletados
 ┣ 📜 produtos_enviados.csv        # Histórico de anúncios já enviados
 ┣ 📜 .env                         # Credenciais do bot (TOKEN e CHAT_ID)
 ┣ 📜 requirements.txt             # Dependências do projeto
 ┗ 📜 README.md
```

---

## ⚙️ Configuração  

1. **Clonar o repositório**  
   ```bash
   git clone https://github.com/seu-usuario/projeto-bot-olx.git
   cd projeto-bot-olx
   ```

2. **Criar ambiente virtual (opcional, mas recomendado)**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Instalar dependências**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Criar arquivo `.env`**  
   ```env
   TOKEN_BOT=seu_token_aqui
   CHAT_ID=seu_chat_id_aqui
   ```

---

## ▶️ Como rodar  

1. **Rodar o coletor de anúncios (OLX):**  
   ```bash
   python bot_anuncio.py
   ```

2. **Rodar o bot do Telegram:**  
   ```bash
   python bot_telegram.py
   ```

> Ambos podem ser rodados em paralelo ou em servidores diferentes.  

---

## 📌 Observações  

- O script **ignora anúncios impulsionados**, garantindo que só anúncios orgânicos sejam considerados.  
- O tempo de execução pode ser ajustado:  
  - `bot_anuncio.py` → busca a cada **1800s (30 min)**.  
  - `bot_telegram.py` → envia notificações a cada **1860s (31 min)**.  
- O arquivo `produtos_enviados.csv` evita que o mesmo anúncio seja enviado duas vezes.  

---

## 🧩 Possíveis melhorias  

- Adicionar suporte a múltiplos estados/categorias.  
- Implementar filtros por preço, modelo ou palavra-chave.  
- Criar painel de controle via web (Flask/Django).  
- Deploy em servidor (ex.: VPS, Docker, Heroku).  
