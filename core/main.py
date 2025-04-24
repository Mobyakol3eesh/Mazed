import pygame as pg

from mesh.mesh_renderer import MeshRenderer
from mesh.mesh_filter import MeshFilter
from mesh.material import Material
from pygame.locals import *
from mesh.game_object import GameObject
from OpenGL.GL import *
from math import *
import glm
from mesh.cube import *
from mesh.mesh import Mesh

class Mazed():
    def __init__(self, width=800, height=600):
        pg.init()
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLEBUFFERS, 1)
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLESAMPLES, 4)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        self.screen = pg.display.set_mode((width, height), DOUBLEBUF | OPENGL)
        self.objects = []
        glViewport(0, 0, width, height)
        glEnable(GL_DEPTH_TEST)
        self.clock = pg.time.Clock() 
        self.time = pg.time
        self.running = True
        self.fov = 45.0
        self.near = 0.1
        self.far = 100.0
        self.aspect = width / height
        self.projection = glm.perspective(glm.radians(self.fov), self.aspect, self.near, self.far)
        self.view = glm.mat4(1.0)
        
    
   
        
    
    
        
    def drawGameObject(self, gameObject : GameObject ):
        timems = self.time.get_ticks() / 1000.0
        # mesh.transform.rotateQGlobal(0,0,1 * sin(timems) * 0.5)
        # mesh.transform.rotateQ(0,0,sin(timems))
        # mesh.transform.rotateQ(0,0,sin(timems))
        # mesh.transform.rotateQ(0,sin(timems) + 2,0)
        
        
        gameObject.getComponent(Transform).rotateQ(0,1,0)
       
        gameObject.getComponent(MeshRenderer).render(gameObject.getComponent(Transform),self.projection, self.view)
        
        glBindVertexArray(gameObject.getComponent(MeshRenderer).vao)
        glDrawElements(GL_TRIANGLES, len(gameObject.getComponent(MeshFilter).mesh.indices), GL_UNSIGNED_INT, None)
        glBindVertexArray(0)
        
   
    def start(self):
        # mesh = Triangle(textures=['wall.jpg'])
        # mesh.AddTexture('awesomeface.png')
        # mesh.transform.translate(0.0, 0.5, 0.0)
        
        # mesh.transform.scale(0.5, 0.5, 1)
        # mesh.transform.translate(0.5, 0.0, 0.0)
        # mesh.transform.scale(1,1,1)
        cubeMesh = MeshFilter(Mesh("cube", cubeVertices, cubeIndices, cubeTexCoord, None))
        
        
        cube2 = GameObject("cube2", position=(2,0,-5))
        cube2.addComponent(cubeMesh)
        cube2.addComponent(MeshRenderer(cubeMesh, Material("cube",None,  textures=['wall.jpg'], shaderName='cube_shader')))
        cube = GameObject("cube", position=(0,0,-5))
        cube.addComponent(cubeMesh)
        cube.addComponent(MeshRenderer(cubeMesh, Material("cube",[1,0,0], textures=[] , shaderName='cube_shader')))
    
        cube.getComponent(Transform).rotateQ(45, 0, 0)
        cube.getComponent(Transform).scale(1, 1,1)
        cube.getComponent(MeshRenderer).material.addTexture('wall.jpg')
        cube.getComponent(MeshRenderer).material.addTexture('awesomeface.png')
        
        cube3 = GameObject("cube3", position=(-2,0,-5))
        cube3.addComponent(cubeMesh)
        cube3.addComponent(MeshRenderer(cubeMesh, Material("cube",[1,1,0], textures=[] , shaderName='cube_shader')))
    
        
       
        while self.running:
            
            for event in pg.event.get():
                if event.type == QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.drawGameObject(cube)
            self.drawGameObject(cube2)
            self.drawGameObject(cube3)
            pg.display.flip()
            self.clock.tick(60)
            
        pg.quit()
        



if __name__ == "__main__":
    Mazed().start()
    
