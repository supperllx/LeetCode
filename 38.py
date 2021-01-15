class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:  return '1'
        else:
            last = self.countAndSay(n - 1)
            cur = ''
            i = 0
            temp = last[0]
            count = 0
            while i < len(last):
                if last[i] == temp:
                    count += 1
                    i += 1
                else:
                    cur = cur + '{0}{1}'.format(count, temp)
                    temp = last[i]
                    count = 0
            cur = cur + '{0}{1}'.format(count, temp)
            return cur