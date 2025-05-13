from MazedEngine.component import Component
from MazedEngine.transform import Transform
import glm

class BoxCollider(Component):
    def __init__(self, name, position, scale, isTrigger=False):
        super().__init__(name)
        self.position = glm.vec3(*position)
        self.scale = glm.vec3(*scale)
        self.isColliding = False
        self.lastSafePosition = glm.vec3(*position)
        self.collisionNormal = glm.vec3(0, 0, 0)
        self.pushBackForce = 0.1  
        self.onCollisionEnter = None
        self.isTrigger = False
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

    def handleCollision(self,other):
        if not self.isTrigger:
            transform = self.gameObject.getComponent(Transform)


            transform.setPosition(*self.lastSafePosition)


            pushBack = self.collisionNormal * self.pushBackForce
            transform.translate(pushBack.x, 0, pushBack.z)
        
        
        if self.onCollisionEnter:
            self.onCollisionEnter(other)
           
        
        


    def onCollisionEnter(self):
        pass

    def update(self, deltaTime):
        
        transform = self.gameObject.getComponent(Transform)
        self.position = glm.vec3(transform.position)

    @staticmethod
    def checkAllCollisions(colliders):
        
     
        active = next((c for c in colliders if c.name == 'activeCollider'), None)
        if not active:
            return

       
        active.isColliding = False
        for obj in colliders:
            if obj == active:
                continue
                
            if active.checkCollision(obj):
                active.isColliding = True
                active.handleCollision(obj)
                
               

                break 
            