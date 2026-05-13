"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_map = {}

        def dfs(root, node_map):
            if root is None:
                return None
            
            if root in node_map:
                return node_map[root]
            else:
                cloned = Node(root.val)
                node_map[root] = cloned
                for neighbor in root.neighbors:
                    cloned.neighbors.append(dfs(neighbor, node_map))
                return cloned
            
        return dfs(node, node_map)
        
            
                

        