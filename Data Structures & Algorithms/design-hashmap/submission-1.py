class MyHashMap:

    def __init__(self):
        self.list = [[] for i in range(10**6 + 1)]  

    def put(self, key: int, value: int) -> None:
        self.list[key] = [key, value] 

    def get(self, key: int) -> int:
        if self.list[key] != [] and self.list[key][0] == key:
            return self.list[key][1]
        return -1 

    def remove(self, key: int) -> None:
        self.list[key] = []


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)