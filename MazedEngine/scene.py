
from mesh.game_object import GameObject





class Scene:
    def __init__(self):
        self.gameObjects = []
        
    def addGameObject(self, gameObject):
        self.gameObjects.append(gameObject)
    def removeGameObject(self, gameObject):
        self.gameObjects.remove(gameObject)
    def createGameObject(self, gameObjectName,position=(0,0,0),*components):
        
        gameObject = GameObject(gameObjectName,position,*components)
        self.addGameObject(gameObject)
        return gameObject
    
    
    
    def update(self,deltaTime):
        for gameObject in self.gameObjects:
            gameObject.update(deltaTime)
    
    
    
    def render(self,projectionMatrix, viewMatrix):
        for gameObject in self.gameObjects:
            gameObject.render(projectionMatrix, viewMatrix)