import pygame
import random
from pygame.locals                 import *
from OpenGL.GL                     import *
from .Cube                         import Cube
from .KeyboardEvent                import KeyboardEvent

class MainGame:

    def __init__(self, cube):
        self.max_distance = 100
        self.cube_quantity = 30
        self.cube_dict = {}
        self.color_index = []
        self.create_cube_dict(cube)
        self.create_color_index_tab()
    
    def create_cube_dict(self, cube):
        for x in range(self.cube_quantity):
            self.cube_dict[x] = cube.set_random_vertices(self.max_distance)

    def create_color_index_tab(self):
        for x in range(self.cube_quantity):
            self.color_index.append(random.randint(0, 6))

    def loop(self, cube, event):
        event.key_callback()
        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        camera_z = x[3][2]
        glTranslatef(event.x, event.y, event.game_speed)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        for each_cube, index in zip(self.cube_dict, self.color_index):
            if camera_z <= self.cube_dict[each_cube][0][2]:
                new_max = int(-1 * (camera_z - self.max_distance))
                self.cube_dict[each_cube] = cube.set_random_vertices(new_max, int(camera_z))
            cube.draw(self.cube_dict[each_cube], index, event.disco)
        pygame.display.flip()
        pygame.time.wait(10)