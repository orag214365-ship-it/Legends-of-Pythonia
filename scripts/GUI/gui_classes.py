import pygame


class Button:
    def __init__(self, x, y, width, height, text, font, color, hover_color, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        current_color = self.hover_color if self.rect.collidepoint(
            mouse_pos) else self.color

        temp = pygame.Surface(
            (self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.rect(temp, current_color,
                         (0, 0, self.rect.width, self.rect.height))
        surface.blit(temp, self.rect.topleft)
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        if self.rect.collidepoint(mouse_pos) and mouse_click[0]:
            return True
        return False


class Entry:
    def __init__(self, x, y, w, h, font, placeholder=""):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactive = (120, 120, 120)
        self.color_active = (255, 165, 0)
        self.color = self.color_inactive
        self.text = ""
        self.font = font
        self.active = False
        self.placeholder = placeholder

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def draw(self, surface):
        if self.text:
            txt_surf = self.font.render(self.text, True, (255, 255, 255))
        else:
            txt_surf = self.font.render(
                self.placeholder, True, (150, 150, 150))

        surface.blit(txt_surf, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(surface, self.color, self.rect, 2)

    def get_text(self):
        return self.text