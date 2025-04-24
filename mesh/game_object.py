from core.transform import Transform


class GameObject(object):
    def __init__(self, name , position=(0,0,0)):
        self.name = name
        self.components = {}
        self.addComponent(Transform(*position))
        
        
    def addComponent(self, component):
        self.components[type(component)] = component
    
    
    def getComponent(self, componentClass):
       return self.components.get(componentClass, None)