class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adjacency_lists = [[] for _ in range(n)]
        for v1, v2 in edges:
            adjacency_lists[v1].append(v2)
            adjacency_lists[v2].append(v1)
        queue = [v for v, adjacency_list in enumerate(adjacency_lists) if len(adjacency_list) == 1]
        while True:
            temp_queue = list()
            result = list()
            while queue:
                leaf = queue.pop(0)
                result.append(leaf)
                for i in adjacency_lists[leaf]:
                    adjacency_lists[i].remove(leaf)
                    if len(adjacency_lists[i]) == 1:
                        temp_queue.append(i)
            if not temp_queue:
                return result
            queue = temp_queue