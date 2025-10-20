#Kody Graham
#Dr Hu- Algorithms
#10/18/2025

#Imports most likely needed for all three questions
from typing import Dict, Set, List, Iterable
import argparse

#Problem 1- Kody Graham
#Using bfs, bfs_path, dfs_path, and dfs_iterative from Dr. Hu's online classroom on blackboard

#P1 Imports
import bfs
import bfs_path
import dfs_path as dfspath
import dfs_iterative as dfsit

#GLOBAL DONT CHANGE!!!!
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