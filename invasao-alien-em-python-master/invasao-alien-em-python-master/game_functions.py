import sys
from time import sleep
import pygame
from bala import Bala
from alien import Alien

            
def check_keydown_events(event, config, screen, nave, balas):
    if event.key == pygame.K_RIGHT:
        # move a espaçonave para a direita
        nave.mover_direita = True
        
        # move a espaçonave para a esquerda
    elif event.key == pygame.K_LEFT:
        nave.mover_esquerda = True
        
    elif event.key == pygame.K_UP:
        nave.mover_pracima = True
        
    elif event.key == pygame.K_DOWN:
        nave.mover_prabaixo = True
        
    elif event.key == pygame.K_z:
        fogo_bala(config, screen, nave, balas)

    elif event.key == pygame.K_q:
        sys.exit()

        
def fogo_bala(config, screen, nave, balas):
    """ Dispara um projetil se o limite ainda nao foi alcançado. """
    # Cria um novo projetil e o adicionaao grupo d projeteis.
    # Cria um novo projetil e o adiciona ao grupo de projeteis.
    if len(balas) < config.balas_allowed:
        nova_bala = Bala(config, screen, nave)
        balas.add(nova_bala)
                
def check_keyup_events(event, nave):
    #Respode a soltura das teclas
    if event.key == pygame.K_RIGHT:
        nave.mover_direita = False
    elif event.key == pygame.K_LEFT:
        nave.mover_esquerda = False        
    elif event.key == pygame.K_UP:
        nave.mover_pracima = False        
    elif event.key == pygame.K_DOWN:
        nave.mover_prabaixo = False

def check_events(config, screen, stats, sb, play_button, nave, aliens, balas):
    """ Responde a eventos de pressionamento de teclas e de mouse. """    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, config,screen,  nave, balas)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,nave)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(config, screen, stats, sb, play_button, nave, aliens, balas, mouse_x, mouse_y)

def check_play_button(config, screen, stats, sb, play_button, nave, aliens, balas, mouse_x, mouse_y):
    """ Inicia um novojogo quando ojogador clicar em Jogar."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_ativo:

        # Reinicia as configurações do jogo
        config.initialize_dynamic_settings()
        
        # Oculta o cursor do mouse
        pygame.mouse.set_visible(False)
        
        # Reinicia os dados estatisiticos do jogo
        stats.reset_stats()
        stats.game_ativo = True

        # Reinicia as imagens do painel de pontuação
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_naves()

        # esvazia a lista de alienigenas e de projeteis
        aliens.empty()
        balas.empty()

        # Cria uma nova frota e centraliza a espoçonave    
        create_fleet(config, screen, nave, aliens)
        nave.center_nave()
        
def update_balas(config, screen, stats, sb, nave, aliens, balas):
    """ Atualiza a posição dos projeteis e se livra dos projeteis antigos."""
    # Atualiza as posições dos projeteis.
    balas.update()

    # Verifica se algum projetil atingiu os alienigenas
    # Em caso afirmativo, livra-se do projetil e do alienigenas.
    # Livra-se dos projeteis que desapareceram
    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)

    check_bala_alien_colisao(config, screen, stats, sb, nave, aliens, balas)

def check_bala_alien_colisao(config, screen, stats, sb, nave, aliens, balas):
    """ Responde a colisoes entre protejeis e alienigenas. """
    # Remove qualquer projetil e alienigenas quetenha colidido.
    colisao = pygame.sprite.groupcollide(balas, aliens, True, True)

    if colisao:
        for aliens in colisao.values():
            stats.score += config.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
        
    if len(aliens) == 0:
        # Se afrotatodafor destruida, inica um novo nivel
        balas.empty()
        config.increase_speed()

        # Aumenta o nivel
        stats.level += 1
        sb.prep_level()

        
        create_fleet(config, screen, nave, aliens)
        
def check_high_score(stats, sb):
    """Verifica se há uma nova pontuação máxima. """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
    
def get_numero_aliens_x(config, alien_width):
    """Determina o numero de alienigenas que cabem em uma linha, """
    valor_espaco_x = config.screen_width - 1 * alien_width
    numero_aliens_x = int(valor_espaco_x / (2 * alien_width))
    return numero_aliens_x

def get_numero_rows(config, nave_height, alien_height):
    """Determina o numero de alienigenas que cabem em uma linha, """
    valor_espaco_y = (config.screen_height - (3 * alien_height) -  nave_height)
    numero_rows = int(valor_espaco_y / (2 * alien_height))
    return numero_rows

def create_alien(config, screen, aliens, alien_numero, row_numero):
    #Cria um alienigena e posiciona na linha
        alien = Alien(config, screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_numero
        alien.rect.x =  alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_numero
        aliens.add(alien)


def create_fleet(config, screen, nave, aliens):
    """Cria uma frota completa de alienigenas. """
    # Cria um alienigenas e calcula o numero de alienigenas em uma linha.
    # O espaçamento entreos alienigenas e igual a largura de um alienigena.
    alien = Alien(config,screen)
    numero_aliens_x = get_numero_aliens_x(config, alien.rect.width)
    numero_rows = get_numero_rows(config, nave.rect.height, alien.rect.height)
    
    # Cria a frota de alienigenas.
    for row_numero in range(numero_rows):
        for alien_numero in range(numero_aliens_x):
            create_alien(config, screen, aliens, alien_numero, row_numero)

#def update_aliens(aliens):
    """ Atualiza as posições de todos os alieniginas da frota."""
def check_fleet_edges(config, aliens):
    """ Responde apropriadamente se algum alienigenas alcançou uma borda."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(config, aliens)
            break

def change_fleet_direction(config, aliens):
    """  Faz toda a frota descer e muda sua direção   """
    for alien in aliens.sprites():
        alien.rect.y += config.fleet_drop_speed
    config.fleet_direction *= -1

def check_aliens_bottom(config, screen, stats, sb, nave, aliens, balas):
    #Verifica se algum alien alcançou a parte infeiror da tela
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Trata esse caso do mesmo que é feitoquando a espaçonave é atingida
            nave_atingida(config, screen, stats, sb, nave, aliens, balas)
            break

def update_aliens(config, screen, stats, sb, nave, aliens, balas):
    """
        Verifica se a frota está em uma das bordas
        e então atualiza as posições de todos os alienigenas da frota.        
    """
    check_fleet_edges(config, aliens)    
    aliens.update()

    # Verifica se houve colisões entre alienigenas e a espaçonave.
    if  pygame.sprite.spritecollideany(nave, aliens):
        nave_atingida(config, screen, stats, sb, nave, aliens, balas)


    # Verifca se há algum alienque atingiu aparteinfeior da tela
    check_aliens_bottom(config, screen, stats, sb, nave, aliens, balas)

    
def nave_atingida(config, screen, stats, sb, nave, aliens, balas):
    # Responde ao fato de a espoçonave ter sido atingida por um alienigena.
    if stats.naves_left > 0:
        # Decrementa nave_left
        stats.naves_left -= 1

        # Atualiza o painel de pontuações
        sb.prep_naves()
        
        # esvazia a lista de alienigenas e de projeteis
        aliens.empty()
        balas.empty()

        # Cria uma nova frota e centraliza a espoçonave    
        create_fleet(config, screen, nave, aliens)
        nave.center_nave()

        # Faz uma pausa
        sleep(0.5)

    else:
        stats.game_ativo = False
        pygame.mouse.set_visible(True)

        
def update_screen(config, screen, stats, sb, nave, aliens, bullets, play_button):
    """Atualiza as imagens na tela e alterna para nova tela. """
    screen.fill(config.bg_color) # Obs: Erro ao exibir disparos
    
    # Redesenha todos os projeteis atras da espaçonave e dos alienigenas.
    for bala in bullets.sprites():
        bala.draw_bala()      
    nave.blitme()
    aliens.draw(screen)

    #Desenha a informação sobre a pontuação
    sb.show_score()

    #Desenha o botão Play seo jogo estiver inativo
    if not stats.game_ativo:
        play_button.draw_button()
        
    #Deixa a tela mais recente visivel
    pygame.display.flip()
