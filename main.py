import pygame
import os
from subprocess import call
from threading import Thread


#colores
red = (255, 0, 0)

pygame.init()
pygame.display.set_caption('Empty Life')
screen = pygame.display.set_mode((650, 650))
done = False

image = pygame.image.load("images/title.png") 
pygame.mixer.music.load('sounds/rain.mp3')
pygame.mixer.music.play(-1)

myfont = pygame.font.SysFont("Arial", 60)
label = myfont.render("Empezar", 1, red)



while not done:

        screen.blit(image, (0, 0)) 
        screen.blit(label, (250, 100))


        pressed = pygame.mouse.get_pressed()
        posicion = pygame.mouse.get_pos()

        if pressed[0] == 1:
                if posicion[0] > 254 and posicion[0] < 447 and posicion[1] > 115 and posicion[1] < 157:
                        done = True
                        call(["python", "scenes/test.py"])

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()