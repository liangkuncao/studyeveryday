class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(s: str, cur: List[str]) -> None:
            if not s:
                res.append(cur.copy())
                return
            for i in range(len(s)):
                if is_palindrome(s[:i + 1]):
                    cur.append(s[:i + 1])
                    dfs(s[i + 1:], cur)
                    cur.pop()

        def is_palindrome(s: str) -> bool:
            if not s:
                return False
            return s == s[::-1]

        dfs(s, [])
        return res