def prepare_match_data(stats):
    """
    Organiza os dados brutos (média de cartões, percentual, etc.)
    em uma lista numérica que o modelo de IA pode processar.
    """
    return [
        stats.get('avg_cards', 0),
        stats.get('both_pct', 0),
        stats.get('cv', 0),
        stats.get('league_rank', 50)
    ]
