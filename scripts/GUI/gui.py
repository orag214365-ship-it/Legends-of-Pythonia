import pygame
import sys
from GUI.gui_classes import Button, DialogueBox


def testScreen():
    pygame.init()
    screen = pygame.display.set_mode((650, 500))
    pygame.display.set_caption("Legends of Pythonia")
    font = pygame.font.Font("assets/BoldPixels.ttf", 50)
    button = Button(150, 120, 100, 50, "Click", font,
                    (70, 130, 180), (100, 160, 210), (255, 255, 255))
    dialogue = DialogueBox(200, 200, 300, 50, font,
                           (255, 255, 255), (0, 0, 0), 0.05)
    dialogue.set_text("This is a test")
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            dialogue.handle_event(event)

        dialogue.update()
        dialogue.draw(screen)

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        screen.fill((255, 0, 0))

        if button.draw(screen):
            pygame.quit()
            sys.exit(0)

        pygame.display.flip()
        clock.tick(60)


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


def tutorial():
    pygame.init()
    screen = pygame.display.set_mode((650, 500))
    pygame.display.set_caption("Legends of Pythonia")
    font = pygame.font.Font("assets/BoldPixels.ttf", 50)
    tut_dialouge_text = "Hello press me to progress"
    tut_dialouge_box = DialogueBox(
        50, 300, 500, 50, tut_dialouge_text, font, (0, 0, 0, 0), (255, 165, 0, 100), (255, 255, 255))

    backgound = pygame.image.load("assets/blackscreen.jpg")
    backgound = pygame.transform.scale(backgound, (650, 500))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(backgound, (0, 0))
        for i in range(3):
            if tut_dialouge_box.draw(screen):
                tut_dialouge_text = "We are no gonna start the fighting tutorial"

        pygame.display.flip()
