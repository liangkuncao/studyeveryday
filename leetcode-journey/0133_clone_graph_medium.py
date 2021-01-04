"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        node_dict = {None: None}

        def dfs(node: Node) -> Node:
            if node not in node_dict:
                new_node = Node(node.val)
                node_dict[node] = new_node
                for i in node.neighbors:
                    new_node.neighbors.append(dfs(i))
            return node_dict[node]

        return dfs(node)