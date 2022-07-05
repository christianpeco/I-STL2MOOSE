**Description**:**I-STL2MOOSE**

**Licensing**: I-STL2MOOSE is distributed under MIT LICENSE as descripted below.

-----------------------------------------------  XXXXXXXX LICENSE XXXXXXXX  ---------------------------------------------------

Copyright <2022> <Joe Sgarrella, Farshad Ghanbari, Christian Peco>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

-----------------------------------------------  XXXXXXXX LICENSE XXXXXXXX  ---------------------------------------------------

**Description**: I-STL2MOOSE software is a procedural script that transforms a group of STL files into a combined, conforming three-dimensional mesh file that can be read by FEM implementation package MOOSE. 

The STL files transformed by the I-STL2MOOSE software are altered to the desired specifications prior to being inputted. This can be done using a software such as MeshMixer. The altered STL files are converted to STEP files by the I-STL2MOOSE software through the mm2solidstep.py script. The STEP files are then merged into a GEO file in Gmsh. The integrated GEO file is then transformed by the I-STL2MOOSE software into a three-dimensional MSH file with the physical volumes and surfaces of each entity defined. The current version of the I-STL2MOOSE software creates a single, general boundary for each entity.

**Technologies:**
- MeshMixer: Meshmixer is not directly used by the I-STL2MOOSE software, but it is required for altering raw STL files to the desired specifications. 
- FreeCAD: FreeCAD is utilized by the I-STL2MOOSE software in converting STL files to solid STEP files.
- Gmsh: The I-STL2MOOSE software uses Gmsh to create an Integrated.geo file that contains all of the solid STEP files. Gmsh converts the individual STEP files into a single mesh. Gmsh also defines the physical volumes and surfaces which can be used to establish boundary conditions. 

**Usage:**
To use the I-STL2MOOSE software, both the ISTL2MOOSE.py and the mm2solidstep.py scripts should be downloaded to the same location. Using the command line, the ISTL2MOOSE software can be launched by executing:

python ISTL2MOOSE.py  --N File1.stl File2.stl --gmsh "Gmsh Path" --freecad "FreeCADCmd Path"

Three inputs are required: N, gmsh, and freecad. 
- N: The number of files to process. Every STL file should be listed for this variable. The files must be listed in the order from the lowest to the highest hierarchy level. 
- gmsh: This is the path to the current Gmsh
- freecad: This is the path to the current FreeCADCmd

**Usage Example:**

The inputfiles folder of this repository contains sample STL files that have already been altered in MeshMixer. There are files for two separate examples. The *AntHead.stl* and *AntSphere.stl* files can be inputted to generate a mesh with the sphere embedded within the ant head. A sample call for this example, in a conventional Mac OS X is:

python ISTL2MOOSE.py --N AntSphere.stl AntHead.stl --gmsh Applications/Gmsh.app/contents/MacOS/gmsh --freecad Applications/FreeCAD.app/contents/MacOS/FreeCAD

Notice that the *AntSphere.stl* file is listed before the *AntHead.stl* because the sphere is to be embedded within the ant head. The resulting mesh of these input files can be found in the Results folder of this repository. The file is labled *AntHead.msh.zip*. 

The second example requires five STL input files. The mesh generated in this example is a cube with two spheres embedded within. Additionally, each sphere has a single smaller sphere embedded. This provides an example of a mesh with more than two hierarchy levels that must be considered with entering the STL files in th script. The command call, in a conventional Mac OS X is:

python ISTL2MOOSE.py --N mm_smallspehere1.stl mm_smallspehere2.stl mm_medspehere1.stl mm_medspehere2.stl mm_largecube.stl --gmsh Applications/Gmsh.app/contents/MacOS/gmsh --freecad Applications/FreeCAD.app/contents/MacOS/FreeCAD

Again notice the ordering of the STL files. The files are arranged from the lowest hierarchy to the highest. The resulting mesh can also be found in the Results folder. The file is labeled *MultiLayer.msh.zip*.



