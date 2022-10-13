class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next  # pointer to the next element


class LinkedList:
    def __init__(self):
        self.head = None  # points to the head

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node  # head is now node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head  # itr = iterator assigned to head.
        llstr = ''  # created a linked list string
        while itr:
            llstr += str(itr.data) + '-->'  # append data from the string
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)  # point to the new node

    def insert_values(self, data_list):
        self.head = None  # wiping out all current values to insert new values
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0  # counter
        itr = self.head
        while itr:
            count+=1
            itr = itr.next  # counting list

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next  # pointing to the next elemtent
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next  # point to elements next element next
                break  # break out of the loop
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1


ll = LinkedList()
# ll.insert_values[23,1,34,24]
# ll.insert_at_beginning(89)
# ll.insert_at_end(10)
# ll.insert_at_end(1)
ll.insert_values(["banana", "mango", "grapes"])
ll.print()
ll.insert_at(0, "apple")
ll.print()
ll.insert_at(2, "jackfruit")

ll.print()
# ll.remove_at(2)
# ll.print()
# print("Length: ", ll.get_length())


