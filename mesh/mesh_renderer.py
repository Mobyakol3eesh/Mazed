from mesh.mesh_filter import MeshFilter
from mesh.material import Material

from OpenGL.GL import *
from core.opengl_utilities import OpenGLUtilities
from core.opengl_buffers import openGLBuffer
from core.component import Component
from core.transform import Transform

class MeshRenderer(Component):
    def __init__(self,meshFilter : MeshFilter, material : Material):
        self.meshFilter = meshFilter
        self.material = material
        
        self.glBuffer = None
        self.vbo = None
        self.ibo = None
        self.vao = None
        self.data , self.indices = self.meshFilter.concatData()
        self.glBuffer = openGLBuffer(vectorSize=3, stride=self.meshFilter.mesh.vertices[0].__len__())
        self.vbo = self.glBuffer.createVertexBuff(self.data, vertexAttrIndex=0, isTextured=self.material.isTextured)
        self.vao = self.glBuffer.getVertexArrayID()
        self.ibo = self.glBuffer.createIndexBuffer(self.indices)
    
    
    
    def render(self,transform: Transform, projectionMatrix, viewMatrix):
        
        if (self.material.color is not None):
            
            self.material.shader.useUniform("isTextured", self.material.isTextured, 'bool') 
            self.material.shader.useUniform("glColor", self.material.color,"vec3")
        
        if (self.material.isTextured):
            self.material.shader.useUniform("isTextured", self.material.isTextured, 'bool')
            self.material.textureActivation()
            
        
        self.material.shader.useUniform("model", transform.getModelMatrix(), 'mat4')
        self.material.shader.useUniform("projection", projectionMatrix, 'mat4')
        self.material.shader.useUniform("view", viewMatrix, 'mat4')
        
        
        
        
        
        
        
    
    
    
            
       