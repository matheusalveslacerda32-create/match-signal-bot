import statistics

def apply_all_rules(data):
    # Pega os dados configurados
    from config import MIN_BOTH_CARDS_PCT, MIN_AVG_CARDS, MAX_CV_CARDS
    
    # Calcula a média e o percentual
    avg = statistics.mean(data['history_cards'])
    both_pct = data['both_pct']
    
    # Calcula a variação (CV)
    cv = statistics.stdev(data['history_cards']) / avg if len(data['history_cards']) > 1 else 0
    
    # Verifica se o jogo passou em todas as suas condições
    passed = (both_pct >= MIN_BOTH_CARDS_PCT and 
              avg >= MIN_AVG_CARDS and 
              cv <= MAX_CV_CARDS)
              
    return passed, {"avg": avg, "pct": both_pct, "cv": cv}
