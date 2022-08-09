

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linked = LinkedList()
        self.hashMap = {}
        return None

    def get(self, key: int) -> int:
        # print("---get--")
        # print("size ",self.linked.size, "capacity ", self.capacity)
        # self.linked.print()
        # print(self.hashMap.keys())
        # print("get", key)
        node = self.hashMap.get(key)

        if node != None:
            self.linked.refresh(node)
            # self.linked.print()
            return self.hashMap.get(key).contents[1]
        # self.linked.print()
        # print(self.hashMap.keys())
        return -1
    # IF IT ALREADY EXISTS AND WE ARE OVERWRITING WE NEED TO DELETE THE PRIOR

    def put(self, key: int, value: int) -> None:
        # print("---put--")
        # print("size ",self.linked.size, "capacity ", self.capacity)
        # self.linked.print()
        # print(self.hashMap.keys())
        # print("put", key, value)
        node = Node([key, value])
        old = self.hashMap.get(key)
        if old != None:
            # print("old activated",old.contents)
            self.linked.cut(old)
        self.hashMap[key] = node
        
        self.linked.append(node)

        if self.linked.size > self.capacity:
            # print("capacity: ", self.capacity,
                #   " | ", "size: ", self.linked.size)
            remove = self.linked.pop()
            # print(remove, "HEREEEEEEEEEEEE")
            # print(self.hashMap)
            self.hashMap.pop(remove[0])
        # self.linked.print()
        # print(self.hashMap.keys())
        return None


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def append(self, node):
        if self.size == 0:
            self.head = node
            self.tail = self.head
        else:
            self.tail.right = node
            node.left = self.tail
            self.tail = node
        self.size += 1

    def pop(self):
        # self.print()
        if self.size != 0:
            ret = self.head
            self.head = self.head.right
            if self.head != None:
                self.head.left = None
            self.size -= 1
            return ret.contents
        return None

    def cut(self, node):
        ret = node
        if self.size > 1:
            if node==self.head:
                refreshed = self.head
                self.head = self.head.right
                self.head.left = None
                refreshed.right = None
                # ret = refreshed
            elif node == self.tail:
                # ret=node
                self.tail = self.tail.left
            else:
                left = node.left
                right = node.right
                left.right = right
                right.left = left
                # ret=node
        else:
            self.head = None
        self.size -= 1
        # return ret

    def refresh(self, node):
        ret = node
        if self.size > 1 and node != self.tail:
            if node == self.head:
                refreshed = self.head
                self.head = self.head.right
                self.head.left = None
                # refreshed.right = None
                ret=refreshed
            else:
                left = node.left
                right = node.right
                left.right = right
                right.left = left
                ret = node
            self.size -= 1
            ret.detach()
            self.append(ret)

    # def print(self):
    #     counter=0
    #     if self.size != 0:
    #         current = self.head
    #         total = []
    #         while current != None:
    #             total.append(current.contents)
    #             if counter<10:
    #                 print(current.contents)
    #                 counter+=1
    #             current = current.right
                
            # print("List: ", total)
        # else:
            # print("List: []")


class Node:
    def __init__(self, contents, left=None, right=None):
        self.contents = contents
        self.left = left
        self.right = right
    def detach(self):
        self.left=None
        self.right=None


inputCmd = ["LRUCache", "put", "put", "get",
            "put", "get", "put", "get", "get", "get"]
inputVal = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

inputCmd = ["LRUCache", "put", "put", "get", "put", "put", "get"]
inputVal = [[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]]

inputCmd =["LRUCache","put","put","put","put","get","get"]
inputVal =[[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]


inputCmd =["LRUCache","put","put","put","put","get","get","get","get","put","get","get","get","get","get"]
inputVal =[[3],[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]]




lru = LRUCache(inputVal[0][0])
print("=====================================","nullLRU ====")

for i in range(len(inputVal)-1):
    if inputCmd[i+1] == "get":
        print("=====================================",lru.get(inputVal[i+1][0]), "=====================================")
    elif inputCmd[i+1] == "put":
        lru.put(inputVal[i+1][0], inputVal[i+1][1])
        print("=====================================","nullPut ==============")


# linked=LinkedList()
# linked.print()
# linked.append(Node("1"))
# linked.append(Node("2"))
# linked.append(Node("3"))
# linked.print()
# print("popping ",linked.pop())
# linked.print()
# # linked.refresh(2)
# linked.print()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
