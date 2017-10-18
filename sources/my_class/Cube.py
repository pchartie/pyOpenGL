import random
from OpenGL.GL          import *

colors = (
        (0,0,1),
        (0,1,0),
        (0,1,1),
        (1,0,0),
        (1,0,1),
        (1,1,0),
        (1,1,1),
    )

class Cube:

    def __init__(self, path):
        self.path = path
        self.vertices = []
        self.faces = []
        self.get_vertices();
        self.get_faces();
        pass

    def get_vertices(self):
        with open(self.path, 'r') as f:
            for line in f:
                first_split = line.split(' ')
                if first_split[0] == 'v':
                    second_split = line.split(' ')   
                    self.vertices.append(list(map(float, second_split[1:4])))

    def get_faces(self):
        with open(self.path, 'r') as f:
            for line in f:
                first_split = line.split(' ')
                if first_split[0] == 'f':
                    if len(first_split) == 5:
                        self.faces.append(int(first_split[1]))
                        self.faces.append(int(first_split[2]))
                        self.faces.append(int(first_split[4]))
                        self.faces.append(int(first_split[2]))
                        self.faces.append(int(first_split[3]))
                        self.faces.append(int(first_split[4]))
                    elif len(first_split) == 4:
                        self.faces.append(int(first_split[1]))
                        self.faces.append(int(first_split[2]))
                        self.faces.append(int(first_split[3]))

    def set_random_vertices(self, max_distance, min_distance = -20):
        random_x = random.randrange(-15,15)
        random_y = random.randrange(-15,15)
        random_z = random.randrange(-1 * max_distance, min_distance)
        random_vertices = []
        for vertice in self.vertices:
            x = vertice[0] + random_x
            y = vertice[1] + random_y
            z = vertice[2] + random_z
            random_vertices.append([x, y, z])
        return random_vertices

    def draw(self, random_vertices, index, disco):
        glBegin(GL_TRIANGLES)
        if disco == 1:
            index = random.randint(0, 6)
        for face in self.faces:
            glColor3fv(colors[index])
            glVertex3fv(random_vertices[face -1])
        glEnd()
