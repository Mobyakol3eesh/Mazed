import pygame as pg
from opengl_utilities import OpenGLUtilities
from mesh.triangle import Triangle
from pygame.locals import *
from OpenGL.GL import *
from math import *




class Main():
    def __init__(self, width=800, height=600):
        pg.init()
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLEBUFFERS, 1)
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLESAMPLES, 4)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        self.screen = pg.display.set_mode((width, height), DOUBLEBUF | OPENGL)
        self.clock = pg.time.Clock() 
        self.time = pg.time
        self.running = True
       
    
   
        
    
    
        
    def draw_mesh(self,mesh):
        mesh.shader.use()
        glBindVertexArray(mesh.glBuffer.vertexArrayID)
        glDrawElements(GL_TRIANGLES, len(mesh.indices), GL_UNSIGNED_INT, None)
        glBindVertexArray(0)
        
        
        
    def start(self):
        mesh = Triangle()
       
        while self.running:
            for event in pg.event.get():
                if event.type == QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.draw_mesh(mesh)
            
            pg.display.flip()
            self.clock.tick(60)
            
        pg.quit()
        



if __name__ == "__main__":
    Main().start()
    
