"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        queue = list()
        queue.append(node)
        node_map = dict()
        while queue:
            pop_node = queue.pop(0)
            node_map[pop_node] = Node(pop_node.val)
            for i in pop_node.neighbors:
                if i not in node_map:
                    queue.append(i)

        queue = list()
        queue.append(node)
        visited = [node]
        while queue:
            pop_node = queue.pop(0)
            for i in pop_node.neighbors:
                node_map[pop_node].neighbors.append(node_map[i])
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
        return node_map[node]


class Solution2:
    def cloneGraph(self, node: 'Node') -> 'Node':
        node_map = dict()

        def DFS(node: 'Node') -> 'Node':
            if not node:
                return node
            if node not in node_map:
                new_node = Node(node.val)
                node_map[node] = new_node
                for i in node.neighbors:
                    new_node.neighbors.append(DFS(i))
            return node_map[node]

        return DFS(node)