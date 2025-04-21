


class GameObject(object):
    def __init__(self, name):
        self.name = name
        self.glBuffer = None
        self.shader = None
        self.textures = []
        self.modelMatrix = None
        self.viewMatrix = None
        self.projectionMatrix = None
        self.transformMatrix = None
        
        