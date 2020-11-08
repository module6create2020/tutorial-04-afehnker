import pygame
import math
from pygame.locals import *
import random


class Bubble:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.dx = random.uniform(-1, 1)
        self.dy = random.uniform(-1, 1)
        self.color = color
        self.diameter = 50

    def move(self, box):
        self.x += self.dx
        self.y += self.dy
        if self.x < box.x and self.dx < 0:
            self.dx = - self.dx
        if self.y < box.y and self.dy < 0:
            self.dy = - self.dy
        if self.x + self.diameter > box.x + box.w and self.dx > 0:
            self.dx = - self.dx
        if self.y + self.diameter > box.y + box.h and self.dy > 0:
            self.dy = - self.dy

    def display(self, screen, font):
        pygame.draw.ellipse(screen, self.color, [[self.x, self.y], [50, 50]])
        text = font.render("!", True, (255, 255, 255))
        screen.blit(text, (self.x + 22, self.y + 12))

    def collide(self, other):
        if not (self is other):
            dist_now = math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))
            dist_next = math.sqrt(
                math.pow(self.x + self.dx - other.x - other.dx, 2) + math.pow(self.y + self.dy - other.y - other.dy, 2))

            if dist_now < 50 and dist_next < dist_now:
                numerator = (self.dx - other.dx) * (self.x - other.x) + (self.dy - other.dy) * (self.y - other.y)
                denominator = math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2)
                temp1dx = self.dx - numerator / denominator * (self.x - other.x)
                temp1dy = self.dy - numerator / denominator * (self.y - other.y)
                temp2dx = other.dx - numerator / denominator * (other.x - self.x)
                temp2dy = other.dy - numerator / denominator * (other.y - self.y)

                self.dx = temp1dx
                self.dy = temp1dy
                other.dx = temp2dx
                other.dy = temp2dy


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
