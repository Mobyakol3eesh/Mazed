import pygame as pg
from MazedEngine.scene import Scene
from mesh.mesh_renderer import MeshRenderer
from mesh.mesh_filter import MeshFilter
from mesh.material import Material
from pygame.locals import *
from mesh.game_object import GameObject
from OpenGL.GL import *
from math import *
import glm
from MazedEngine.camera import Camera
from mesh.cube import *
from mesh.mesh import Mesh
from mesh.rotation_script import RotationScript 
from MazedGame.Scripts.rotate_camera import RotateCamera
from MazedEngine.input import Input
from MazedGame.Scripts.camera_movment import cameraMovement


class MazedEngine():
    def __init__(self, width=800, height=600):
        pg.init()
        self.width = width
        self.height = height
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLEBUFFERS, 1)
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLESAMPLES, 4)
       
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.mouse.set_pos(width // 2, height // 2)
        self.screen = pg.display.set_mode((self.width, self.height), DOUBLEBUF | OPENGL)
        self.objects = []
        self.fps = 60
        glViewport(0, 0, self.width, self.height)
        glEnable(GL_DEPTH_TEST)
        self.clock = pg.time.Clock() 
        self.time = pg.time
        self.running = True
        self.input = Input()
        self.activeScene = None
        
    
   
        
    
    
        
    def drawScene(self,dt):
        
        self.activeScene.render(self.mainCamera.projection,self.mainCamera.view)
        self.activeScene.update(dt)
        
        
       
        
        
        
   
    def start(self):
        self.activeScene = Scene()
        self.mainCameraObject = self.activeScene.createGameObject("MainCamera",(0,0,9),Camera("MainCamera",near=0.1,far=100.0,fov=45.0,aspect=self.width/self.height))
        self.mainCamera = self.mainCameraObject.getComponent(Camera)
        self.mainCameraObject.addComponent(RotateCamera("RotateCamera",speed=1.0))
        self.mainCameraObject.addComponent(cameraMovement("CameraMovment",self.input))
        cube = self.createCube((0,0,0))
        cube.addComponent(RotationScript("RotationScript",))
        cube = self.createCube((2,0,0))
        cube.addComponent(RotationScript("RotationScript",))
        cube = self.createCube((-2,0,0))
        cube.addComponent(RotationScript("RotationScript",))
        cube = self.createCube((0,2,0))
        cube.addComponent(RotationScript("RotationScript",))
        cube = self.createCube((0,-2,3))
        cube.addComponent(RotationScript("RotationScript",))
        cube = self.createCube((0,0,-2))
        
        while self.running:
            
            self.input.update()
            self.running = self.input.runningState()
            if self.running == False:
                pg.quit()
                exit()
                break
                
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            
            dt = self.clock.tick(self.fps) / 1000.0
            
            self.drawScene(dt)
            pg.display.flip()
            self.clock.tick(self.fps)
            
        pg.quit()
        
    def setScene(self, scene):
        self.activeScene = scene
        
    def createCube(self,position=(0,0,0)):
        cubeMesh = MeshFilter(Mesh("cube",cubeVertices,cubeIndices,cubeTexCoord,None))
        cube = self.activeScene.createGameObject("Cube",position,cubeMesh,MeshRenderer(Material("cube",None,textures=["wall.jpg"],shaderName="basic_shader")))
        return cube
        

if __name__ == "__main__":
    MazedEngine().start()
    
