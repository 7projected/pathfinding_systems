G cast = distance from node to START node
H cast = distance from node to END node
F cast = G + H

Psuedocode:
    Node = coords
    Calculate F cast for all Surrounding nodes
    Find lowest F cast, if multiple are the same F, look for lowest H cast
    Repeat

needs 
something to calculate f cast for all cubes surrounding self