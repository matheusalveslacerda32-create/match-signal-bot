from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class Scraper:
    def __init__(self):
        # Configura o navegador para rodar em servidores (modo headless)
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")

    def fetch_matches(self):
        """
        Busca a lista de jogos do dia.
        Por enquanto, retorna um jogo de teste.
        """
        return [{"home": "Time A", "away": "Time B", "id": "1"}]

    def get_details(self, match_id):
        """
        Pega os detalhes de cartões de um jogo específico.
        Dados simulados para o bot começar a trabalhar.
        """
        return {
            'history_cards': [2, 3, 2, 4, 1], # Últimos 5 jogos
            'both_pct': 85,                  # 85% de chance
            'goals_ht': 1,
            'corners': 8
        }
