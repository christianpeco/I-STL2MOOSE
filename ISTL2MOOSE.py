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
                    help='number of stl files to process')

# Gmesh path to executable in the system
parser.add_argument('--gmesh', metavar='gmesh_path', type=str, nargs='+', required=True,
                    help='path to current gmesh')

# FreeCAD path to executable in the system
parser.add_argument('--freecad', metavar='freecad_path', type=str, nargs='+', required=True,
                    help='path to current freecad')

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


f.write('BooleanFragments{')

for i in range(0, files_num):
    solid_string = args.N[i][:-4] + '_solid.step'
    string_vol = 'Volume{' + str(i+1) + '};'
    f.write(string_vol)

f.write('Delete;}{ }\n')

f.close()


# Step solid file to .msh

a = 'integrated.geo'

string1 = "/Applications/Gmsh.app/Contents/MacOS/gmsh -3 " + a
print(string1)

os.system(string1)
os.system("ls -l")
