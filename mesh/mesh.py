from OpenGL.GL import *
from mesh.game_object import GameObject
from core.opengl_utilities import OpenGLUtilities
from core.opengl_buffers import openGLBuffer



class Mesh(GameObject):
    def __init__(self, vertices, indices, shaderName='mesh_shader', textures=None):
        super().__init__(name="Mesh",)
       