import pygame
import time


pygame.init()

screen= pygame.display.set_mode((750,750))
pygame.display.set_caption("Greeting Card")


image_1 = pygame.image.load("1.png")
i1 =pygame.transform.scale(image_1,(750,750))

while True :
    font=pygame.font.SysFont("Avenir",67)

    text1=font.render("Issac",True,(255,0,0))

    screen.fill((0,0,0))
    screen.blit(i1,(0,0))
    screen.blit(text1,(600,670))
    pygame.display.update()

    time.sleep(2.5)










