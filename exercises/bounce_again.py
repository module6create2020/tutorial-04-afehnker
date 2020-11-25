import pygame
from pygame.locals import *
import sys
from exercises.keyboard_handler import KeyboardHandler
import random
from exercises.bubble import Bubble
from exercises.box import Box


class Game:
    """
    Initialize PyGame and create a graphical surface to write. Similar
    to void setup() in Processing
    """

    def __init__(self):
        pygame.init()

        # Below this line are the variables and objects fo the animation
        self.size = [800, 800]
        self.diameter = 50;
        self.balls = [];
        for i in range(10):
            self.balls.append(Bubble(200, 200, (random.randrange(0, 255), self.diameter, self.diameter)))
        self.box = Box(100, 100, 600, 600, self.size[0], self.size[1])

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
        for b in self.balls:
            b.move(self.box)
            for b2 in self.balls:
                b.collide(b2)
        # code to change position and size of the box
        self.box.update(self.keyboard_handler.pressed, self.diameter)

    """
    Method 'draw_components' is similar is meant to contain 
    everything that draws one frame. It is similar to method
    void draw() in Processing. Put all draw calls here. Leave all
    updates in method 'update'
    """

    def draw_components(self):
        # fill the screen and draw the rectangle in it
        self.screen.fill([255, 255, 255])
        self.box.display(self.screen)
        # draw ball
        for b in self.balls:
            b.display(self.screen, self.font)

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
