from mesh.shader import Shader
from mesh.texture import Texture
from OpenGL.GL import *
import pdb


class Material:
    def __init__(self, name, color, textures, shaderName):
        self.name = name
        self.color = color
        self.textures = textures
        self.texturesID = []
        self.shaderName = shaderName 
        self.isTextured = False
        
        self.shader = Shader(self.shaderName)
        self.activateMaterial()
        
        print(self.isTextured)
        
        
    def activateMaterial(self):
        
        
        if (self.textures):
            
            
            self.isTextured = True
            self.textures = [Texture(texture) for texture in self.textures]
            self.texturesID = [texture.textureID for texture in self.textures]
            self.textureActivation()
            
        
        
        
    
    
    def textureActivation(self):
        
        for i in range(len(self.textures)):
            if i == 16:
                 raise Exception("Max 16 textures supported")   
            
            self.shader.useUniform(f"texture{i}", i, 'int')                     
            glActiveTexture(GL_TEXTURE0 + i)
            glBindTexture(GL_TEXTURE_2D, self.texturesID[i])
            
            
    
        
    
    def addTexture(self,textureName):
         self.textures.append(Texture(textureName))
         self.texturesID.append(self.textures[-1].textureID)
         self.isTextured = True
         
         if  self.textures.__len__() > 1:
            self.textureActivation()  
            
            
            
