import unittest

# You may need to change this depending on the file name
from HW5 import Graph


class HW5TestCases(unittest.TestCase):
    """Tests for HW5"""

    # Graphs 1-5 (g1-g5) are copied from the instructions for HW5
    # Graphs 6-7 (g6-67) are generated with igraph: (https://igraph.org/python/doc/igraph.GraphBase-class.html#Erdos_Renyi)
    
    g1 = {
        'A': ['B','D','G'],
        'B': ['A','E','F'],
        'C': ['F'],
        'D': ['A','F'],
        'E': ['B','G'],
        'F': ['B','C','D'],
        'G': ['A','E'],
    }
    g2 = {
        'F': ['D','C','B'],
        'A': ['G','D','B'],
        'B': ['F','A','E'],
        'E': ['G','B'],
        'C': ['F'],
        'D': ['F','A'],
        'G': ['A','E'],
    }
    g3 = {
        'B': [('E',3),('C',5)],
        'F': [],
        'C': [('F',2)],
        'A': [('D',3),('B',2)],
        'D': [('C',1)],
        'E': [('F',4)],
    }
    g4 = {
        'Bran': ['East','Cap'],
        'Flor': [],
        'Cap': ['Flor'],
        'Apr': ['Dec','Bran'],
        'Dec': ['Cap'],
        'East': ['Flor'],
    }
    g5 = {
        'A': ['B','C'],
        'B': ['A','D'],
        'C': ['A','D','E'],
        'D': ['B','C','E'],
        'E': ['C','D','F'],
        'F': ['E'],
    }
    g6 = {
        # 0--2 0--3 1--3 0--5 4--5 2--6 5--6 2--7 5--7
        0: [2, 3, 5],
        1: [3],
        2: [0, 6, 7],
        3: [0, 1],
        4: [5],
        5: [0, 4, 6, 7],
        6: [2, 5],
        7: [2, 5],
    }
    g7 = {
        # 0--1 2--3 2--4 0--5 1--5 3--5 4--6 5--7 6--7
        0:  [1, 5],
        1:  [0, 5],
        2:  [3, 4],
        3:  [2, 5],
        4:  [2, 6],
        5:  [0, 1, 3, 7],
        6:  [4, 7],
        7:  [5, 6],
    }

    graphs = [g1, g2, g3, g4, g5, g6, g7]

    def test_bfs(self):
        """Is the graph correctly traversed using BFS?"""
        startNodes = ['A', 'A', 'A', 'Apr', 'A', 0, 3]
        expected = [
            ['A', 'B', 'D', 'G', 'E', 'F', 'C'],
            ['A', 'B', 'D', 'G', 'E', 'F', 'C'],
            ['A', 'B', 'D', 'C', 'E', 'F'],
            ['Apr', 'Bran', 'Dec', 'Cap', 'East', 'Flor'],
            ['A', 'B', 'C', 'D', 'E', 'F'],
            [0, 2, 3, 5, 6, 7, 1, 4],
            [3, 2, 5, 4, 0, 1, 7, 6],
        ]
        graphs = HW5TestCases.graphs
        i = 0
        while i < len(graphs):
            g = Graph(graphs[i])
            start = startNodes[i]
            self.assertEqual(g.bfs(start), expected[i], f"Failed BFS test for g{i + 1}")
            i += 1


    def test_dfs(self):
        """Is the graph correctly traversed using DFS?"""
        startNodes = ['A', 'A', 'A', 'Apr', 'A', 2, 6]
        expected = [
            ['A', 'B', 'E', 'G', 'F', 'C', 'D'],
            ['A', 'B', 'E', 'G', 'F', 'C', 'D'],
            ['A', 'B', 'C', 'F', 'E', 'D'],
            ['Apr', 'Bran', 'Cap', 'Flor', 'East', 'Dec'],
            ['A', 'B', 'D', 'C', 'E', 'F'],
            [2, 0, 3, 1, 5, 4, 6, 7],
            [6, 4, 2, 3, 5, 0, 1, 7],
        ]
        graphs = HW5TestCases.graphs
        i = 0
        while i < len(graphs):
            g = Graph(graphs[i])
            start = startNodes[i]
            self.assertEqual(g.dfs(start), expected[i], f"Failed DFS test for g{i + 1}")
            i += 1




if __name__ == '__main__':
	unittest.main(exit = False)