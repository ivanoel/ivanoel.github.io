#import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from nave import Nave
#from alien import Alien
import game_functions as gf

def inicio_game():
    # inicializa o jogo, as configurações e o objeto screen
    pygame.init()
    config = Settings()
    screen = pygame.display.set_mode(
        (config.screen_width, config.screen_height)
        )
    pygame.display.set_caption("Alien Invasion")

    # Cria botão Play
    play_button = Button(config, screen, "Jogar")
    
    #Cria uma nova instância para armazenar dados estatisticos do jogo e cria painel de pontuação
    stats= GameStats(config)
    sb = Scoreboard(config, screen, stats)
    
    # Define a cor de fundo
   # bg_color = (230, 230,230)
    
    # Cria uma espaçonave, um grupo de projeteis e um grupo de alienigenas.
    nave = Nave(config, screen)
    balas = Group()
    aliens = Group()

    # Cria frota de alienigenas.
    gf.create_fleet(config, screen,nave, aliens)

    # Inicia o laço principal do jogo
    while True:
        gf.check_events(config, screen, stats, sb, play_button, nave, aliens, balas)
        
        if stats.game_ativo:
            nave.update()
            gf.update_balas(config, screen, stats,sb, nave, aliens, balas)
            gf.update_aliens(config, screen, stats, sb, nave, aliens, balas)
            
        gf.update_screen(config, screen, stats, sb, nave, aliens, balas, play_button)

inicio_game()
