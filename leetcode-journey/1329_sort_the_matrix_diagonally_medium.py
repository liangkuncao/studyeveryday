class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonal = defaultdict(list)
        for i, row in enumerate(mat):
            for j, cell in enumerate(row):
                diagonal[i - j].append(cell)
        for d in diagonal.values():
            d.sort(reverse=True)
        for i, row in enumerate(mat):
            for j, cell in enumerate(row):
                row[j] = diagonal[i - j].pop()
        return mat