# design hashmap without any built in hashmap libraries

class MyHashMap:
    def __init__(self):
        print("MyHashMap")
        self.map = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        value = self.map[key]
        return value if value != None else -1

    def remove(self, key: int) -> None:
        self.map[key] = None

    def printMap(self):
        for value in self.map:
            if value:
                print([value,self.map[value]],end="")
        print("")

def main():
    hashMap = MyHashMap()
    hashMap.put(1,1)
    hashMap.printMap()
    hashMap.put(2,2)
    hashMap.printMap()
    print(hashMap.get(1))
    print(hashMap.get(3))
    hashMap.put(2,1)
    hashMap.printMap()
    print(hashMap.get(2))
    hashMap.remove(2)
    hashMap.printMap()
    print(hashMap.get(2))
if __name__ == "__main__":
    main()
