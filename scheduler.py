import asyncio
from scraper import Scraper

async def run_automation(bot_send_func, model):
    scraper = Scraper()
    while True:
        try:
            print("Iniciando busca automática de jogos...")
            # O scraper busca a lista de jogos
            jogos = scraper.fetch_matches() 
            
            for jogo in jogos:
                # Aqui o bot vai analisar cada jogo sozinho
                print(f"Analisando: {jogo['home']} x {jogo['away']}")
                
            # Espera 1 hora (3600 segundos) para a próxima busca
            await asyncio.sleep(3600) 
        except Exception as e:
            print(f"Erro no agendador: {e}")
            await asyncio.sleep(300)
