from mesh.mesh_filter import MeshFilter
from mesh.material import Material

from OpenGL.GL import *
from core.opengl_utilities import OpenGLUtilities
from core.opengl_buffers import openGLBuffer
from core.component import Component
from core.transform import Transform

class MeshRenderer(Component):
    def __init__(self, material : Material):
        super().__init__(name="MeshRenderer")
        self.gameObject = None
        self.meshFilter = None
        self.material = material
        
        self.glBuffer = None
        self.vbo = None
        self.ibo = None
        self.vao = None
        
    
    def start(self):
        
        self.meshFilter = self.gameObject.getComponent(MeshFilter)
        self.data , self.indices = self.meshFilter.concatData()
        self.glBuffer = openGLBuffer(vectorSize=3, stride=self.meshFilter.mesh.vertices[0].__len__())
        self.glBuffer.createVertexBuff(self.data, vertexAttrIndex=0, isTextured=self.material.isTextured)
        self.vbo = self.glBuffer.vertexBufferID
        self.glBuffer.createIndexBuffer(self.indices)
        self.ibo = self.glBuffer.indexBufferID
        self.vao = self.glBuffer.getVertexArrayID()
        
        
    
    def render(self,transform: Transform, projectionMatrix, viewMatrix):
        self.material.shader.use()
        
        if (self.material.color is not None):
            
            self.material.shader.useUniform("isTextured", self.material.isTextured, 'bool') 
            self.material.shader.useUniform("glColor", self.material.color,"vec3")
        
        if (self.material.isTextured):
            self.material.shader.useUniform("isTextured", self.material.isTextured, 'bool')
            self.material.textureActivation()
            
        
        self.material.shader.useUniform("model", transform.getModelMatrix(), 'mat4')
        self.material.shader.useUniform("projection", projectionMatrix, 'mat4')
        self.material.shader.useUniform("view", viewMatrix, 'mat4')

        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES, len(self.meshFilter.mesh.indices), GL_UNSIGNED_INT, None)
        glBindVertexArray(0)
    
        
    def addTexture(self, textureName):
        self.material.addTexture(textureName)
        glDeleteBuffers(1, [self.vbo])
        
        self.glBuffer.createVertexBuff(self.data, vertexAttrIndex=0, isTextured=self.material.isTextured)
        self.vbo = self.glBuffer.vertexBufferID
        
        self.glBuffer.createIndexBuffer(self.indices)
        
        
        
        
        
    
    
    
            
       