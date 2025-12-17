class SimpleModel:
    def predict(self, features):
        # Lógica simples para dar uma nota ao jogo de 0 a 100
        # features[0] é a média de cartões, features[1] é o percentual
        score = (features[0] * 10) + (features[1] * 0.5)
        return min(max(score, 0), 100)

def create_model():
    return SimpleModel()
