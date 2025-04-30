
from pygame.locals import *
import pygame as pg


class Input:
    def __init__(self):
        self.event = None
        self.sensitivity = 0.2

        self.axis = {
        "Horizontal": 0.0,
        "Vertical": 0.0,
        "MouseX": 0.0,
        "MouseY": 0.0  
    }
        self.state = True
        self.keyHeld = None
        
    
 
    
    
   
    def getAxis(self, axisName):
        if axisName in self.axis:
            return self.axis[axisName]
        else:
            raise ValueError(f"Axis '{axisName}' not found.")

    

    def getKeyDown(self):
        if self.event.type == KEYDOWN:
            return self.event.key
        return None
    
   
    def getKeyUp(self):
        if self.event.type == KEYUP:
            return self.event.key
        return None
    
 
   
    
    def runningState(self):
        return self.state
    
    def update(self):
        for event in pg.event.get():
            
            if event.type == QUIT:
                self.state = False

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
        print(self.axis.get("Vertical"),self.axis.get("Horizontal"))