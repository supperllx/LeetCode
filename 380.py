class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []
        self.d = {}
        self.count = 0


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.d:
            self.l.append(val)
            self.d[val] = self.count
            self.count += 1
            return True
        else:
            return False



    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.d:
            temp_i = self.d[val]
            self.l[temp_i], self.l[-1] = self.l[-1], self.l[temp_i]
            self.d[self.l[temp_i]] = temp_i
            self.d.pop(val)
            self.l.pop()
            self.count -= 1
            return True
        else:
            return False
    

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        i = random.randint(0, self.count-1)
        return self.l[i]




# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()