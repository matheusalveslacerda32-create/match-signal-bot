import os
import asyncio
from telegram import Bot
from config import BOT_TOKEN, CHANNEL_ID
from scheduler import run_automation
from model import create_model

async def main():
    # Inicializa o Bot do Telegram e o Modelo de IA
    bot = Bot(token=BOT_TOKEN)
    model = create_model()
    
    print("Bot de Sinais Iniciado com Sucesso!")
    
    # Inicia o relógio automático do bot
    await run_automation(bot.send_message, model)

if __name__ == "__main__":
    asyncio.run(main())
