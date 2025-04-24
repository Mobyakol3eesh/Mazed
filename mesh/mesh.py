# from OpenGL.GL import *
from mesh.game_object import GameObject
# from core.opengl_utilities import OpenGLUtilities
# from core.opengl_buffers import openGLBuffer
# from core.transform import Transform
# from mesh.shader import Shader
# from mesh.texture import Texture


class Mesh(GameObject):
    def __init__(self, name ,vertices,indices, texCoord,normals):
        super().__init__(name)
        self.vertices = vertices
        self.indices = indices
        self.texCoord = texCoord
        self.normals = normals
        
        
  