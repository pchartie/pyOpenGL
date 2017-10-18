import pygame
import random
from pygame.locals      import *
from OpenGL.GL          import *
from OpenGL.GLU         import *

WIDTH       = 800
HEIGHT      = 600
FOV         = 45
NEAR_PLAN   = 0.1
FAR_PLAN    = 50

def gl_init():
    pygame.init()
    display = (WIDTH, HEIGHT)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(FOV, (display[0]/display[1]), NEAR_PLAN, FAR_PLAN)
    glTranslatef(random.randrange(-5, 5), random.randrange(-5, 5), -40)
    glEnable(GL_DEPTH_TEST)
    # trouver l'antialiasing !
    print('Renderer: ' + str(glGetString(GL_RENDERER)))
    print('OpenGL version supported ' + str(glGetString(GL_VERSION)))