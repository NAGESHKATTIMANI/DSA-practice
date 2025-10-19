## the objective of this program is to get all stack function using linked list
# -> .pop() and .push() and .peek()
# -> print_all_elements() and count_the_number_of_nodes()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def push(self, data):
        # the push function adds the given node to the end

        Node_1 = Node(data)
        
        # # if list is empty
        if self.head == None:
            self.head = Node_1
            self.count += 1
            return
        
        
        # if list has one node

        if self.head.next == None:
            self.head.next = Node_1
            self.count += 1
            return

        # if list has more than one node

        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next
        
        current_node.next = Node_1
        self.count += 1

    
        
    def pop(self):
        # this function remove the last node from the list 
        # case 1 : if list is empty
        if self.head == None:
            print("The List is empty")
            return
        
        # case 2 : if list has only one node 
        if self.head.next == None:
            self.head == None
            self.count -= 1
            return
        
        # if list has more than one node
        current_node = self.head

        while current_node.next.next != None:
            current_node = current_node.next
        
        current_node.next = None
        self.count -= 1

    def peek(self):
        # this function is to return the data of the last node

        # case 1 : if list is empty
        if self.head == None:
            print("The list is empty")
            return

        # case 2 : if list has only onde node'
        if self.head.next == None:
            return self.head.data
    
        # case 3 : if list has more than two nodes
        currrent_node = self.head 
        while currrent_node.next != None:
            currrent_node = currrent_node.next
        
        return currrent_node.data
    
    def print_all(self):
        # this function return the list of all elements in the LL

        # case 1 : if list is empty
        if self.head == None:
            print("The List is empty")
            return
        
        # case 2 : if there are more than one node
        current_node = self.head
        print("The nodes in the LL are : ")
        while current_node != None:
            print(f"<--{current_node.data}-->")
            current_node = current_node.next


    def get_count(self):
        print(f"The number of nodes in the list are {self.count}")


if __name__ == "__main__":
    Singly_LL = SinglyLinkedList()

    Singly_LL.pop()
    Singly_LL.peek()
    Singly_LL.print_all()

    Singly_LL.push(10)
    Singly_LL.push(20)
    Singly_LL.push(30)
    Singly_LL.push(40)

    Singly_LL.pop()
    Singly_LL.peek()

    Singly_LL.print_all()
    Singly_LL.get_count()



