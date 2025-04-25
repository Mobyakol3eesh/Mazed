import pygame as pg
from core.scene import Scene
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
from mesh.rotation_script import RotationScript 

class Mazed():
    def __init__(self, width=800, height=600):
        pg.init()
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLEBUFFERS, 1)
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLESAMPLES, 4)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        self.screen = pg.display.set_mode((width, height), DOUBLEBUF | OPENGL)
        self.objects = []
        self.fps = 60
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
        self.view = glm.translate(glm.mat4(1.0), glm.vec3(0, 0, -5))
        
        self.activeScene = None
    
   
        
    
    
        
    def drawScene(self,dt):
        self.activeScene.render(self.projection, self.view)
        self.activeScene.update(dt)
        
        
       
        
        
        
   
    def start(self):
        self.activeScene = Scene()
        cubeMesh = MeshFilter(Mesh("cube",cubeVertices,cubeIndices,cubeTexCoord,None))
        cube = self.activeScene.createGameObject("Cube",cubeMesh,MeshRenderer(Material("cube",None,textures=["wall.jpg"],shaderName="cube_shader")))
        cube.addComponent(RotationScript("RotationScript",))
        
       
        while self.running:
            
            for event in pg.event.get():
                if event.type == QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            
            dt = self.clock.tick(self.fps) / 1000.0
            self.drawScene(dt)
            pg.display.flip()
            self.clock.tick(self.fps)
            
        pg.quit()
        
    def setScene(self, scene):
        self.activeScene = scene


if __name__ == "__main__":
    Mazed().start()
    
