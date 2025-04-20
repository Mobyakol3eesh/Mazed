from OpenGL.GL import * 
import numpy as np
from ctypes import sizeof, c_float,c_void_p
class openGLBuffer:
    def __init__(self,vectorSize,stride):
        self.vertexArrayID = glGenVertexArrays(1)
        self.vectorSize = vectorSize
        self.vertexBufferID = None
        self.indexBufferID = None
        self.stride = stride
        
        
  
    def createVertexBuff(self,vertecies,vertexAttrIndex):
       
        vertecies = np.array(vertecies).astype(np.float32)
        
        self.vertexBufferID = glGenBuffers(1)
        
        glBindVertexArray(self.vertexArrayID)
        glBindBuffer(GL_ARRAY_BUFFER, self.vertexBufferID)
        glBufferData(GL_ARRAY_BUFFER, vertecies.nbytes, vertecies.ravel(), GL_STATIC_DRAW)
        if self.stride >= 3:
            glVertexAttribPointer(vertexAttrIndex, self.vectorSize, GL_FLOAT, GL_FALSE, self.stride * sizeof(c_float), None)
            glEnableVertexAttribArray(vertexAttrIndex)
        if self.stride >= 6:
           
            glVertexAttribPointer(vertexAttrIndex + 1, self.vectorSize, GL_FLOAT, GL_FALSE, self.stride * sizeof(c_float), c_void_p(self.vectorSize * sizeof(c_float)))
            glEnableVertexAttribArray(vertexAttrIndex + 1)
        elif self.stride == 8:
             
            glVertexAttribPointer(vertexAttrIndex + 2, self.vectorSize, GL_FLOAT, GL_FALSE, self.stride * sizeof(c_float), c_void_p(2 * self.vectorSize * sizeof(c_float)))
            glEnableVertexAttribArray(vertexAttrIndex + 2)
        
        glBindVertexArray(0)    
        
    
    def createIndexBuffer(self,indices,vertexAttrIndex):
        
        self.indexBufferID = glGenBuffers(1)
        glBindVertexArray(self.vertexArrayID)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.indexBufferID)
        indices = np.array(indices).astype(np.uint32)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices.ravel(), GL_STATIC_DRAW)
        glVertexAttribPointer(vertexAttrIndex, self.vectorSize, GL_FLOAT, GL_FALSE, self.stride * sizeof(c_float), None)
        glBindVertexArray(0)
        
        
        
        
        
    
        
        
        
   
        
    
        
