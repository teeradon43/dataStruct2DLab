class Node:
    
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return self.data

class LinkedLists:
    def __init__(self, head = None):
        self.head = head
        self.size = 0

    def __str__(self):
        t = self.head
        s = ''
        while t != None:
            s += t.data + ' '
            t = t.next
        return s if s != '' else 'Empty'

    def size(self):
        # return size
        return self.size

    def isEmpty(self):
        # return bool
        return self.size == 0

    def append(self,data):
        # add node follow lists
        n = Node(data)
        if self.head == None:
            self.head = n
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = n
        self.size += 1

    def addHead(self, data):
        # add node before lists
        n = Node(data)
        if self.head == None:
            self.head = n
        else:
            t = self.head
            n.next = t
            self.head = n
        self.size += 1

    def isIn(self, data):
        # check if data is in lists
        t = self.head
        if self.size > 0:
            if t.data == data:
                return 'Found'
            else:
                while t.next != None:
                    t = t.next
                    if t.data == data:
                        return 'Found'
                return 'Not found, '+data+" isn't in list(s)"
        else:
            return 'Not found, list is empty'

    def before(self, data):
        # return node before the data
        if self.isIn(data) == 'Found':
            if self.size > 0:
                t = self.head
                if t.data == data:
                    return 'Error, '+data+' is header'
                else:
                    while t.next != None:
                        if t.next.data == data:
                            return t
                        else:
                            t = t.next
                    return 'Error '+data+' is not found'
        else:
            self.isIn(data)

    def remove(self, data):
        # remove and return node that have exact data
        if self.size > 0:
            t = self.head
            if t.data == data:
                self.head = t.next
                self.size -= 1
            else:
                while t.next != None:
                    if t.next.data == data:
                        t.next = t.next.next
                        self.size -= 1
                        return 'Removed '+data+' from list(s)'
                    else:
                        t = t.next
                return 'Error, '+data+' not found'
        else:
            return 'Error, list is empty'

    def removeTail(self):
        # remove and return last node
        if self.size > 0:
            t = self.head
            if t.next == None:
                self.head = None
                size -= 1
            else:
                while t.next != None:
                    t = t.next
                    if t.next == None:
                        self.remove(t.data)
                        return t.data
        else:
            return 'list have no tail'

    def removeHead(self):
        # remove and return first node
        if self.size > 0:
            t = self.head
            if t.next == None:
                self.head = None
                self.size -= 1
            else:
                self.head = t.next
                self.size -= 1
            return t.data
        else:
            return 'List is Empty'

if __name__ == '__main__':
    L = LinkedLists()
    L.append('B')
    L.addHead('A')
    L.append('C')
    L.append('D')
    # L.removeHead()
    # L.addHead('A')
    # L.removeTail()
    # L.append('D')
    # L.isIn('E')
    # L.before('D')
    # L.remove('D')
    print('List is empty =',L.isEmpty())
    print('Listed =',L)
    print('Listed size =',L.size)
