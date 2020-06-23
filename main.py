import pygame
from random import randrange

# GLOBAIS
WHITE = (229,229,229) 
BLACK = (30,30,30)
RED = (255,64,64)
GREEN = (144,238,144)
BLUE = (0,178,238)
LARGURA = 460
ALTURA = 320
TITLE = 'Snake Game'
TAMANHO = 10
PLACAR = 30

RELOGIO = pygame.time.Clock()

pygame.init()
BACKGROUND = pygame.display.set_mode(size=(LARGURA,ALTURA))
pygame.display.set_caption(TITLE)


def Text(msg, cor, tam, x, y):
  FONT = pygame.font.SysFont(None, tam)
  text1 = FONT.render(msg, True, cor)
  BACKGROUND.blit(text1, [x, y])

def Cobra(Cobra_XY):
  for XY in Cobra_XY:
    pygame.draw.rect(BACKGROUND, BLACK, [XY[0], XY[1], TAMANHO, TAMANHO])
  
def Maca(POS_X, POS_Y):
  pygame.draw.rect(BACKGROUND, RED, [POS_X, POS_Y, TAMANHO, TAMANHO])
  
def main():
  sair = True
  Cobra_XY = list()
  CobraComp = 5
  GameOver = False
  Pontos = 0
  POS_X, POS_Y = randrange(0,LARGURA-TAMANHO,10), randrange(0,(ALTURA-PLACAR)-TAMANHO,10)
  MACA_X, MACA_Y = randrange(0,LARGURA-TAMANHO,10), randrange(0,(ALTURA-PLACAR)-TAMANHO,10)
  SPEED_X, SPEED_Y = 0, 0
  
  while sair:
    while GameOver:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sair = False
          GameOver = False
          
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_c:
            sair = True
            Cobra_XY = list()
            CobraComp = 5
            GameOver = False
            Pontos = 0
            POS_X, POS_Y = randrange(0,LARGURA-TAMANHO,10), randrange(0,(ALTURA-PLACAR)-TAMANHO,10)
            MACA_X, MACA_Y = randrange(0,LARGURA-TAMANHO,10), randrange(0,(ALTURA-PLACAR)-TAMANHO,10)
            SPEED_X, SPEED_Y = 0, 0
            
          if event.key == pygame.K_s:
            sair = False
            GameOver = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
          x, y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
          if x > 130 and y > 120 and x < 225 and y < 145:
            sair = True
            Cobra_XY = list()
            CobraComp = 5
            GameOver = False
            Pontos = 0
            POS_X, POS_Y = randrange(0,LARGURA-TAMANHO,10), randrange(0,(ALTURA-PLACAR)-TAMANHO,10)
            MACA_X, MACA_Y = randrange(0,LARGURA-TAMANHO,10), randrange(0,(ALTURA-PLACAR)-TAMANHO,10)
            SPEED_X, SPEED_Y = 0, 0
            
          if x > 260 and y > 120 and x < 320 and y < 145:
            sair = False
            GameOver = False
            
      BACKGROUND.fill(WHITE)
      Text("GAME OVER", RED, 50, 115, 50)
      Text(f"Final Score: {str(Pontos)}", BLACK, 30, 135, 90)
      pygame.draw.rect(BACKGROUND, BLACK, [130, 120, 95, 25])
      Text("Continue (C)", WHITE, 20, 135, 125)
      
      pygame.draw.rect(BACKGROUND, BLACK, [260, 120, 60, 25])
      Text("Get Out (S)", WHITE, 20, 268, 125)
      pygame.display.update()
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sair = False
        
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and SPEED_X != TAMANHO:
          SPEED_Y = 0
          SPEED_X = -TAMANHO
        if event.key == pygame.K_RIGHT and SPEED_X != -TAMANHO:
          SPEED_Y = 0
          SPEED_X = TAMANHO
        if event.key == pygame.K_UP and SPEED_Y != TAMANHO:
          SPEED_X = 0
          SPEED_Y = -TAMANHO
        if event.key == pygame.K_DOWN and SPEED_Y != -TAMANHO:
          SPEED_X = 0
          SPEED_Y = TAMANHO
    
    if sair:
    
      BACKGROUND.fill(WHITE)
      
      if POS_X == MACA_X and POS_Y == MACA_Y:
        MACA_X, MACA_Y = randrange(0,LARGURA-TAMANHO,10), randrange(0,(ALTURA-PLACAR)-TAMANHO,10)
        CobraComp += 1; Pontos += 1
      
      # BORDAS
      if POS_X > LARGURA or POS_X < 0 or POS_Y > ALTURA-40 or POS_Y < 0: GameOver = True
      
      CobraInicio = []
      CobraInicio.append(POS_X)
      CobraInicio.append(POS_Y)
      Cobra_XY.append(CobraInicio)
      if len(Cobra_XY) > CobraComp:
        del Cobra_XY[0]
      
      if CobraComp > 6:
        for Bloco in Cobra_XY[:-1]:
          if Bloco == CobraInicio:
            GameOver = True
      
      pygame.draw.rect(BACKGROUND, BLACK, [0, ALTURA-PLACAR, LARGURA, PLACAR])
      Text(f"Score: {str(Pontos)}", WHITE, 20, 10, ALTURA-22)
      Cobra(Cobra_XY)
      Maca(MACA_X, MACA_Y)
      
      POS_X += SPEED_X
      POS_Y += SPEED_Y
      
      RELOGIO.tick(15)
      pygame.display.update()  
    
main()