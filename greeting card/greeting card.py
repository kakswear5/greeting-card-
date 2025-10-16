


import pygame
import time


pygame.init()

screen= pygame.display.set_mode((750,750))
pygame.display.set_caption("Greeting Card")


image_1 = pygame.image.load("1.png")
i1 =pygame.transform.scale(image_1,(750,750))


while True :
    font=pygame.font.SysFont("Playwrite DE SAS",67)

    text1=font.render("Issac",True,(255,0,0))

    screen.fill((0,0,0))
    screen.blit(i1,(0,0))
    screen.blit(text1,(600,670))
    pygame.display.update()

    time.sleep(2.5)

    image_2 = pygame.image.load("2.png")
    i2= pygame.transform.scale(image_2,(750,750))

    text2=font.render("WELL DONE",True,(250,0,0))

    screen.fill((0,0,0))
    screen.blit(i2,(0,0))
    screen.blit(text2,(375,650))
    pygame.display.update()

    time.sleep(2.5)

    image_3=pygame.image.load("3.png")
    i3=pygame.transform.scale(image_3,(750,750))

    text3=font.render("GOOD JOB",True,(250,0,0))

    screen.fill((0,0,0))
    screen.blit(i3,(0,0))
    screen.blit(text3,(100,700))
    pygame.display.update()

    time.sleep(2.5)













