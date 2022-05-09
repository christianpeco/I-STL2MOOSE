"""
Python script: mmstl2solidstep.py
Description: macro that imports a MeshMixer processed STL file and generates a solid model for volumetrical meshing in Gmesh    

"""
import sys
import FreeCAD
import Mesh
import Part

stl_name = sys.argv[2]
object_name = stl_name[:-4]
print('mmstl2solid is processing file: ', stl_name, 'object', object_name)

Mesh.open(stl_name)

print("STL mesh opened...")

string_part = object_name + 'temp'
FreeCAD.getDocument("Unnamed").addObject("Part::Feature", string_part)
__shape__ = Part.Shape()
__shape__.makeShapeFromMesh(FreeCAD.getDocument("Unnamed").getObject(object_name).Mesh.Topology, 0.100000)
FreeCAD.getDocument("Unnamed").getObject(string_part).Shape=__shape__
FreeCAD.getDocument("Unnamed").getObject(string_part).purgeTouched()

solid = Part.makeSolid(__shape__)
string_solid = object_name + '_solid.step'
solid.exportStep(string_solid)

del __shape__

# Macro End +++++++++++++++++++++++++++++++++++++++++++++++++



