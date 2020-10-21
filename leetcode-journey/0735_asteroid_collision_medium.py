class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for x in asteroids:
            if x > 0:
                stack.append(x)
            else:
                insert_flg = True
                while stack and stack[-1] > 0:
                    if abs(x) < stack[-1]:
                        insert_flg = False
                        break
                    elif abs(x) == stack[-1]:
                        insert_flg = False
                        stack.pop()
                        break
                    else:
                        stack.pop()
                if insert_flg:
                    stack.append(x)
        return stack
