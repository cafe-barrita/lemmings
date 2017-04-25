import os, sys, math, random, eztext
import pygame
from pygame.locals import *
if sys.platform == 'win32' or sys.platform == 'win64':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
from ScenarioEdit import Scenario

pygame.init()
reloj = pygame.time.Clock()


resolution = (800, 600)
scenario = Scenario(resolution)
pygame.display.set_caption('Lemmings map editor')
screen = pygame.display.set_mode(resolution)


WHITE = 100, 100, 100

done = False
previousPosition = -9999, -9999

state = "drawing"


text = eztext.Input(maxlength=45, color=(100, 0, 0), prompt='Scenario name: ')

while not done:

    screen.fill((0, 0, 0))
    events = pygame.event.get()
    teclas = pygame.key.get_pressed()
    if state == "drawing":
        # --- Bucle principal de eventos


        for event in events:
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
               scenario.newFloor()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
               # scenario.addFloor()


        if pygame.mouse.get_pressed()[0] == 1:
            movimiento = pygame.mouse.get_rel()
            position = pygame.mouse.get_pos()
            # print(movimiento)
            if movimiento[0] != 0 or movimiento[1] != 0:
                # print(position)
                scenario.add(position)
                previousPosition= position

        # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ


        # if teclas[pygame.K_w]:
        #     # x=x+0.2
        #     avance = avance[0]+1, avance[1]
        if teclas[pygame.K_a]:
            # draw a few rectangles

            rect1 = pygame.draw.rect(screen, WHITE, (20, 20, 60, 60), 0)  # filled = 0
            rect2 = pygame.draw.rect(screen, WHITE, (100, 20, 60, 60), 3)  # not filled
        #     # y=y+0.2
        #     avance = avance[0], avance[1]+1

        #SAVE
        if teclas[pygame.K_s]:
            events = 0
            state = "saving"
            text = eztext.Input(maxlength=45, color=(150, 0, 0), prompt='Scenario name: ')

        # TEXT
        size = 20
        myfont = pygame.font.SysFont("calibri", size)
        # render text
        label = myfont.render("To save press \"s\"", 1, (0, 100, 255))
        screen.blit(label, (resolution[0] / 50, resolution[1] - size))
        label = myfont.render("To exit press esc", 1, (0, 100, 255))
        screen.blit(label, (resolution[0] / 50, resolution[1] - size * 2))

        # to exit
        if teclas[pygame.K_ESCAPE]:
            done=True


    scenario.draw(screen)

    if state == "saving" and events != 0:
        if teclas[pygame.K_RETURN] or teclas[K_KP_ENTER]:
            scenario.save(text.getInput())
            state = "drawing"
        text.update(events)
        text.draw(screen)

        # TEXT
        size = 20
        myfont = pygame.font.SysFont("calibri", size)
        # render text
        label = myfont.render("To save press enter", 1, (0, 100, 255))
        screen.blit(label, (resolution[0] / 50, resolution[1] - size))



    # t=reloj.get_time()
    # print(t)


    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ

    # # borra lo anterior





    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.

    pygame.display.flip()

    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    # print("iteracion")
    reloj.tick(10)

# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()
