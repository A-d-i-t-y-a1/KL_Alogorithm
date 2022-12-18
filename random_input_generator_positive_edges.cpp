//This is random input generator where edge cost can be any integer btw 0 and 1000

#include<bits/stdc++.h>
#include <time.h>
using namespace std;  
int main(){
    #ifndef ONLINE_JUDGE
	freopen("graph.txt", "r", stdin);                   
	freopen("gen_input.txt", "w", stdout);
    #endif

    srand(time(0));

    //attribute of graph
    int no_of_node;
    cin>>no_of_node;
    int no_of_edge;
    cin>>no_of_edge;
    cout<<no_of_node<<" "<<no_of_edge<<"\n";

    //adjacency list of nodes with cost
    vector<pair<int,int>> adj_list[no_of_node+1];
    set<pair<int,int>> edges;

    //run the loop till we don't get the required no. of edges in graph
    while(edges.size()<no_of_edge){

        int u=(rand()%no_of_node)+1;
        int v=(rand()%no_of_node)+1;

        if(u>v){
            swap(u,v);
        }
        if((u==v)||edges.find({u,v})!=edges.end()){
            continue;
        }

        int cost_of_edge=rand()%10;

        adj_list[u].push_back({v,cost_of_edge});
        adj_list[v].push_back({u,cost_of_edge});
        edges.insert({u,v});
    }

    //printing the randomly formed graph
    for(int i=1;i<=no_of_node;i++){
        sort(adj_list[i].begin(),adj_list[i].end());
        std::cout<<adj_list[i].size();
        for(auto &it: adj_list[i]){
            std::cout<<" "<<it.first;
        }
        std::cout<<"\n";
        std::cout<<adj_list[i].size();
        for(auto &it: adj_list[i]){
            std::cout<<" "<<it.second;
        }
        std::cout<<"\n";
    }
  
    return 0;
}