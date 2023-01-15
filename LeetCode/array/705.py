# https://leetcode.com/problems/design-hashset/

class MyHashSet:
    def __init__(self, hashSet=list()):
        self.hashSet = hashSet
        self.hashSet = []

    def add(self, key: int) -> None:
        if not __class__.contains(self, key):
            self.hashSet.append(key)

    def remove(self, key: int) -> None:
        if __class__.contains(self, key):
            self.hashSet.remove(key)
        
    def contains(self, key: int) -> bool:
        return key in self.hashSet
    
    def showSet(self):
        return self.hashSet

operations = ["MyHashSet","add","remove","add","contains","add","remove","add","add","add","add"]
keys = [[],[6],[4],[17],[14],[14],[17],[14],[14],[18],[14]]
result = []

for index, method in enumerate(operations):
    if method == "MyHashSet":
        obj = MyHashSet()
    elif method == 'add':
        obj.add(keys[index][0])
    elif method == 'remove':
        obj.remove(keys[index][0])
    elif method == 'contains':
        result.append(obj.contains(keys[index][0]))
        continue
    result.append(None)
print(result)

        


# Your MyHashSet object will be instantiated and called as such:
obj2 = MyHashSet()
print(obj2.hashSet)
# obj.add(int([18]))
# obj.contains(18)
# obj.remove(key)
# param_3 = obj.contains(key)   