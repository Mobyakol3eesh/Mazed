from OpenGL.GL import * 
import numpy as np
from ctypes import sizeof, c_float,c_void_p
class openGLBuffer:
    def __init__(self,vectorSize,stride,rgbCoord=3,texCoord=2):
        self.vertexArrayID = glGenVertexArrays(1)
        self.rgbCoord = rgbCoord
        self.texCoord = texCoord
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
           
            glVertexAttribPointer(vertexAttrIndex + 1, self.rgbCoord, GL_FLOAT, GL_FALSE, self.stride * sizeof(c_float), c_void_p(self.vectorSize * sizeof(c_float)))
            glEnableVertexAttribArray(vertexAttrIndex + 1)
        if self.stride == 8:
             
            glVertexAttribPointer(vertexAttrIndex + 2, self.texCoord, GL_FLOAT, GL_FALSE, self.stride * sizeof(c_float), c_void_p((self.vectorSize + self.rgbCoord) * sizeof(c_float)))
            glEnableVertexAttribArray(vertexAttrIndex + 2)
        
        glBindVertexArray(0)    
        
    
    def createIndexBuffer(self,indices):
        
        self.indexBufferID = glGenBuffers(1)
        glBindVertexArray(self.vertexArrayID)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.indexBufferID)
        indices = np.array(indices).astype(np.uint32)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices.ravel(), GL_STATIC_DRAW)
        glBindVertexArray(0)
        
        
        
        
        
    
        
        
        
   
        
    
        
