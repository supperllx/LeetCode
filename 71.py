class Solution:
    def simplifyPath(self, path: str) -> str:
        s = list(filter(lambda x: x not in {'', '.'}, path.split('/')))
        # s = path.split('/')
        res = []
        for i in s:
            # if i in {'', '.'}:  continue
            if i == '..':
                if res: res.pop()
            else:   res.append(i)
        return '/' + '/'.join(res)