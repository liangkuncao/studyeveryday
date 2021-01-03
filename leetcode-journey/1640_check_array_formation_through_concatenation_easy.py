class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        piece_map = {}
        for piece in pieces:
            piece_map[piece[0]] = piece
        i = 0
        while i < len(arr):
            if arr[i] not in piece_map:
                return False
            for _, n in enumerate(piece_map[arr[i]]):
                if arr[i] != n:
                    return False
                i += 1
        return True