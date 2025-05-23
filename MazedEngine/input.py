
from pygame.locals import *
import pygame as pg


class Input:
    def __init__(self):
        
        self.sensitivity = 0.2

        self.axis = {
        "Horizontal": 0.0,
        "Vertical": 0.0,
        "MouseX": 0.0,
        "MouseY": 0.0  
    }
        self.state = True
        self.keyDown = None
        self.keyUp = None
        self.mouseMoving = False
    
 
    
    
    
    def getAxis(self, axisName):
        if axisName in self.axis:
            return self.axis[axisName]
        else:
            raise ValueError(f"Axis '{axisName}' not found.")

    

    def getKeyDown(self):
        return self.keyDown
   
    def getKeyUp(self):
        return self.keyUp
    
 
   
    
    def runningState(self):
        return self.state
    
    def update(self):
        self.mouseMoving = False
        
        for event in pg.event.get():
            if event.type == KEYDOWN:
                self.keyDown = event.key
            if event.type == KEYUP:
                self.keyUp = event.key
            if event.type == MOUSEMOTION:
                if  pg.mouse.get_focused():
                    self.mouseMoving = True
                    self.axis["MouseX"] = -event.rel[0] * self.sensitivity
                    self.axis["MouseY"] = -event.rel[1] * self.sensitivity
                else :
                    print("Mouse not focused")     
                    
                    self.axis["MouseX"] = 0.0
                    self.axis["MouseY"] = 0.0
            if event.type == QUIT:
                self.state = False
                
        if not self.mouseMoving:
            self.axis["MouseX"] = 0.0
            self.axis["MouseY"] = 0.0
        
        keys = pg.key.get_pressed()
    
      
        if keys[K_w] or keys[K_UP]:
            self.axis["Vertical"] += self.sensitivity 
        if keys[K_s] or keys[K_DOWN]:
            self.axis["Vertical"] -= self.sensitivity
        if keys[K_a] or keys[K_LEFT]:
            self.axis["Horizontal"] -= self.sensitivity
        if keys[K_d] or keys[K_RIGHT]:
            self.axis["Horizontal"] += self.sensitivity

        self.axis["Vertical"] = max(-1.0, min(self.axis["Vertical"], 1.0))
        self.axis["Horizontal"] = max(-1.0, min(self.axis["Horizontal"], 1.0))

       
        if not (keys[K_w] or keys[K_UP] or keys[K_s] or keys[K_DOWN]):
            if self.axis["Vertical"] > 0:
                self.axis["Vertical"] = max(0.0, self.axis["Vertical"] - self.sensitivity)
            elif self.axis["Vertical"] < 0:
                self.axis["Vertical"] = min(0.0, self.axis["Vertical"] + self.sensitivity)

        if not (keys[K_a] or keys[K_LEFT] or keys[K_d] or keys[K_RIGHT]):
            if self.axis["Horizontal"] > 0:
                self.axis["Horizontal"] = max(0.0, self.axis["Horizontal"] - self.sensitivity)
            elif self.axis["Horizontal"] < 0:
                self.axis["Horizontal"] = min(0.0, self.axis["Horizontal"] + self.sensitivity)
        