from MazedEngine.transform import Transform
from mesh.mesh_renderer import MeshRenderer

class GameObject(object):
    def __init__(self, name , position=(0,0,0),*components):
        self.name = name
        self.components = {}
        self.addComponent(Transform(*position))
        for component in components:
            self.addComponent(component)
        
    def addComponent(self, component):
        
        self.components[type(component)] = component
       
        
        if hasattr(component, 'setGameObject'):
            component.setGameObject(self)
        
        if hasattr(component, 'start'):
            component.start()
        
        
    
    
    def getComponent(self, componentClass):
       return self.components.get(componentClass, None)
    
    def update(self,deltaTime):
        for component in self.components.values():
            if hasattr(component, 'update'):
                component.update(deltaTime)

    def render(self, projectionMatrix, viewMatrix):
        renderer = self.getComponent(MeshRenderer)
        if renderer:
            renderer.render(self.getComponent(Transform), projectionMatrix, viewMatrix)