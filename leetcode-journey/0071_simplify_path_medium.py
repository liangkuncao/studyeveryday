class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        paths = re.split(r'\/+', path)
        if len(paths) > 0 and paths[0] == '':
            paths.pop(0)
        if len(paths) > 0 and paths[-1] == '':
            paths.pop()
        for level in paths:
            if level == '.':
                continue
            elif level == '..':
                if len(res) > 0:
                    res.pop()
            else:
                res.append(level)
        return '/' + '/'.join(res)