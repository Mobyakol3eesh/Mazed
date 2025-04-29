
from math import *
import pygame as pg
from core.mscript import MScript
from core.camera import Camera
import glm
from core.transform import Transform



class RotateCamera(MScript):

    def __init__(self, name, speed=1.0):
        super().__init__(name)
       

    def start(self):
        self.camera = self.gameObject.getComponent(Camera)
        
        if not self.camera:
            raise Exception("RotateCamera script requires a Camera component on the GameObject.")
    
    
    def update(self, deltaTime):
       
        transform = self.gameObject.getComponent(Transform)
       
        if transform:
            print(transform.position.__str__())
            camX = sin (pg.time.get_ticks() / 1000) * 10
            camY = cos (pg.time.get_ticks() / 1000) * 10
            
            self.camera.view = glm.lookAt(
                glm.vec3(camX, 0, camY),
                glm.vec3(0, 0, 0),
                glm.vec3(0, 1, 0)
            )
        