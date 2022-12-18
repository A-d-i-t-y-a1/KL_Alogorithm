import random

def merge(arr,l,m,r):
    n1=m-l+1
    n2=r-m
 
    #temporary array
    L=[]
    for i in range (0,n1):
        temp1=[]
        temp1.append(0)
        temp1.append(0)
        L.append(temp1)
    R=[]
    for i in range (0,n2):
        temp2=[]
        temp2.append(0)
        temp2.append(0)
        R.append(temp2)

    for i in range(0,n1):
        L[i][0]=arr[l+i][0]
        L[i][1]=arr[l+i][1]
 
    for j in range(0,n2):
        R[j][0]=arr[m+1+j][0]
        R[j][1]=arr[m+1+j][1]
 
    # Merge the temp arrays back into arr[l..r]
    i=0     # Initial index of first subarray
    j=0     # Initial index of second subarray
    k=l     # Initial index of merged subarray
 
    while i<n1 and j<n2:
        if L[i][0]<=R[j][0]:
            arr[k][0]=L[i][0]
            arr[k][1]=L[i][1]
            i+=1
        else:
            arr[k][0]=R[j][0]
            arr[k][1]=R[j][1]
            j+=1
        k+=1
 
    # Copy the remaining elements of L[], if there are any
    while i<n1:
        arr[k][0]=L[i][0]
        arr[k][1]=L[i][1]
        i+=1
        k+=1
 
    # Copy the remaining elements of R[], if there are any
    while j<n2:
        arr[k][0]=R[j][0]
        arr[k][1]=R[j][1]
        j+=1
        k+=1

def mergeSort(arr,l,r):
    if l<r:
        # Same as (l+r)//2, but avoids overflow for large l and h
        m = int(l+(r-l)//2)

        # Sort first and second halves
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        merge(arr,l,m,r)

#reading from file
file=open("gen_input.txt",'r')

first_line=file.readline()
v_list=first_line.split()

#no of nodes and edges
no_of_nodes=int(v_list[0])
no_of_edges=int(v_list[1])

#Adjacency matrix
rows=no_of_nodes
cols=no_of_nodes
edges=[]
for i in range (0,rows+1):
    edge=[]
    for j in range (0,cols+1):
        edge.append(0)
    edges.append(edge)

#Adjacency list
adj_list=[]
temp_list=[]
temp_list.append(0)
adj_list.append(temp_list)

n=no_of_nodes
all_node=[]
for i in range (1,n+1):
    all_node.append(i)

random.shuffle(all_node)

print("Initial partition is :")
ini_part1=""
ini_part2=""
for i in range (0,int(n/2)):
    ini_part1+=" "+str(all_node[i])
for i in range (int(n/2),n):
    ini_part2+=" "+str(all_node[i])

print(ini_part1)
print(ini_part2)

type_of_node=[]
type_of_node.append(0)
for i in range (1,n+1):
    type_of_node.append(0)

#marking first n/2 elements to be type 1 using a shuffle function
for i in range (0,int(n/2)):
    type_of_node[all_node[i]]=1

LOW=-100000000000

for i in range (1,no_of_nodes+1):

    #getting the edges
    line=file.readline()
    edge_list=line.split()
    #getting the cost of edges
    line=file.readline()
    cost_list=line.split()

    #first line will give the no. of neighbour
    no_of_neigh=int(edge_list[0])
    neighbour=[]

    #storing the cost in adjcency matrix and neighbours in list 
    for j in range(1,no_of_neigh+1):
        edges[i][int(edge_list[j])]=int(cost_list[j])
        neighbour.append(int(edge_list[j]))
    
    adj_list.append(neighbour)

#partition size into 2 equal subgroups  
partition_size=int(no_of_nodes/2)
exter=[]
inter=[]

#external edges cost
exter.append(0)
#internal edges cost
inter.append(0)

for i in range(1,no_of_nodes+1):
    inter.append(0)
    exter.append(0)
    size=len(adj_list[i])
    #finding cost for internal and external edges
    for j in range(0,size):
        #if type is not equal then they belong to different partition
        if type_of_node[i]!=type_of_node[adj_list[i][j]]:
            exter[i]+=edges[i][adj_list[i][j]]
        else:
            inter[i]+=edges[i][adj_list[i][j]]

initial_cost=0
for i in range (0,int(n/2)):
    initial_cost+=exter[all_node[i]]

print("Initial Cost: ",initial_cost)

#for making the swapped nodes
mark=[]
for i in range (0,n+1):
    mark.append(0)

#gain for each step
gain_pre=[]
gain_pre.append(0)

#storing the swapped pair of each iteration
swapped_pair=[]

dval=[]
#finding dval for each node
for i in range (0,n+1):
    dval.append(exter[i]-inter[i])

for i in range (1,partition_size+1):

    part1_gain=[]
    part2_gain=[]

    #finding the node with highest gain among remaining nodes for partition 1
    for j in range (0,partition_size):
        if mark[all_node[j]]==1:
            continue
        pair_list=[]
        pair_list.append(dval[all_node[j]])
        pair_list.append(all_node[j])
        part1_gain.append(pair_list)

    #finding the node with highest gain among remaining nodes for partition 2
    for j in range (partition_size,n):
        if mark[all_node[j]]==1:
            continue
        pair_list=[]
        pair_list.append(dval[all_node[j]])
        pair_list.append(all_node[j])
        part2_gain.append(pair_list)

    #Using Merge sort 
    size=len(part1_gain)
    mergeSort(part1_gain,0,size-1)
    mergeSort(part2_gain,0,size-1)

    #sorting in descending order
    part1_gain.reverse()
    part2_gain.reverse()

    #list for storing the pair of elements to be swapped
    best_pair=[]
    best_pair.append(-1)
    best_pair.append(-1)
    best_gain=LOW

    #checking for each combination of pair
    for k in range (0,size):
        for l in range (0,size):
            # if part1_gain[k][0]+part2_gain[l][0]<best_gain:
            #     break
            curr_gain=part1_gain[k][0]+part2_gain[l][0]-2*(edges[part1_gain[k][1]][part2_gain[l][1]])
            if curr_gain>best_gain:
                best_gain=curr_gain
                best_pair[0]=(part1_gain[k][1])
                best_pair[1]=(part2_gain[l][1])

    #making the swapped list so that nodes are not swapped again
    mark[best_pair[0]]=1
    mark[best_pair[1]]=1
    swapped_pair.append(best_pair)
    gain_pre.append(best_gain)

    #updating the Dval after swapping
    for i in range (0,partition_size):
        if mark[all_node[i]]==1:
            continue
        # if i==best_pair[0] or i==best_pair[1]:
        #     continue
        dval[all_node[i]]=dval[all_node[i]]+2*edges[all_node[i]][best_pair[0]]-2*edges[all_node[i]][best_pair[1]]
    
    for i in range (partition_size,n):
        if mark[all_node[i]]==1 :
            continue
        # if i==best_pair[1] or i==best_pair[0]:
        #     continue
        dval[all_node[i]]=dval[all_node[i]]+2*edges[all_node[i]][best_pair[1]]-2*edges[all_node[i]][best_pair[0]]

#prefix sum of gain of interation before it
for i in range (1,partition_size+1):
    gain_pre[i]=gain_pre[i]+gain_pre[i-1]

max_pre=0
k=0
for i in range (1,partition_size+1):
    if max_pre<gain_pre[i]:
        max_pre=gain_pre[i]
        k=i

temp=[]
for i in range (0,n+1):
    temp.append(0)

#partition after swapping first k iteration
part1_ans=[]
part2_ans=[]
for i in range (0,k):
    temp[swapped_pair[i][0]]=1
    temp[swapped_pair[i][1]]=1

for i in range (0,partition_size):
    if temp[all_node[i]]==0:
        part1_ans.append(all_node[i])
        
for i in range (0,k):
    part1_ans.append(swapped_pair[i][1])

for i in range (partition_size,n):
    if temp[all_node[i]]==0:
        part2_ans.append(all_node[i])
    
for i in range (0,k):
    part2_ans.append(swapped_pair[i][0])
    
print("Final partition is :")
partition1=""
partition2=""
for i in part1_ans:
    partition1+=" "+str(i)
    
for i in part2_ans:
    partition2+=" "+str(i)

print(partition1)
print(partition2)

final_cost=initial_cost-gain_pre[k]
print("Final Cost : ",final_cost)
            











