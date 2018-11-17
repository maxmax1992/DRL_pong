# PyGame template.

# Import standard modules.
import sys

# Import non-standard modules.
import pygame
from pygame.locals import *
import numpy as np
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)



class Player():
    def __init__(self, location, isRight, controllable=False):
        self.isRightt = isRight
        self.loc = location
    
    def draw(self, screen):
        pass

    def update(self):
        pass
        

class Ball():
    def __init__(self, loc):
        self.location = loc
        self.dir = np.random.uniform(0, 2*np.pi)
        # print(self.dir)
        self.speed = 200
    
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.getLoc(), 30, 1)

    def getLoc(self):
        loc = (int(np.round(self.location[0])), int(np.round(self.location[1])))
        return loc

    def update(self, dt):
        # print(dt)
        dx = np.cos(self.dir)*self.speed*dt/1000
        dy = np.sin(self.dir)*self.speed*dt/1000
        # print(dy, dx)
        # print(dx, dy)
        self.location = (self.location[0] + dx, self.location[1] + dy)
        

class Game:
    def __init__(self, ballpos, player1pos, player2pos):
        speed = 1
        self.ball = Ball(loc=ballpos)
        self.p1 = Player(player1pos, isRight=True, controllable=True)
        self.p2 = Player(player2pos, isRight=False, controllable=True)

    def draw(self, screen):
        screen.fill(BLACK)  # Fill the screen with black.
        self.p1.draw(screen)
        self.p2.draw(screen)
        self.ball.draw(screen)
        
        # self.ball.draw(screen)
        # Flip the display so that the things we drew actually show up.
        pygame.display.flip()

    def update(self, dt):
        """
        Update game. Called once per frame.
        dt is the amount of time passed since last frame.
        If you want to have constant apparent movement no matter your framerate,
        what you can do is something like

        x += v * dt

        and this will scale your velocity based on time. Extend as necessary."""
        self.ball.update(dt)
        # Go through events that are passed to the script by the window.
        for event in pygame.event.get():
            # We need to handle these events. Initially the only one you'll want to care
            # about is the QUIT event, because if you don't handle it, your game will crash
            # whenever someone tries to exit.
            if event.type == QUIT:
                pygame.quit()  # Opposite of pygame.init
                sys.exit()  # Not including this line crashes the script on Windows. Possibly
                # on other operating systems too, but I don't know for sure.
            # Handle other events as you wish.


def drawScreen(screen):
    """
    Draw things to the window. Called once per frame.
    """
    screen.fill(BLACK)  # Fill the screen with black.
    

    # Flip the display so that the things we drew actually show up.
    pygame.display.flip()


def runPyGame():
    # Initialise PyGame.
    pygame.init()

    # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
    fps = 60.0
    fpsClock = pygame.time.Clock()

    # Set up the window.
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))

    # screen is the surface representing the window.
    # PyGame surfaces can be thought of as screen sections that you can draw onto.
    # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.
    ballpos = (width//2, height//2)
    p1pos = (0, height//2)
    p2pos = (width, height//2)

    game = Game(ballpos, p1pos, p2pos)
    # Main game loop.
    dt = 1/fps  # dt is the time since last frame.
    while True:  # Loop forever!
        game.draw(screen)
        game.update(dt)
        # You can update/draw here, I've just moved the code for neatness.
        
        # update(dt)
        # draw(screen)


        dt = fpsClock.tick(fps)



if __name__ == '__main__':
    runPyGame()
