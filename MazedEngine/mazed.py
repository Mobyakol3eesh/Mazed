import pygame as pg
import trimesh

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

from MazedEngine.input import Input
from MazedGame.Scripts.camera_movment import cameraMovement
from mesh.plane import *
from mesh.objects_movment import objectMovement

class MazedEngine():
    def __init__(self, width=1200, height=800):
        pg.init()
        self.width = width
        self.height = height
        
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLEBUFFERS, 1)
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLESAMPLES, 4)
        trimesh.util.attach_to_log()
        
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
       
        pg.mouse.set_pos(width // 2, height // 2)
        self.screen = pg.display.set_mode((self.width, self.height), DOUBLEBUF | OPENGL)
        self.objects = []
        self.fps = 120
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
        self.mainCameraObject = self.activeScene.createGameObject("MainCamera",(-480,-70,500),Camera("MainCamera",near=0.1,far=2000.0,fov=70.0,aspect=self.width/self.height))
        self.mainCamera = self.mainCameraObject.getComponent(Camera)
     
        self.mainCameraObject.addComponent(cameraMovement("CameraMovment",self.input))
        
        plane = self.createPlane((0,0,0),textures=['wallborder.png'])
        plane.getComponent(Transform).scale(1000,1000,2000)
        plane.getComponent(Transform).rotateQ(90,0,0)
        for i in range(0,10):
            if(i == 3 or  i == 6 or i==7):
                continue
            plane = self.createPlane((-460 +  100 * i ,-60,400),textures=['wall.jpg'])
            plane.getComponent(Transform).scale(100,100,200)
        
        for i in range(0,7):
              
            plane = self.createPlane((-460 + 600 -60,-60,361 - i * 100),textures=["wall.jpg"])
            plane.getComponent(Transform).scale(100,100,200)
            plane.getComponent(Transform).rotateQ(0,90,0)
        
        for i in range(0,8):
            plane = self.createPlane((-460 + 700 -60,-60,361 - i * 100),textures=["wall.jpg"])
            plane.getComponent(Transform).scale(100,100,200)
            plane.getComponent(Transform).rotateQ(0,90,0)
        for i in range(0,5):
            plane = self.createPlane((-460 + 600 - i * 100, -60 ,-380))
            plane.getComponent(Transform).scale(100,100,200)
        
        for i in range(0,7):
            if(i == 3):
                continue
            plane = self.createPlane((-460 + 700 + 60,-60,340 - i * 100),textures=["wall.jpg"])
            plane.getComponent(Transform).scale(100,100,200)
            plane.getComponent(Transform).rotateQ(0,90,0)
        for i in range(0,4):
            plane = self.createPlane((-460 + 700 + i * 100, -60 ,360 -650))
            plane.getComponent(Transform).scale(100,100,200)
        for i in range (0,7):
            plane = self.createPlane((-460 + 250 , -60 ,361 -600 + i * 100))
            plane.getComponent(Transform).scale(100,100,200)
            plane.getComponent(Transform).rotateQ(0,90,0)
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
    
    def createPlane(self,position=(0,0,0),textures=["wall.jpg"]):
        planeMesh = MeshFilter(Mesh("plane",planeVertices,planeIndices,planeTexCoord,None))
        plane = self.activeScene.createGameObject("Plane",position,planeMesh,MeshRenderer(Material("plane",None,textures=textures,shaderName="basic_shader")))
        
        return plane
    def importMesh(self,meshName,position=(0,0,0)):
      
        mesh = trimesh.load_mesh(f"mazedgame/meshes/{meshName}.obj")
      
        print("Vertex range:", mesh.vertices.min(axis=0), mesh.vertices.max(axis=0))
        print("Face counts:", len(mesh.faces))
        mesh = MeshFilter(Mesh(meshName,mesh.vertices,mesh.faces,None,None))
        meshObject = self.activeScene.createGameObject(meshName,position,mesh,MeshRenderer(Material(meshName,[255,255,255],textures=[],shaderName="basic_shader")))

        
        
if __name__ == "__main__":
    MazedEngine().start()
    
