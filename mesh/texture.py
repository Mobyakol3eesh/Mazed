from OpenGL.GL import *
import os 
from PIL import Image




class Texture():
    def __ininit__(self):
        self.textureID = None
        
    
    def __init__(self, imageName):
        self.textureID = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.textureID)
        self.initialize()
        image_data , width, height = self.__load(imageName)
        if (image_data is None):
            raise Exception(f"Failed to load texture: {imageName}")
        
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
        glGenerateMipmap(GL_TEXTURE_2D)
        
        del image_data
        
        
        
    def initialize(self):
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
       

    def __load(self,image_name):
        base_path = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_path, "textures", image_name)
        
        image = Image.open(image_path)
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        image_data = image.convert("RGBA").tobytes()
        width, height = image.size
        
        return image_data, width, height
        