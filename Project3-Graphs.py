#Kody Graham
#Dr Hu- Algorithms
#10/18/2025

#Imports most likely needed for all three questions
from typing import Dict, Set, List, Iterable
import argparse

#Problem 1- Kody Graham
#Using bfs, bfs_path, dfs_path, and dfs_iterative from Dr. Hu's online classroom on blackboard

#P1 Imports all from Dr. Hu's example code
import bfs
import bfs_path
import dfs_path as dfspath
import dfs_iterative as dfsit

#For my helpers to build a dict of sets so i can call Dr. Hu's sample code without modifying it
UNDIRECTED_PROBLEM1_EDGES: List[tuple[str,str]] = [

    #
    #Normally dont do this but will space these out so i can keep track of which i have already done

    #Top row
    ('A','B'), ('A','E'),('A','F'),
    ('B','C'),('B','F'),
    ('C','D'),('C','G'),
    ('D','H'),

    #2 row
    ('E','F'),('E','I'),
    ('F','J'),('F','G'),
    ('G','H'),('G','K'),
    ('H','L'),
    #3 row
    ('I','J'),('I','M'),
    ('K','L'),('K','O'),
    ('L','P'),
    #4 row
    ('M','N'),
    ('N','O')
]

#Helper to create a dictionary of sets adjacency so that i dont have to change the sample code Dr. Hu provided
def build_undirected_adj(edges: Iterable[tuple[str,str]]) -> Dict[str, Set[str]]:
    G: Dict[str, Set[str]] = {}
    for u, v in edges:
        G.setdefault(u, set()).add(v)
        G.setdefault(v, set()).add(u)
    return G

#Helper to repeat BFS for unvisited nodes to list all of our connected components
def components_via_bfs(G: Dict[str, Set[str]]) -> List[List[str]]:
    seen: Set[str] = set()
    components: List[List[str]] = []
    for v in sorted(G.keys()):
        if v in seen:
            continue
        order= bfs.bfs(G, v)
        component= sorted(set(order))
        components.append(component)
        seen.update(component)
    return components #Each component as a sorted vertices list

#Same as function above just with DFS instead
def components_via_dfs(G: Dict[str, Set[str]]) -> List[List[str]]:
    seen: Set[str] = set()
    comps: List[List[str]] = []
    for v in sorted(G.keys()): #Determine the outer order
        if v in seen:
            continue
        visited = dfsit._dfs(G,v) #Iterative dfs traverse from sample
        comp = sorted(set(visited))
        comps.append(comp)
        seen.update(comp)
    return comps


def main():
    #Build adjacency and protect against having an empty graph
    G=build_undirected_adj(UNDIRECTED_PROBLEM1_EDGES)
    if not G:
        print("No undirected edges found")
        return

    nodes= sorted(G.keys())
    s, t = nodes[0], nodes[-1]

    #Just added these to give me an easy copy of the graph used for use in our report
    print("Nodes:", nodes)
    print("Edges:", sorted(tuple(sorted(e)) for e in UNDIRECTED_PROBLEM1_EDGES))

    #First Components using both BFS and DFS obviously independently
    print("\nPart a: Connected Components")
    print("BFS components:", components_via_bfs(G))
    print("DFS components:", components_via_dfs(G))

    #Second check for the path for both BFS and DFS
    print(f"\nPart b: Path exists between {s} to {t}.")
    bfs_p= bfs_path.bfs_path(G,s,t)
    print("Reach it?", bfs_p is not None)

    #Third BFS vs. DFS paths
    print(f"\nPart c: BFS vs DFS path from {s} to {t} ")
    if bfs_p is not None:
        print("BFS path (least edges):", bfs_p)
        print("DFS path (one discovered):", dfspath.dfs_path(G,s,t))
    else:
        print(f"No path between {s} and {t}.")

if __name__ == "__main__":
    main()

