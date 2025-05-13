from MazedEngine.component import Component
from MazedEngine.transform import Transform
import glm

class BoxCollider(Component):
    def __init__(self, name, position, scale):
        super().__init__(name)
        self.position = glm.vec3(*position)
        self.scale = glm.vec3(*scale)
        self.isColliding = False
        self.lastSafePosition = glm.vec3(*position)
        self.collisionNormal = glm.vec3(0, 0, 0)
        self.pushBackForce = 0.1  

    def updateLastSafePosition(self):
        
        transform = self.gameObject.getComponent(Transform)
        self.lastSafePosition = glm.vec3(transform.position)

    def checkCollision(self, other):
       
        a_min = self.position - self.scale * 0.5
        a_max = self.position + self.scale * 0.5
        b_min = other.position - other.scale * 0.5
        b_max = other.position + other.scale * 0.5

      
        colliding = not (a_max.x <= b_min.x or a_min.x >= b_max.x or
                        a_max.y <= b_min.y or a_min.y >= b_max.y or
                        a_max.z <= b_min.z or a_min.z >= b_max.z)
        
        if colliding:
           
            self.collisionNormal = glm.normalize(self.position - other.position)
        return colliding

    def handleCollision(self):
        
        transform = self.gameObject.getComponent(Transform)
        
        
        transform.setPosition(*self.lastSafePosition)
        
       
        pushBack = self.collisionNormal * self.pushBackForce
        transform.translate(pushBack.x, pushBack.y, pushBack.z)
        
       
        

    def update(self, deltaTime):
        
        transform = self.gameObject.getComponent(Transform)
        self.position = glm.vec3(transform.position)

    @staticmethod
    def checkAllCollisions(colliders):
        
     
        cam = next((c for c in colliders if c.name == 'camCollider'), None)
        if not cam:
            return

       
        cam.isColliding = False
        for obj in colliders:
            if obj == cam:
                continue
                
            if cam.checkCollision(obj):
                cam.isColliding = True
                cam.handleCollision()
                break 