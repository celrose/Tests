from linkedlist.node import LinkedListNode

class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        temp = LinkedListNode(item, None)

        if self.size() == 0:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

        return self.head

    def append(self, item):
        temp = LinkedListNode(item, None)

        if self.size() == 0:
            self.head = temp
            return self.head
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = temp
            return current.next


    def insert(self, item, position):
        if position < 0 or position > self.size():
            return False
        else:
            temp = LinkedListNode(item, None)
            if position == 0:
                temp.next = self.head
                self.head = temp
            else:
                count = 0
                current = self.head
                while count != position - 1:
                    current = current.next
                    count += 1
                hold = current.next
                current.next = temp
                temp.next = hold
            return temp

    def remove(self, item):
        current = self.head
        previous = None

        while current != None: 
            if current.value == item:
                if self.head == current:
                    self.head = current.next
                else:
                    previous.next = current.next
                current.next = None
                return current

            else:
                previous = current
                current = current.next

        return current

    def search(self, item):
        found = False
        current = self.head

        while not found:
            if current == None:
                return False
            elif current.value == item:
                found = True
                break
            else:
                current = current.next
        return found


    def size(self):
        if self.head == None:
            return 0
        else:
            current = self.head
            count = 1
            while current.next != None:
                count += 1
                current = current.next

            return count
