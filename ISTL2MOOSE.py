"""
Python script: ISTL2MOOSE.py
Description: procedural script that imports a MeshMixer processed STL file
and generates a MOOSE readable volumetrical .msh file
"""

import sys
import random
import os
import numpy
import argparse

################# Initiate Argument Parsing #################

parser = argparse.ArgumentParser(description='command line options')

# Aligned, transformed and re-meshed files .stl from the preprocessor (usually MeshMixer)

parser.add_argument('--N', metavar='file1.stl', type=str, nargs='+', required=True,
                    help='Number of stl files to process. Note: the files have to be ordered from lower to higher hierarchy level.')

# Gmesh path to executable in the system
parser.add_argument('--gmesh', metavar='gmesh_path', type=str, nargs='+', required=True,
                    help='Path to current gmesh.')

# FreeCAD path to executable in the system
parser.add_argument('--freecad', metavar='freecad_path', type=str, nargs='+', required=True,
                    help='Path to current freecad.')

args = parser.parse_args()
################# Finish Argument Parsing #################


# FreeCad stl to solid model procedure through mmstl2solidstep script

files_num = len(args.N)
string0 = str(args.freecad[0])

for i in range(0, files_num):
    string1 = string0 + ' ' + 'mmstl2solidstep.py' + ' ' + args.N[i]
    os.system(string1)

# Generate geometry .geo file for Gmesh from .step solid model

f = open("integrated.geo", "w")

for i in range(0, files_num):
    solid_string = args.N[i][:-4] + '_solid.step'
    string_geo = 'Merge ' + '"' + solid_string + '"' + ';'  '\n'
    f.write(string_geo)

f.write('//+\n')
f.write('SetFactory("OpenCASCADE");\n')
f.write('//+\n')

#Defining surface boundary for each of the volumes

for i in range(0, files_num):
    solid_string = 'Suf' + str(i + 1) + '[] = CombinedBoundary {Volume{' + str(i + 1) + '};};\n'
    f.write(solid_string)
  
# Generation of Booleans (involves hierarchy levels of embedding)  
  
f.write('//+\n')
f.write('BooleanFragments{Volume{1')
for i in range(1, files_num):
    solid_string = ',' + str(i + 1)
    f.write(solid_string)
f.write('}; Delete;}{ };\n')

# Physical surface tags for boundary conditions

f.write('//+\n')
for i in range(0, files_num):
    solid_string = 'Physical Surface("Boundary' + str(i + 1) + '", ' + str(i + 1) + ') = {Suf' + str(i + 1) + '[]};\n'
    f.write(solid_string)
    

# Physical volume tags for MOOSE  

f.write('//+\n')
for i in range(0, files_num):
    solid_string = 'Physical Volume("Block' + str(i + 1) + '", ' + str(i + 1) + ') = {' + str(i + 1) + '};\n'
    f.write(solid_string)

f.close()

# Step solid file to .msh

a = 'integrated.geo'

string0 = str(args.gmesh[0])
string1 = string0 + ' -3 ' + a
print(string1)

os.system(string1)

# Output as integrated.msh file

