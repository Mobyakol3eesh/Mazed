
from mesh.game_object import GameObject



class Mesh(GameObject):
    def __init__(self, name ,vertices,indices, texCoord,normals):
        super().__init__(name)
        self.vertices = vertices
        self.indices = indices
        self.texCoord = texCoord
        self.normals = normals
        
        
  