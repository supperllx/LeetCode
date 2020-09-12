class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.l = []
        self.count = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val not in self.d:
            self.l.append(val)
            self.d[val] = {self.count}
            self.count += 1
            return True
        else:
            self.l.append(val)
            self.d[val].add(self.count)
            self.count += 1
            return False


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val in self.d:
            temp_i = self.d[val].pop()
            tail_i = self.count - 1
            self.l[temp_i], self.l[tail_i] = self.l[tail_i], self.l[temp_i]
            self.d[self.l[temp_i]].add(temp_i)
            self.d[self.l[temp_i]].remove(tail_i)
            self.l.pop()
            self.count -= 1
            if len(self.d[val]) == 0:
                self.d.pop(val)
            return True
        else:
            return False


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        i = random.randint(0, self.count -1)
        return self.l[i]



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()