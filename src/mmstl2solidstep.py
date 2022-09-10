"""
Python script: mmstl2solidstep.py
Description: macro that imports a MeshMixer processed STL file and generates a solid model for volumetrical meshing in Gmesh    
**Licensing**: I-STL2MOOSE is distributed under MIT LICENSE.
"""
import sys
import FreeCAD
import Mesh
import Part

stl_name = sys.argv[2]
object_name = stl_name[:-4]
print('mmstl2solid is processing file: ', stl_name, 'object', object_name)


# Macro Init +++++++++++++++++++++++++++++++++++++++++++++++++

mesh = Mesh.Mesh(stl_name)
shape = Part.Shape()
shape.makeShapeFromMesh(mesh.Topology, 0.1)

solid = Part.makeSolid(shape)
string_solid = object_name + '_solid.step'
solid.exportStep(string_solid)

del shape

# Macro End +++++++++++++++++++++++++++++++++++++++++++++++++



