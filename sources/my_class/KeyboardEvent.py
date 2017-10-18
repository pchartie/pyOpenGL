import pygame
from pygame.locals      import *
from utils              import my_quit

class KeyboardEvent:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.game_speed = 0.5
        self.disco = 0

    def key_callback(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                my_quit()
            elif event.type == pygame.KEYDOWN:
                self.key_down(event)
            elif event.type == pygame.KEYUP:
                self.key_up(event)
        self.key_pressed()

    def key_pressed(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_a]:
            self.x += 0.10
        if keys_pressed[K_d]:
            self.x -= 0.10
        if keys_pressed[K_w]:
            self.y -= 0.10
        if keys_pressed[K_s]:
            self.y += 0.10
        if keys_pressed[K_LSHIFT]:
            self.game_speed = 1.5

    def key_up(self, event):
        if event.key == pygame.K_a or event.key == pygame.K_d:
            self.x = 0
        if event.key == pygame.K_w or event.key == pygame.K_s:
            self.y = 0
        if event.key == pygame.K_LSHIFT:
            self.game_speed = 0.5
    
    def key_down(self, event):
        if event.key == pygame.K_ESCAPE:
            my_quit()
        if event.key == pygame.K_SPACE:
            if self.disco == 1:
                self.disco = 0
            else:
                self.disco = 1
