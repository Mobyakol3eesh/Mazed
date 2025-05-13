import pygame as pg
import trimesh
from MazedEngine.box_collider import BoxCollider
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
from mesh.plane import *
from MazedEngine.input import Input
from MazedGame.Scripts.camera_movment import cameraMovement
from mesh.wall import *
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
        
        self.colliders = []
    
    
        
    def drawScene(self,dt):
     
        self.activeScene.render(self.mainCamera.projection,self.mainCamera.view)
        self.activeScene.update(dt)
        
        
       
    def win(self,other):
        
        if other.gameObject.name == "treasure":
            print("You win!")
            self.running = False
            pg.quit()
            exit()
        
        
   
    def start(self):
        self.activeScene = Scene()
        self.mainCameraObject = self.activeScene.createGameObject("MainCamera",(-480,-70,500),Camera("MainCamera",near=0.1,far=5000.0,fov=70.0,aspect=self.width/self.height))
        self.mainCamera = self.mainCameraObject.getComponent(Camera)
     
        self.mainCameraObject.addComponent(cameraMovement("CameraMovment",self.input))
        boxCollider = BoxCollider("activeCollider",position=self.mainCameraObject.getComponent(Transform).position, scale=[1,1,1])
        boxCollider.onCollisionEnter = self.win                    
        self.mainCameraObject.addComponent(boxCollider)
        self.colliders.append(self.mainCameraObject.getComponent(BoxCollider))
        
       
        
        plane = self.createPlane((0,-100,0),color=[255,242,92],textures=["floorgrad.jpg"])
        plane.getComponent(Transform).scale(4000,0,2000)
        
        
        plane = self.createPlane((0,120,0),color=[255,246,143],textures=["roofgrad.jpg"])
        plane.getComponent(Transform).scale(4000,0,2000)
        
        plane = self.createPlane((2000,0,0),color=[255,250,194],textures=["wallgrad.jpg"])
        plane.getComponent(Transform).scale(250,0,2000)
        plane.getComponent(Transform).rotateQ(0,0,90)
        plane.addComponent(BoxCollider("wallCol",position=plane.getComponent(Transform).position, scale=[20,240,2000]))
        self.colliders.append(plane.getComponent(BoxCollider))
        
        plane = self.createPlane((-2000,0,0),color=[255,250,194],textures=["wallgrad.jpg"])
        plane.getComponent(Transform).scale(250,0,2000)
        plane.getComponent(Transform).rotateQ(0,0,90)
        plane.addComponent(BoxCollider("wallCol",position=plane.getComponent(Transform).position, scale=[20,240,2000]))
        self.colliders.append(plane.getComponent(BoxCollider))

        
        plane = self.createPlane((0,0,1000),color=[255,250,194],textures=["wallgrad.jpg"])
        plane.getComponent(Transform).scale(4000,0,240)
        plane.getComponent(Transform).rotateQ(90,0,0)
        plane.addComponent(BoxCollider("wallCol",position=plane.getComponent(Transform).position, scale=[2000,240,20]))
        self.colliders.append(plane.getComponent(BoxCollider))
        
        plane = self.createPlane((0,0,-1000),color=[255,250,194],textures=["wallgrad.jpg"])
        plane.getComponent(Transform).scale(4000,0,240)
        plane.getComponent(Transform).rotateQ(90,0,0)
        plane.addComponent(BoxCollider("wallCol",position=plane.getComponent(Transform).position, scale=[2000,240,20]))
        self.colliders.append(plane.getComponent(BoxCollider))
        
        treasure = self.createCube("treasure",(296,-70,-342),)
        treasure.getComponent(Transform).scale(50,50,50)
        boxc = BoxCollider("activeCollider", position=treasure.getComponent(Transform).position, scale=[50,50,50])
        boxc.isTrigger = True
        treasure.addComponent(boxc)
        self.colliders.append(boxc)
        treasure.addComponent(RotationScript("RotationScript"))
        
        #first horizontal wall
        for i in range(0,20):
            if(i ==2  or i == 11 or  i == 12 or i==17):
                continue
            wall = self.createWall((-960 +  100 * i ,-60,400),textures=[])    
            wall.getComponent(Transform).scale(100,100,200)
            wall.addComponent(BoxCollider("wallCol" + i.__str__(),position=[-960 + 100 * i,0,400], scale=[100,100,80]))
            self.colliders.append(wall.getComponent(BoxCollider))
        
        
        #center v wall
        for i in range(0,7):
            if(i == 3 or i == 5):
                continue
            wall = self.createWall((-460 + 600 -60,-60,361 - i * 100),textures=[])
            wall.getComponent(Transform).scale(100,100,200)
            wall.getComponent(Transform).rotateQ(0,90,0)
            wall.addComponent(BoxCollider("wallCol" + i.__str__(),position=wall.getComponent(Transform).position, scale=[50,100,100]))
            self.colliders.append(wall.getComponent(BoxCollider))
        
        
        #top center horizontal wall
        for i in range(0,15):
            if(i == 7 or i == 9):
                continue
            wall = self.createWall((-960 + i * 100, -60 ,-380))
            wall.getComponent(Transform).scale(100,100,200)
            wall.addComponent(BoxCollider("wallCol" + i.__str__(),position=[-960 + 100 * i,0,400], scale=[100,100,80]))
            self.colliders.append(wall.getComponent(BoxCollider))
        
        for i in range(0,7):
            if(i == 3):
                continue
            wall = self.createWall((-460 + 700 + 60,-60,340 - i * 100),textures=[])
            wall.getComponent(Transform).scale(100,100,200)
            wall.getComponent(Transform).rotateQ(0,90,0)
            wall.addComponent(BoxCollider("wallCol" + i.__str__(),position=wall.getComponent(Transform).position, scale=[50,100,100]))
            self.colliders.append(wall.getComponent(BoxCollider))
        
        #top right horizontal wall
        # for i in range(0,8):
        #     wall = self.createWall((-460 + 700 + i * 100, -60 ,360 -650),color=[255,250,194],textures=[])
        #     wall.getComponent(Transform).scale(100,100,200)
        #     wall.addComponent(BoxCollider("wallCol" + i.__str__(),position=[-960 + 100 * i,0,400], scale=[100,100,80]))
        #     self.colliders.append(wall.getComponent(BoxCollider))
            

        for i in range (0,7):
            if(i == 3):
                continue
            wall = self.createWall((-460 + 250 , -60 ,361 -600 + i * 100))
            wall.getComponent(Transform).scale(100,100,200)
            wall.getComponent(Transform).rotateQ(0,90,0)
            wall.addComponent(BoxCollider("wallCol" + i.__str__(),position=wall.getComponent(Transform).position, scale=[50,100,100]))
            self.colliders.append(wall.getComponent(BoxCollider))
        
        for i in range(0,40):
            if(i == 11 or i == 12 or i == 17 or i == 22 or i == 23 ):
                continue
            wall = self.createWall((-1920 + 100 * i,-60,400),textures=[])    
            wall.getComponent(Transform).scale(100,100,200)
            wall.addComponent(BoxCollider("wallCol" + i.__str__(),position=[-1920 + 100 * i,0,400], scale=[100,100,80]))
            self.colliders.append(wall.getComponent(BoxCollider))
        #2nd v wall
        for i in range(0,14):
            if(i == 3 or i == 6 or i == 9 or i == 12):
                continue
            wall = self.createWall((-920 + 1200 -60,-60,361 - i * 100),textures=[])
            wall.getComponent(Transform).scale(100,100,200)
            wall.getComponent(Transform).rotateQ(0,90,0)
            wall.addComponent(BoxCollider("wallCol" + i.__str__(),position=wall.getComponent(Transform).position, scale=[50,100,100]))
            self.colliders.append(wall.getComponent(BoxCollider))
        
        for i in range(0,14):
            if (i == 6 or i == 7) or i == 12:
                continue
            wall = self.createWall((-920 + 1400 -60,-60,361 - i * 100),textures=[])
            wall.getComponent(Transform).scale(100,100,200)
            wall.getComponent(Transform).rotateQ(0,90,0)
            wall.addComponent(BoxCollider("wallCol" + i.__str__(),position=wall.getComponent(Transform).position, scale=[50,100,100]))
            self.colliders.append(wall.getComponent(BoxCollider))
        
        for i in range(0,9):
            if(i == 7 or i == 9):
                continue
            wall = self.createWall((-1920 + i * 100, -60 ,-380),textures=[])
            wall.getComponent(Transform).scale(100,100,200)
            wall.addComponent(BoxCollider("wallCol" + i.__str__(),position=[-1920 + 100 * i,0,400], scale=[100,100,80]))
            self.colliders.append(wall.getComponent(BoxCollider))
        
        for i in range(0,14):
            if(i == 3 or i == 6 or i == 8 or i==7 or i == 12):
                continue
            wall = self.createWall((-920 + 1400 + 60,-60,340 - i * 100),textures=[],)
            wall.getComponent(Transform).scale(100,100,200)
            wall.getComponent(Transform).rotateQ(0,90,0)
            wall.addComponent(BoxCollider("wallCol" + i.__str__(),position=wall.getComponent(Transform).position, scale=[50,100,100]))
            self.colliders.append(wall.getComponent(BoxCollider))
        
        for i in range(0,18):
            wall = self.createWall((-920 + 1200 + i * 100, -60 ,-290),textures=[])
            wall.getComponent(Transform).scale(100,100,200)
            wall.addComponent(BoxCollider("wallCol" + i.__str__(),position=[-1920 + 100 * i,0,400], scale=[100,100,40]))
            self.colliders.append(wall.getComponent(BoxCollider))
        
        for i in range(0,14):
            wall = self.createWall((-920 + 500 , -60 ,361 -1200 + i * 100))
            wall.getComponent(Transform).scale(100,100,200)
            wall.getComponent(Transform).rotateQ(0,90,0)
            wall.addComponent(BoxCollider("wallCol" + i.__str__(),position=wall.getComponent(Transform).position, scale=[50,100,100]))
            self.colliders.append(wall.getComponent(BoxCollider))
        
        while self.running:
            if not self.mainCameraObject.getComponent(BoxCollider).isColliding:
                self.mainCameraObject.getComponent(BoxCollider).updateLastSafePosition() 
            BoxCollider.checkAllCollisions(self.colliders)
            
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
     
    def createPlane(self,position=(0,0,0),color=[255,255,255], textures=[]):
        color = [c / 255.0 for c in color]
        planeMesh = MeshFilter(Mesh("plane",planeVertices,planeIndices,planeTexCoord,None))
        plane = self.activeScene.createGameObject("Plane",position,planeMesh,MeshRenderer(Material("plane",color=color,textures=textures,shaderName="basic_shader")))
        
        return plane 
        
    def createCube(self,name, position=(0,0,0)):
        cubeMesh = MeshFilter(Mesh("cube",cubeVertices,cubeIndices,cubeTexCoord,None))
        cube = self.activeScene.createGameObject("treasure",position,cubeMesh,MeshRenderer(Material("cube",None,textures=[],shaderName="basic_shader")))
        
        return cube
    
    def createWall(self,position=(0,0,0),color=[255,255,255], textures=[]):
        color = [c / 255.0 for c in color]
        wallMesh = MeshFilter(Mesh("wall",wallVertices,wallIndices,wallTexCoord,None))
        wall= self.activeScene.createGameObject("wall",position,wallMesh,MeshRenderer(Material("wall",color=color,textures=textures,shaderName="basic_shader")))
        
        return wall
    
    def destroyObject(self,objectName):
        for i in range(len(self.activeScene.gameObjects)):
            if self.activeScene.gameObjects[i].name == objectName:
                self.activeScene.gameObjects[i].destroy()
                del self.activeScene.gameObjects[i]
                print(f"Object {objectName} destroyed.")
                break
        else:
            print(f"Object {objectName} not found.")
    
    def importMesh(self,meshName,position=(0,0,0)):
      
        mesh = trimesh.load_mesh(f"mazedgame/meshes/{meshName}.obj")
      
        print("Vertex range:", mesh.vertices.min(axis=0), mesh.vertices.max(axis=0))
        print("Face counts:", len(mesh.faces))
        mesh = MeshFilter(Mesh(meshName,mesh.vertices,mesh.faces,None,None))
        meshObject = self.activeScene.createGameObject(meshName,position,mesh,MeshRenderer(Material(meshName,[255,255,255],textures=[],shaderName="basic_shader")))

        
        
if __name__ == "__main__":
    MazedEngine().start()
    
