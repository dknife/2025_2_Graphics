from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

class Sphere:
    def __init__(self, radius=1.0, slices=16, stacks=16):
        self.radius = radius
        self.slices = slices  # Number of divisions around the z-axis (longitude)
        self.stacks = stacks  # Number of divisions along the z-axis (latitude)

    def draw(self):
        
        # Loop through the stacks (latitude lines)
        for i in range(self.stacks + 1):
            lat = np.pi * (-0.5 + float(i) / self.stacks)  # Latitude angle in radians
            sin_lat = np.sin(lat)
            cos_lat = np.cos(lat)

            # Loop through the slices (longitude lines)
            glBegin(GL_LINE_LOOP)
            for j in range(self.slices):
                lon = 2 * np.pi * float(j) / self.slices  # Longitude angle in radians
                x = self.radius * cos_lat * np.cos(lon)
                y = self.radius * cos_lat * np.sin(lon)
                z = self.radius * sin_lat

                glVertex3f(x, y, z)
            glEnd()

        # Loop through the slices (longitude lines)
        for i in range(self.slices):
            lon = 2 * np.pi * float(i) / self.slices  # Longitude angle in radians
            sin_lon = np.sin(lon)
            cos_lon = np.cos(lon)

            # Loop through the stacks (latitude lines)
            glBegin(GL_LINE_LOOP)
            for j in range(self.stacks + 1):
                lat = np.pi * (-0.5 + float(j) / self.stacks)  # Latitude angle in radians
                x = self.radius * np.cos(lat) * cos_lon
                y = self.radius * np.cos(lat) * sin_lon
                z = self.radius * np.sin(lat)

                glVertex3f(x, y, z)
            glEnd()