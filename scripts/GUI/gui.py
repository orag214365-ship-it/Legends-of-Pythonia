import pygame
import sys
from GUI.gui_classes import Button


def testScreen():
    pygame.init()
    screen = pygame.display.set_mode((650, 500))
    pygame.display.set_caption("Legends of Pythonia")
    font = pygame.font.Font("assets/BoldPixels.ttf", 50)
    button = Button(150, 120, 100, 50, "Click", font,
                    (70, 130, 180), (100, 160, 210), (255, 255, 255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        screen.fill((255, 0, 0))

        if button.draw(screen):
            pygame.quit()
            sys.exit(0)

        pygame.display.flip()


def startScreen():
    pygame.init()
    screen = pygame.display.set_mode((650, 500))
    pygame.display.set_caption("Legends of Pythonia")
    font = pygame.font.Font("assets/BoldPixels.ttf", 50)
    startGameButton = Button(205, 300, 200, 50, "Start!",
                             font, (0, 0, 0, 0), (255, 165, 0, 100), (0, 0, 0))

    background = pygame.image.load("assets/startscreen.png")
    background = pygame.transform.scale(background, (650, 500))

    running = True

    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background, (0, 0))
        if startGameButton.draw(screen):
            running = False
        pygame.display.flip()
