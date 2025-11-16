from Data.player_profile import userprofile, saveUserProfile
from GUI.gui_classes import Button, Entry
import pygame
import sys


def chooseClass():
    pygame.init()
    screen = pygame.display.set_mode((650, 500))
    pygame.display.set_caption("Legends of Pythonia")
    background = pygame.image.load("assets/blackscreen.jpg")
    background = pygame.transform.scale(background, (650, 500))
    font = pygame.font.Font("assets/BoldPixels.ttf", 50)
    class_select_text_font = pygame.font.Font("assets/BoldPixels.ttf", 75)
    class_select_text = class_select_text_font.render(
        "Choose a class", True, (255, 255, 255))
    warriorButton = Button(75, 250, 200, 50, "Warrior", font,
                           (0, 0, 0, 0), (255, 165, 0, 100), (255, 255, 255))
    mageButton = Button(325, 250, 200, 50, "Mage", font,
                        (0, 0, 0, 0), (255, 165, 0, 100), (255, 255, 255))
    rogueButton = Button(75, 300, 200, 50, "Rogue", font,
                         (0, 0, 0, 0), (255, 165, 0, 100), (255, 255, 255))
    archerButton = Button(325, 300, 200, 50, "Archer", font,
                          (0, 0, 0, 0), (255, 165, 0, 100), (255, 255, 255))
    tankButton = Button(75, 350, 200, 50, "Tank", font,
                        (0, 0, 0, 0), (255, 165, 0, 100), (255, 255, 255))
    summonerButton = Button(325, 350, 200, 50, "Summoner",
                            font, (0, 0, 0, 0), (255, 165, 0, 100), (255, 255, 255))
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(background, (0, 0))
        screen.blit(class_select_text, (75, 50))
        if warriorButton.draw(screen):
            userprofile["class"] = "warrior"
            saveUserProfile()
            running = False
        if mageButton.draw(screen):
            userprofile["class"] = "mage"
            saveUserProfile()
            running = False
        if rogueButton.draw(screen):
            saveUserProfile()
            running = False
        if archerButton.draw(screen):
            userprofile["class"] = "archer"
            saveUserProfile()
            running = False
        if tankButton.draw(screen):
            userprofile["class"] = "tank"
            saveUserProfile()
            running = False
        if summonerButton.draw(screen):
            userprofile["class"] = "summoner"
            saveUserProfile()
            running = False
        pygame.display.flip()


def chooseName():
    pygame.init()
    screen = pygame.display.set_mode((650, 500))
    pygame.display.set_caption("Legends of Pythonia")
    background = pygame.image.load("assets/blackscreen.jpg")
    background = pygame.transform.scale(background, (650, 500))
    font = pygame.font.Font("assets/BoldPixels.ttf", 50)
    name_select_entry = Entry(75, 50, 500, 60, font,
                              placeholder="What is your name?")
    confirm_button = Button(200, 125, 200, 50, "Confirm",
                            font, (0, 0, 0, 0), (255, 165, 0, 100), (255, 255, 255))
    running = True
    while running == True:
        for event in pygame.event.get():
            name_select_entry.handle_event(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(background, (0, 0))
        name_select_entry.draw(screen)
        if confirm_button.draw(screen):
            userprofile["name"] = name_select_entry.get_text()
            saveUserProfile()
            running = False
        pygame.display.flip()


def confirmUserData():
    pygame.init()
    screen = pygame.display.set_mode((650, 500))
    pygame.display.set_caption("Legends of pythonia")
    background = pygame.image.load("assets/blackscreen.jpg")
    background = pygame.transform.scale(background, (650, 500))
    font = pygame.font.Font("assets/BoldPixels.ttf", 50)
    character_confirm_text = font.render(
        f'Is this correct?', True, (255, 255, 255))
    character_confirm_text_class = font.render(
        f'Class = "{userprofile["class"]}"', True, (255, 255, 255))
    character_confirm_text_name = font.render(
        f'Name = "{userprofile["name"]}"', True, (255, 255, 255))
    character_confirm_button_yes = Button(
        200, 250, 200, 50, "Yes", font, (0, 0, 0, 0), (255, 165, 0, 100), (255, 255, 255))
    character_confirm_button_no = Button(
        200, 300, 200, 50, "No", font, (0, 0, 0, 0), (255, 165, 0, 100), (255, 255, 255))
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(background, (0, 0))
        screen.blit(character_confirm_text, (140, 50))
        screen.blit(character_confirm_text_class, (140, 100))
        screen.blit(character_confirm_text_name, (140, 150))
        if character_confirm_button_yes.draw(screen):
            return True
        if character_confirm_button_no.draw(screen):
            return False
        pygame.display.flip()
