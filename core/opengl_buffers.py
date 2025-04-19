from OpenGL.GL import * 
import numpy as np
from ctypes import sizeof, c_float
class openGLBuffer:
    def __init__(self):
        self.vertexArrayID = glGenVertexArrays(1)
        
    
    def createVertexBuffer(self,vertecies,vertexAttrIndex):
       
        vertecies = np.array(vertecies).astype(np.float32)
        
        vertexBufferID = glGenBuffers(1)
        
        glBindVertexArray(self.vertexArrayID)
        glBindBuffer(GL_ARRAY_BUFFER, vertexBufferID)
        glBufferData(GL_ARRAY_BUFFER, vertecies.nbytes, vertecies.ravel(), GL_STATIC_DRAW)
        glVertexAttribPointer(vertexAttrIndex, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(c_float), None) ## hardcoded to 3 floats per vertex
        glEnableVertexAttribArray(vertexAttrIndex)
        glBindVertexArray(0)
        
        return vertexBufferID
    
    def createIndexBuffer(self,indices,vertexAttrIndex):
        
        indexBufferID = glGenBuffers(1)
        glBindVertexArray(self.vertexArrayID)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, indexBufferID)
        indices = np.array(indices).astype(np.uint32)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices.ravel(), GL_STATIC_DRAW)
        glVertexAttribPointer(vertexAttrIndex, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(c_float), None) ## hardcoded to 3 floats per vertex
        glBindVertexArray(0)
        
        return indexBufferID
        
        
        
    
        
        
        
   
        
    
        
