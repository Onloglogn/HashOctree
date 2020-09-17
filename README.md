# HashOctree
``` def hashOctree(pts, sz): ``` 

An implementation of hashed octree for python. The first bit of the integer is just for not creating ambiguity, sz the size of the box and pts are the points to add to octree.

The outputed dictionary maps to a tuple where the fist element is the first point to go to the cell, and the second is an integer with value 1 if it has a child node and zero otherwise.
If n is the integer value representing a particular direction, say for example x, then n<<1 would be equivalent to choosing all child nodes with x coordinate at most sz/2, and x<<1+1, would be equivalen to choosing all child nodes with x coordinate at least sz/2. 

if (x, y, z) is a node,where x, y, z are integers, then its parent node is (x>>1, y>>1, z>>1).
