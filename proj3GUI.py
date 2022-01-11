from functools import partial
import sys
#You should change location to proj3function.py's location
sys.path.append('location')
import proj3function as proj

cmds.window(width=200)
cmds.columnLayout(adjustableColumn=True)

#Tree
cmds.text(label='Tree', align='center')
cmds.text(label='Tree Number', align='left')
tree_num_window = cmds.intField()
cmds.text(label='Tree Size', align='left')
tree_size_window = cmds.floatField()
tree_x_window = cmds.floatFieldGrp(numberOfFields=2, label='Coord X', value1=0, value2=5)
tree_z_window = cmds.floatFieldGrp(numberOfFields=2, label='Coord Z', value1=0, value2=5)

def onClick_create_tree(*args):
    # print(*args)
    num_tree = cmds.intField(tree_num_window, q=True, value=True)
    size_tree = cmds.floatField(tree_size_window, q=True, value=True)
    coord_x = cmds.floatFieldGrp(tree_x_window, q=True, value=True)
    coord_z = cmds.floatFieldGrp(tree_z_window, q=True, value=True)
    print(coord_x)
    coord = [coord_x, coord_z]
    proj.create_tree(num_tree, coord, size_tree)
    # print(type(*args))
    print("succeed")

cmds.intField(tree_num_window, e=True, value=True, minValue=0)
cmds.floatField(tree_size_window, e=True, value=True, minValue=0)

cmds.button(label="Create Tree", command=onClick_create_tree)


#Rock
cmds.text(label='Rock', align='center')
cmds.text(label='Rock Number', align='left')
rock_num_window = cmds.intField()
cmds.text(label='Rock Size', align='left')
rock_size_window = cmds.floatField()
rock_x_window = cmds.floatFieldGrp(numberOfFields=2, label='Coord X', value1=0, value2=5)
rock_z_window = cmds.floatFieldGrp(numberOfFields=2, label='Coord Z', value1=0, value2=5)

def onClick_create_rock(*args):
    # print(*args)
    num_rock = cmds.intField(rock_num_window, q=True, value=True)
    size_rock = cmds.floatField(rock_size_window, q=True, value=True)
    coord_x = cmds.floatFieldGrp(rock_x_window, q=True, value=True)
    coord_z = cmds.floatFieldGrp(rock_z_window, q=True, value=True)
    print(coord_x)
    coord = [coord_x, coord_z]
    proj.create_rock(num_rock, coord, size_rock)
    # print(type(*args))
    print("succeed")


cmds.intField(rock_num_window, e=True, value=True, minValue=0)
cmds.floatField(rock_size_window, e=True, value=True, minValue=0)

cmds.button(label="Create Rock", command=onClick_create_rock)


#Cloud
cmds.text(label='Cloud', align='center')
cmds.text(label='Cloud Number', align='left')
cloud_num_window = cmds.intField()
cmds.text(label='Cloud Size', align='left')
cloud_size_window = cmds.floatField()
cloud_x_window = cmds.floatFieldGrp(numberOfFields=2, label='Coord X', value1=0, value2=5)
cloud_z_window = cmds.floatFieldGrp(numberOfFields=2, label='Coord Z', value1=0, value2=5)

def onClick_create_cloud(*args):
    # print(*args)
    num_cloud = cmds.intField(cloud_num_window, q=True, value=True)
    size_cloud = cmds.floatField(cloud_size_window, q=True, value=True)
    coord_x = cmds.floatFieldGrp(cloud_x_window, q=True, value=True)
    coord_z = cmds.floatFieldGrp(cloud_z_window, q=True, value=True)
    print(coord_x)
    coord = [coord_x, coord_z]
    proj.create_cloud(num_cloud, coord, size_cloud)
    # print(type(*args))
    print("succeed")

cmds.intField(cloud_num_window, e=True, value=True, minValue=0)
cmds.floatField(cloud_size_window, e=True, value=True, minValue=0)

cmds.button(label="Create Cloud", command=onClick_create_cloud)

#Low poly for any mesh
cmds.text(label='Low poly for selected mesh', align='center')
cmds.text(label='Reduced Amount', align='left')
lowpoly_window = cmds.floatField()
def onClick_create_lowpoly(*args):
    reduced = cmds.floatField(lowpoly_window, q=True, value=True)
    mesh_name = cmds.ls(selection=True)
    proj.create_poly(mesh_name,reduced)
 
cmds.floatField(lowpoly_window, e=True, value=98, minValue=0, maxValue=100)   
cmds.button(label="Make selected mesh low poly", command=onClick_create_lowpoly)


cmds.showWindow()