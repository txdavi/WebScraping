import pandas as pd
from telegram import Bot
import asyncio
import os
from dotenv import load_dotenv

# CONFIGURAÇÕES INICIAIS
load_dotenv()  # Carrega variáveis do arquivo .env
TOKEN = os.getenv("TOKEN_BOT")  # Token do Bot do Telegram
CHAT_ID = os.getenv("CHAT_ID")  # ID do chat para enviar mensagens
bot = Bot(token=TOKEN)

# Arquivos que armazenam os anúncios
CSV_ARQUIVOS = ["celulares.csv"]
ENVIADOS_CAMINHO = "produtos_enviados.csv"  # Histórico de anúncios já enviados

# FUNÇÃO PRINCIPAL
async def enviar_produtos_novos():
    while True:
        
        # Ler histórico de anúncios enviados
        if os.path.exists(ENVIADOS_CAMINHO):
            enviados = pd.read_csv(ENVIADOS_CAMINHO, sep=';', encoding="utf-8-sig")
        else:
            enviados = pd.DataFrame(columns=["nome", "preco", "link"])

        enviados.columns = enviados.columns.str.strip().str.lower()
        novos = pd.DataFrame(columns=["nome", "preco", "link"])

        # Verificar anúncios em CSV
        for arquivo in CSV_ARQUIVOS:
            if not os.path.exists(arquivo):
                continue

            df = pd.read_csv(arquivo, sep=';')
            df.columns = df.columns.str.strip().str.lower()

            # Adicionar apenas os anúncios que ainda não foram enviados
            for _, linha in df.iterrows():
                if not (
                    (enviados['nome'] == linha['nome']) &
                    (enviados['preco'] == linha['preco']) &
                    (enviados['link'] == linha['link'])
                ).any():
                    novos = pd.concat([novos, pd.DataFrame([linha])], ignore_index=True)

        # Enviar novos anúncios pelo Telegram
        if not novos.empty:
            for _, produto in novos.iterrows():
                mensagem = (
                    f"🚨 NOVO PRODUTO ANUNCIADO! 🚨\n\n"
                    f"Nome: {produto['nome']}\n\n"
                    f"Preço: {produto['preco']}\n\n"
                    f"Link: {produto['link']}"
                )
                await bot.send_message(chat_id=CHAT_ID, text=mensagem)

            # Atualiza histórico
            enviados = pd.concat([enviados, novos], ignore_index=True)
            enviados.to_csv(ENVIADOS_CAMINHO, sep=';', index=False, encoding="utf-8-sig")

        # Espera 31 minutos antes de rodar novamente
        await asyncio.sleep(1860)

# EXECUÇÃO DO SCRIPT

if __name__ == "__main__":
    asyncio.run(enviar_produtos_novos())
