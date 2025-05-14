from OpenGL.GL import * 
import numpy as np
from ctypes import sizeof, c_float,c_void_p
class openGLBuffer:
    def __init__(self,vectorSize,stride,texCoord=2):
        self.vertexArrayID = glGenVertexArrays(1)
       
        self.texCoord = texCoord
        self.vectorSize = vectorSize
        self.vertexBufferID = None
        self.indexBufferID = None
        self.stride = stride
        
        
  
    def createVertexBuff(self,vertices,vertexAttrIndex,isTextured=True):
       
        
        vertices = np.array(vertices).astype(np.float32)
        
        self.vertexBufferID = glGenBuffers(1)
        
        glBindVertexArray(self.vertexArrayID)
        glBindBuffer(GL_ARRAY_BUFFER, self.vertexBufferID)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices.ravel(), GL_STATIC_DRAW)
        
        glVertexAttribPointer(vertexAttrIndex, self.vectorSize, GL_FLOAT, GL_FALSE, self.stride * sizeof(c_float), None)
        glEnableVertexAttribArray(vertexAttrIndex)
       
       
        # if isTextured and isRGB:
        #     glVertexAttribPointer(vertexAttrIndex + 1, self.rgbCoord, GL_FLOAT, GL_FALSE, self.stride * sizeof(c_float), c_void_p(self.vectorSize * sizeof(c_float)))
        #     glEnableVertexAttribArray(vertexAttrIndex + 1)
          
        #     glVertexAttribPointer(vertexAttrIndex + 2, self.texCoord, GL_FLOAT, GL_FALSE, self.stride * sizeof(c_float), c_void_p((self.vectorSize + self.rgbCoord) * sizeof(c_float)))
        #     glEnableVertexAttribArray(vertexAttrIndex + 2)
        #     print("isTextured and isRGB")
        
        # elif isRGB:
           
        #     glVertexAttribPointer(vertexAttrIndex + 1, self.rgbCoord, GL_FLOAT, GL_FALSE, self.stride * sizeof(c_float), c_void_p(self.vectorSize * sizeof(c_float)))
        #     glEnableVertexAttribArray(vertexAttrIndex + 1)
        #     print("isRGB")
        
        if isTextured:
            
            glVertexAttribPointer(vertexAttrIndex + 1, self.texCoord, GL_FLOAT, GL_FALSE, self.stride * sizeof(c_float), c_void_p((self.vectorSize) * sizeof(c_float)))
            glEnableVertexAttribArray(vertexAttrIndex + 1)
            
        
        
        
        glBindVertexArray(0)    
        
    
    def createIndexBuffer(self,indices):
        
        self.indexBufferID = glGenBuffers(1)
        glBindVertexArray(self.vertexArrayID)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.indexBufferID)
        indices = np.array(indices).astype(np.uint32)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices.ravel(), GL_DYNAMIC_DRAW)
        glBindVertexArray(0)
        
    def getVertexArrayID(self):
        return self.vertexArrayID    
        
        
        
    
        
        
        
   
        
    
        
