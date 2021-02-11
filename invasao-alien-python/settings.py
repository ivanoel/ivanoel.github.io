class Settings():
    """ Uma Classe para armazenar todas as configurações da Invasão Alienigenas. """

    
    def __init__(self):       
        
        """   Inicializa as configurações do jogo   """
        
        # Configurações da tela
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Configurações da espaçonave
        self.nave_speed_factor = 1.5
        self.nave_limit = 3

        # Configurações dos projeteis
        self.bala_speed_factor = 2
        self.bala_width = 2
        self.bala_height = 15
        self.bala_color = 60, 60, 60
        self.balas_allowed= 5

        #Configurações dos alieniginas
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction igual a 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 1


        # A taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.1

        # A taxa com que os pontos para cada alienigena aumentam
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Inicializa as configurações que mudam no decorrer do jogo. """
        self.nave_speed_factor = 1.5
        self.bala_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction igual a 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 1

        # Pontuação
        self.alien_points = 10

    def increase_speed(self):
        """Aumenta as configurações de velocidade. """
        self.nave_speed_factor *= self.speedup_scale
        self.bala_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
    
