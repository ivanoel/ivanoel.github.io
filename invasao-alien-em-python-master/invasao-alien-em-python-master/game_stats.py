import pygame

class GameStats():
    """ Armazena dados estatisticos da Invasão Alienigenas. """


    def __init__(self, config):
        # Inicialiaza os dados estatisticos
        self.config = config
        self.reset_stats()

        # inicia a invasão alienigenas em um estado ativo
        self.game_ativo = False

        # A pontuação máxima jamais deverá ser reiniciada
        self.high_score = 0
        
    def reset_stats(self):
        # Inicialiaza os dados estatisticos quepodem mudar durante o jogo
        self.nave_left = self.config.nave_limit
        self.score = 0
        self.level = 1



    
        
