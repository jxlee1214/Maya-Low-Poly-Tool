<!-- # Maya-Low-Poly-Tool -->
# README for Maya Low Poly Tool

## 1. What is Low Poly Tool

Low poly tool provides function for auto generating low poly objects. It provides tree, rock and cloud mesh random generating. You can also select your own object and make it low poly.

![overview](.\pic\overview.png)

## 2. How to use

### 2.1 Import Script

- Open Maya->Windows->General Editors->Script Editor

- Script Editor->File->Open Script

  - In File Explorer, select proj3GUI.py

- In line 4, change _location_ in _sys.path.append('location')_ . _location_ is where _proj3function.py_ locates. For example:

  ```python
  sys.path.append('C:\Users\admin\Desktop')
  ```

- Press _Execute_ in menu or _Ctrl Enter_ to run the script. The window will appear.

  ![1640001047916](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\1640001047916.png)

### 2.2 Create Object

- **Create Low Poly Tree**
  1. _Tree Number_: Number of trees. Default: 1
  2. _Tree Size_: Size of trees. Default: 1.0
  3. _Coord_: Coordinate range in the scene that trees will be randomly located. If you want to specify the coordinate, keep the two number in coordinate same.
  4. Button _Create Tree_: Click to create trees with above parameters.

![1639995519859](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\1639995519859.png)

- **Create Low Poly Rock**

  Similar to _**Create Low Poly Tree**_.

![1639995549854](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\1639995549854.png)

- **Create Low Poly Cloud**

  Similar to _**Create Low Poly Tree**_. The default _Y_ lies between [10, 20].  

![1639999392426](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\1639999392426.png)

### 2.3 Create Low Poly for Any Selected Mesh

1. Select a mesh in scene

2. _Reduced Amount_: Control the face amounts that the low poly mesh will have. Range: [0,100.0]. Default is 98.0. Value in [95, 99] will be nice. 

   

**Notice**: If target mesh has too much lines, it will be slow to process. It can only process polygons, not NURBS. 



