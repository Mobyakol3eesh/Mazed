from OpenGL.GL import * 
import numpy as np
from ctypes import sizeof, c_float
class openGLBuffer:
    def __init__(self,bufferType):
        self.bufferType = bufferType
        self.vertexBufferID =  glGenBuffers(1)
        self.vertexArrayID = glGenVertexArrays(1)
        
    
    def createVertexBuffer(self,data,vertexAttrIndex):
       
        data = np.array(data).astype(np.float32)
        
        glBindVertexArray(self.vertexArrayID)
        glBindBuffer(self.bufferType, self.vertexBufferID)
        glBufferData(self.bufferType, data.nbytes, data.ravel(), GL_STATIC_DRAW)
        glVertexAttribPointer(vertexAttrIndex, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(c_float), None) ## hardcoded to 3 floats per vertex
        glEnableVertexAttribArray(vertexAttrIndex)
        return self.vertexBufferID, self.vertexArrayID
    
        
        
        
    
        
        
        
   
        
    
        
