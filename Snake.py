##OBS1: Comidas podem spawnar em cima da cobra, o que faz com que ela cresça sem comer a comida
##OBS2: Talvez possa aumentar a velocidade do jogo de acordo com o tamanho da cobra
##OBS3: Os pixeis não pertencem a uma grid, portanto, para manter uma certa proporção, o tamanho da tela deve ser múltiplo ao tamanho do quadrado. Caso contrário, podem haver problemas.

#Configurações iniciais
import random
import pygame

pygame.init() #Inicializa o pygame
pygame.display.set_caption('Snake Game') #Nome da janela
largura, altura = 1200, 800 #Tamanho da janela
tela = pygame.display.set_mode((largura, altura)) #Cria a janela
relogio = pygame.time.Clock() #Relógio do jogo

#Cores RGB
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
grey21 = (54, 54, 54)
DarkGray = (169, 169, 169)
semi_sweet_chocolate = (107, 66, 38)
azul_corn_flower = (66, 66, 111)
vermelho_indiano = (78, 47, 47)

#Parâmetros
tamanho_quadrado = 20
velocidade_jogo = 15
multiplicador_de_pontos = 100

#Gera a posição da comida
def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y

#Desenha a comida na tela
def desenhar_comida(comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho_quadrado, tamanho_quadrado])

#Desenha a cobra na tela
def desenhar_cobra(pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho_quadrado, tamanho_quadrado])

#Desenha pontuação na tela
def desenhar_pontuacao(pontos):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render('Pontos: ' + str(pontos), True, DarkGray)
    tela.blit(texto, (1, 1))

#Muda a direção da cobra
def selecionar_velocidade(tecla, vel_x, vel_y):
    if tecla == pygame.K_DOWN and vel_y == 0:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP and vel_y == 0:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_LEFT and vel_x == 0:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_RIGHT and vel_x == 0:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    else:
        return vel_x, vel_y
    
    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False

    x = largura / 2 #Posição horizontal inicial da cobra
    y = altura / 2 #Posição vertical inicial da cobra

    velocidade_x = 0 #Velocidade horizontal da cobra
    velocidade_y = 0 #Velocidade vertical da cobra

    tamanho_cobra = 1 #Tamanho inicial da cobra
    pixels = [] #Lista de pixels da cobra

    comida_x, comida_y = gerar_comida() #Primeira comida do jogo

    while not fim_jogo:
        tela.fill(grey21) #Preenche a tela com a cor preta

        for evento in pygame.event.get(): #Verifica interação do usuário 
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key, velocidade_x, velocidade_y)
        
        #Movimentação da cobra
        x += velocidade_x
        y += velocidade_y

        #Atualiza lista de pixels da cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        #VERIFICA CONDIÇÕES DE FIM DE JOGO:

        #Verifica colisão com o corpo da cobra
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        #Verifica colisão com as paredes
        if x < 0 or x > largura - tamanho_quadrado or y < 0 or y > altura - tamanho_quadrado:
            fim_jogo = True

        #VERIFICA COMIDA COMIDA:

        #Come comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()

        #DESENHA ELEMENTOS NA TELA:

        #Desenha comida na tela
        desenhar_comida(comida_x, comida_y)

        #Desenha pontuação na tela
        desenhar_pontuacao((tamanho_cobra - 1) * multiplicador_de_pontos)

        #Desenha cobra na tela
        desenhar_cobra(pixels)

        #Atualização da tela
        pygame.display.update() #Atualiza a tela
        relogio.tick(velocidade_jogo) #FPS(aumente para diminuir a velocidade do jogo)

rodar_jogo() #Roda o jogo :D