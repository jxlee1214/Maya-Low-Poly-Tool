import maya.cmds as cmds                                              #commands engine.
import maya.mel as mel                                                      #execute mel from python
import os
import random


def create_trunk(pos_x,pos_z,size):
    my_edges = random.randint(3, 5)
    cmds.polyDisc(sides=my_edges, subdivisionMode=4, subdivisions=1, radius=size/4)
    disc_name = cmds.ls(selection=True)
    print(disc_name)
    cmds.move(pos_x, 0, pos_z, componentSpace=True, relative=True)
    crown_x=pos_x
    crown_y=0
    crown_z=pos_z
    for j in range(4):
        transX = (random.random() - 0.5)*0.5*size
        transY = random.uniform(1, 5)*0.4*size
        transZ = (random.random() - 0.5)*0.5*size
        crown_x+=transX
        crown_y+=transY
        crown_z+=transZ
        
        rotateXYZ=(random.random()-0.5)*10

        cmds.polyExtrudeFacet(constructionHistory=True, keepFacesTogether=True,
                              translateX=transX, translateY=transY, translateZ=transZ, rotate=(rotateXYZ,rotateXYZ,rotateXYZ))
        f_name = disc_name[0] + ".f[0:" + str(my_edges - 1) + "]"
        print(f_name)
        cmds.select([f_name])
    crown_pos=[crown_x,crown_y,crown_z]
    return crown_pos

def create_poly(mesh_name, reduce_per):
    # mesh_name=cube_name
    cmds.select(mesh_name)
    cmds.polyRemesh(maxEdgeLength=1.3, collapseThreshold=20)
    cmds.polyRetopo(targetFaceCount=1000, constructionHistory=True)
    cmds.polyTriangulate(constructionHistory=True )
    cmds.select(mesh_name)
    f=cmds.polyEvaluate(face=True)
    print(f)
    face_name=mesh_name[0]+".f[0:"+str(f-1)+"]"
    print(face_name)
    cmds.polySoftEdge(face_name,angle=0,constructionHistory=True)
    cmds.polyReduce(face_name,version=1,percentage=reduce_per)


def create_crown(pos,size):
    size*=2
    cmds.polyCube()
    cube_name = cmds.ls(selection=True)
    print(cube_name)
    cmds.move(pos[0], pos[1]*1.2, pos[2], componentSpace=True, relative=True)
    top_name = cube_name[0] + ".f[1]"
    bottom_name = cube_name[0] + ".f[3]"
    cmds.select([top_name])
    cmds.polyExtrudeFacet(constructionHistory=True, keepFacesTogether=True, translateY=0.5, scale=(0.4,0.5,0.3))
    cmds.select([bottom_name])
    cmds.polyExtrudeFacet(constructionHistory=True, keepFacesTogether=True, translateY=-0.5, scale=(0.4,0.5,0.3))
    cmds.select(cube_name)
    cmds.scale(size*(1+ random.random()),size*(1+ random.random()),size*(1+ random.random()))
    cmds.polySmooth(divisions=2)
    cmds.select(cube_name[0]+".vtx[0:255]",replace=True)
    moveVertex=cmds.polyMoveVertex(constructionHistory=True, random=0.5, localTranslate=(0.1*size,0.1*size,0.1*size))
    print(moveVertex)

    create_poly(cube_name,97)

def create_tree(num, coord, size):
    len_x=coord[0][1]-coord[0][0]
    len_z=coord[1][1]-coord[1][0]
    base=[coord[0][0],coord[1][0]]
    for i in range(num):
        pos_x = random.random()*len_x+base[0]
        pos_z=random.random()*len_z+base[1]
        crown_pos=create_trunk(pos_x,pos_z,size)
        create_crown(crown_pos,size)

def create_a_rock(pos_x, pos_z, size):
    cmds.polyPlatonic(primitive=0, subdivisionMode=0, subdivisions=1)
    cmds.move(pos_x, 0.5, pos_z, componentSpace=True, relative=True)
    rock_name = cmds.ls(selection=True)
    print(rock_name)
    cmds.scale((1 + random.random())*size, size, (1 + random.random())*size)
    cmds.polySmooth(divisions=1)
    cmds.select(rock_name[0] + ".vtx[26:30]", replace=True)
    move_vertex = cmds.polyMoveVertex(constructionHistory=True, random=0.5, localTranslate=(0.1, 0.1, 0.1))
    print(move_vertex)

    create_poly(rock_name, 98)

def create_rock(num, coord, size):
    len_x=coord[0][1]-coord[0][0]
    len_z=coord[1][1]-coord[1][0]
    base=[coord[0][0],coord[1][0]]
    for i in range(num):
        pos_x = random.random()*len_x+base[0]
        pos_z=random.random()*len_z+base[1]
        create_a_rock(pos_x,pos_z,size)

def create_a_cloud(pos_x, pos_y, pos_z, size):
    cloud_name=[]
    for i in range(6):
        cmds.polyCube()
        cloud_scale=random.random()+0.5
        cmds.scale(cloud_scale,cloud_scale,cloud_scale)
        cmds.move((random.random()-1)*2, (random.random()-1), (random.random()-1), componentSpace=True, relative=True)
        cloud_name.append(cmds.ls(selection=True)[0])
        cmds.polyBevel3(fraction=0.7, segments=3,offsetAsFraction=1, miteringAngle=180, angleTolerance=180, mergeVertices=1)

    cmds.select(cloud_name,replace=True)
    cmds.move(pos_x, pos_y, pos_z, componentSpace=True, relative=True)
    
    cloud_name=cmds.polyCBoolOp(ch=False)

    create_poly(cloud_name, 95)
    cmds.scale(size,size,size)

def create_cloud(num, coord, size):
    len_x=coord[0][1]-coord[0][0]
    len_z=coord[1][1]-coord[1][0]
    base=[coord[0][0],10, coord[1][0]]
    for i in range(num):
        pos_x = random.random()*len_x+base[0]
        pos_y= (random.random()+1)*base[1]
        pos_z=random.random()*len_z+base[2]
        create_a_cloud(pos_x,pos_y,pos_z,size)
