#Group 18


Input Format:

{no_of_vertex} {no_of_edges}
{no of neighbour of vertex 1} {neighbour 1 of vertex 1} {neighbour 2 of vertex 2} ....
{no of neighbour of vertex 1} {cost of above edge} {cost of above edge} ....
{no of neighbour of vertex 2} {neighbour 1 of vertex 2} {neighbour 2 of vertex 2} ....
{no of neighbour of vertex 2} {cost of above edge} {cost of above edge} ....
.
.
.

Output Format:

Initial cost of partition
partition given by algorithm
Final cost of partition


--------------------------------------------------------------------
                                graph.txt
Input format for graph.txt

{no_of_nodes in graph} {no_of_edges in graph}

--------------------------------------------------------------------
                        random_input_gen_neg.cpp
                
Generates the graph as specified in graph.txt where weight of edges of graaph can be 
and can range from -1000 to 1000

--------------------------------------------------------------------
                        random_input_gen_pos.cpp
                
Generates the graph as specified in graph.txt where weight of edges of graaph can be 
and can range from 0 to 1000

--------------------------------------------------------------------
                            gen_input.txt
                
Generated graph by the random generator or input can be given manually