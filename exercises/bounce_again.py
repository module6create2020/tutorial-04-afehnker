import pygame
from pygame.locals import *
import sys
from exercises.keyboard_handler import KeyboardHandler
import random


class Game:
    """
    Initialize PyGame and create a graphical surface to write. Similar
    to void setup() in Processing
    """

    def __init__(self):
        pygame.init()

        # Below this line are the variables and objects fo the animation
        self.x = 100
        self.y = 100
        self.dx = random.uniform(-2, 2)
        self.dy = random.uniform(-2, 2)
        self.size = [800, 800]
        self.box = [100, 100, 600, 600]
        self.diameter = 50
        self.color = (250, 50, 50)

        # Loads a random system font
        self.font = pygame.font.SysFont(pygame.font.get_fonts()[0], 24)

        # Below this line are objects for timing, keyboard
        # handling and screen. Don't change this.
        self.time = pygame.time.get_ticks()
        self.keyboard_handler = KeyboardHandler()
        self.screen = pygame.display.set_mode(self.size)

    """
    Method 'game_loop' will be executed every frame to drive
    the display and handling of events in the background. 
    In Processing this is done behind the screen. Don't 
    change this, unless you know what you are doing.
    """

    def game_loop(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.time
        self.time = current_time
        self.handle_events()
        self.update_game(delta_time)
        self.draw_components()

    """
    Method 'update_game' is there to update the state of variables 
    and objects from frame to frame.
    """

    def update_game(self, dt):
        # code to update the position
        self.x += self.dx
        self.y += self.dy
        if self.x < self.box[0] and self.dx < 0:
            self.dx = - self.dx
        if self.y < self.box[1] and self.dy < 0:
            self.dy = - self.dy
        if self.x > self.box[0] + self.box[2] - self.diameter and self.dx > 0:
            self.dx = - self.dx
        if self.y > self.box[1] + self.box[3] - self.diameter and self.dy > 0:
            self.dy = - self.dy

        # code to change position of the box
        if K_UP in self.keyboard_handler.pressed:
            if self.box[1] > 0:
                self.box[1] -= 1
        if K_DOWN in self.keyboard_handler.pressed:
            if self.box[1] + self.box[3] < self.size[1]:
                self.box[1] += 1
        if K_LEFT in self.keyboard_handler.pressed:
            if self.box[0] > 0:
                self.box[0] -= 1
        if K_RIGHT in self.keyboard_handler.pressed:
            if self.box[0] + self.box[2] < self.size[0]:
                self.box[0] += 1

        # code to change th sie of the box
        if K_a in self.keyboard_handler.pressed:
            if self.box[2] > self.diameter:
                self.box[2] -= 1
        if K_w in self.keyboard_handler.pressed:
            if self.box[3] > self.diameter:
                self.box[3] -= 1
        if K_d in self.keyboard_handler.pressed:
            if self.box[0] + self.box[2] < self.size[0]:
                self.box[2] += 1
        if K_s in self.keyboard_handler.pressed:
            if self.box[1] + self.box[3] < self.size[0]:
                self.box[3] += 1


    """
    Method 'draw_components' is similar is meant to contain 
    everything that draws one frame. It is similar to method
    void draw() in Processing. Put all draw calls here. Leave all
    updates in method 'update'
    """

    def draw_components(self):
        # fill the screen and draw the rectangle in it
        self.screen.fill([255, 255, 255])
        #draw the box
        pygame.draw.rect(self.screen, (100, 100, 100), self.box)
        # draw ball
        pygame.draw.ellipse(self.screen, self.color, [[self.x, self.y], [self.diameter, self.diameter]])
        text = self.font.render("!", True, (255, 255, 255))
        self.screen.blit(text, (self.x + 22, self.y + 12))

        # updates the entire surface (canvas). Keep it.
        pygame.display.flip()

    def reset(self):
        pass

    """
    Method 'handle_event' loop over all the event types and 
    handles them accordingly. 
    In Processing this is done behind the screen. Don't 
    change this, unless you know what you are doing.
    """

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.handle_key_down(event)
            if event.type == pygame.KEYUP:
                self.handle_key_up(event)
            if event.type == pygame.MOUSEMOTION:
                self.handle_mouse_motion(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_pressed(event)
            if event.type == pygame.MOUSEBUTTONUP:
                self.handle_mouse_released(event)

    """This method will store a currently pressed buttons 
    in list 'keyboard_handler.pressed'."""

    def handle_key_down(self, event):
        self.keyboard_handler.key_pressed(event.key)


    """This method will remove a released button 
        from list 'keyboard_handler.pressed'."""

    def handle_key_up(self, event):
        self.keyboard_handler.key_released(event.key)

    def handle_mouse_motion(self, event):
        """Similar to void mouseMoved() in Processing"""
        pass

    def handle_mouse_pressed(self, event):
        """Similar to void mousePressed() in Processing"""
        pass

    def handle_mouse_released(self, event):
        """Similar to void mouseReleased() in Processing"""
        pass


if __name__ == "__main__":
    g = Game()
    while True:
        g.game_loop()
