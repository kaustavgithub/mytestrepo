class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def set_next(self, next_node):
        self.next = next_node

    def get_next(self):
        return self.next

    def set_prev(self, prev_node):
        self.prev = prev_node

    def get_prev(self):
        return self.prev

    def __str__(self):
        return f'''--------------------\n| <- | {self.data} | -> |\n--------------------'''


class SinglyLinkedList:
    def __init__(self):
        self.head = None

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

    def search(self, data):
        current = self.head
        while current:
            if data == current.get_data():
                return current
            else:
                current = current.get_next()
        return current

    def delete(self, data):
        prev = current = self.head
        while current:
            if data == current.get_data():
               prev.set_next(current.get_next())
               print('deleted node is')
               print(str(current))
               return
            else:
                prev = current
                current = current.get_next()
        print('Item not found')
        return

    def __str__(self):
        current = self.head
        llist = ''
        while current:
            llist += '\n' + str(current)
            current = current.get_next()
        if len(llist)== 0:
            return 'Linked list is empty'
        else:
            return llist


if __name__ == '__main__':
    sl = SinglyLinkedList()
    sl.insert(5)
    sl.insert(8)
    sl.insert(2)
    sl.insert(7)
    print('%s' % sl)
    print(sl.size())
    sl.delete(8)
    print(sl.size())
    print('%s' % sl)
