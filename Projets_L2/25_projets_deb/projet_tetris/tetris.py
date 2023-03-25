import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("tetris")
launched = True

            
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load("/Users/sambarbosa/visual_studio_code/L2/Projets_L2/projet_tetris/580b57fcd9996e24bc43c344.png")
        self.rect = self.image.get_rect()
        
player = Player()


while launched:
    screen.blit(player.image,player.rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
            