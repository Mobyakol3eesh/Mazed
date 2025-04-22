import pygame as pg
from opengl_utilities import OpenGLUtilities
from mesh.triangle import Triangle
from pygame.locals import *
from OpenGL.GL import *
from math import *




class Mazed():
    def __init__(self, width=800, height=600):
        pg.init()
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLEBUFFERS, 1)
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLESAMPLES, 4)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        self.screen = pg.display.set_mode((width, height), DOUBLEBUF | OPENGL)
        self.objects = []
        glViewport(0, 0, width, height)
        self.clock = pg.time.Clock() 
        self.time = pg.time
        self.running = True
       
    
   
        
    
    
        
    def draw_mesh(self,mesh):
        timems = self.time.get_ticks() / 1000.0
        # mesh.transform.rotateQGlobal(0,0,1 * sin(timems) * 0.5)
        # mesh.transform.rotateQ(0,0,sin(timems))
        # mesh.transform.rotateQ(0,0,sin(timems))
        mesh.transform.rotateQ(0,cos(timems),0,False)
        glBindVertexArray(mesh.glBuffer.vertexArrayID)
        glDrawElements(GL_TRIANGLES, len(mesh.indices), GL_UNSIGNED_INT, None)
        glBindVertexArray(0)
        
   
    def start(self):
        mesh = Triangle(textures=['wall.jpg'])
        mesh.AddTexture('awesomeface.png')
        mesh.transform.translate(0.2, 0.0, 0.0)
        mesh.transform.rotateQ(80,0,0) 
       
        
       
       
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
    Mazed().start()
    
