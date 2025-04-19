import sys
import os

# Check the resolved pat
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame as pg
from opengl_utilities import OpenGLUtilities
from mesh.triangle import Triangle
from pygame.locals import *
from OpenGL.GL import *





class Main():
    def __init__(self, width=800, height=600):
        pg.init()
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLEBUFFERS, 1)
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLESAMPLES, 4)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        self.program = None
        self.screen = pg.display.set_mode((width, height), DOUBLEBUF | OPENGL)
        self.clock = pg.time.Clock() 
        self.running = True
       
    
    def render_triangle(self):
        triangle = Triangle()
        self.program = OpenGLUtilities.create_program(triangle.vertexShaderID, triangle.fragmentShaderID)
        return triangle
    
    def update(self,triangle):
        glUseProgram(self.program)
        glBindVertexArray(triangle.vertexArrayID)
        glDrawArrays(GL_TRIANGLES, 0 , 3)
        
        
        
    def start(self):
        triangle =  self.render_triangle()
        while self.running:
            for event in pg.event.get():
                if event.type == QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.update(triangle)
            pg.display.flip()
            self.clock.tick(60)
            
        pg.quit()

if __name__ == "__main__":
    Main().start()