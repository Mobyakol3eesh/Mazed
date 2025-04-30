from MazedEngine.component import Component





class MeshFilter(Component):
    def __init__(self, mesh):
        self.mesh = mesh
        self.texCoord = False
        self.normals = False
    
    
    def checkMesh(self):
        try:
            if self.mesh is None:
                raise Exception("Mesh is not assigned to the MeshFilter")
            if self.mesh.vertices is None or self.mesh.indices is None:
                raise Exception("Mesh vertices or indices are not assigned")
            if self.mesh.texCoord is None :
                
                raise Exception("Mesh texCoord not assigned")
            self.texCoord = True    
            if self.mesh.normals is None:
                
                raise Exception("Mesh normals not assigned")
            self.normals = True        
        except Exception as e:
            print(f"{e}")
            return
        
        
    def concatData(self):
        self.checkMesh()
        vertices = self.mesh.vertices
        indices = self.mesh.indices
        texCoord = self.mesh.texCoord
        normals = self.mesh.normals
        
        
        data = []
        for i in range(len(vertices)):
            vertexData = vertices[i]
            if self.texCoord:
                
                vertexData.append(texCoord[i*2])
                vertexData.append(texCoord[i*2 + 1])
            
            if self.normals:
                
                vertexData.append(normals[i])
            
            data.append(vertexData)
        
        return data, indices
          
    