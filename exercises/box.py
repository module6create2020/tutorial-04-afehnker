import pygame
from pygame.locals import *


class Box:

    def __init__(self, x, y, h, w, max_x, max_y):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.max_x = max_x
        self.max_y = max_y
        self.color = (100, 100, 100)

    def update(self, input_keys, diameter):

        if K_UP in input_keys:
            if self.y > 0:
                self.y -= 1
        if K_DOWN in input_keys:
            if self.y + self.h < self.max_y:
                self.y += 1
        if K_LEFT in input_keys:
            if self.x > 0:
                self.x -= 1
        if K_RIGHT in input_keys:
            if self.x + self.w < self.max_x:
                self.x += 1

        # code to change th sie of the box
        if K_a in input_keys:
            if self.w > diameter:
                self.w -= 1
        if K_w in input_keys:
            if self.h > diameter:
                self.h -= 1
        if K_d in input_keys:
            if self.x + self.w < self.max_x:
                self.w += 1
        if K_s in input_keys:
            if self.y + self.h < self.max_y:
                self.h += 1

    def display(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.w, self.h])
