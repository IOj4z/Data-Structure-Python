import sys


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def set_next(self, new_next):
        self.data = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, nodeData):
        current = self.head
        isPresent = False
        while current and isPresent is False:
            if current.get_data() == nodeData:
                isPresent = True
            else:
                current = current.get_next()
                if current is None:
                    raise ValueError('Data not present in list')
                return current

    def delete(self, nodeData):
        current = self.head
        previous = None
        isPresent = False
        while current and isPresent is False:
            if current.get_data() == nodeData:
                isPresent = True
            else:
                previous = current
                current = current.get_next()

            if current is None:
                raise ValueError('Data not present in list')
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

# s = 'камни'
# j = 'драгоценности'
# c = 0
# for i in range(0, len(j)):
#     if j[i] in s:
#         c += 1

# j = sys.stdin.readline().strip()
# s = sys.stdin.readline().strip()
# result = 0
# for ch in s:
#     if ch in j:
#         result += 1
#
# print(result)
