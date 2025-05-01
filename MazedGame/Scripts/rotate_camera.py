
from math import *
import pygame as pg
from MazedEngine.mscript import MScript
from MazedEngine.camera import Camera
import glm
from MazedEngine.transform import Transform



class RotateCamera(MScript):

    def __init__(self, name, speed=1.0):
        super().__init__(name)
       

    def start(self):
        self.camera = self.gameObject.getComponent(Camera)
        
        if not self.camera:
            raise Exception("RotateCamera script requires a Camera component on the GameObject.")
        self.transform = self.gameObject.getComponent(Transform)
        self.transform.rotateQ(10,24 ,0)
        
    def update(self, deltaTime):
        
        print(self.transform.forward)
        
        
        