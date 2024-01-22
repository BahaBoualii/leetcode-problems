import random

class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.index_map = {}

    def search(self, val):
        return val in self.index_map

    def insert(self, val: int) -> bool:
        if self.search(val):
            return False
        
        self.lst.append(val)
        self.index_map[val] = len(self.lst) - 1
        return True

    def remove(self, val: int) -> bool:
        if not self.search(val): 
            return False
        
        idx = self.index_map[val]
        self.lst[idx] = self.lst[-1]
        self.index_map[self.lst[-1]] = idx
        self.lst.pop()
        del self.index_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()