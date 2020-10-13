class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dd = collections.defaultdict(list)
        # ct = collections.Counter()
        for i in paths:
            items = i.split(' ')
            path = items[0]
            for f in items[1:]:
                index = f.index('(')
                filename = f[:index]
                content = f[index+1: -1]
                dd[content].append(path + '/' + filename)
                # ct[content] += 1
        # return [dd[i] for i in dd.keys() if ct[i] > 1]
        return [i for i in dd.values() if len(i) > 1]
