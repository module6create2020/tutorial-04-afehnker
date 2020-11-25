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
        dist_now = math.sqrt(math.pow(self.x-other.x,2)+math.pow(self.y-other.y,2))
        dist_next = math.sqrt(math.pow(self.x+self.dx-other.x-other.dx,2)+math.pow(self.y+self.dy-other.y-other.dy,2))
        minDist = (self.diameter + other.diameter) / 2

        if not(self is other) and dist_now < minDist and dist_next < dist_now:
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



