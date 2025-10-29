from Stack_using_LL import SinglyLinkedList

class LL_Problems:
    def __init__(self, L_List):
        self.L_List = L_List


# problem 1 - Find the middle of the linked list
    def find_middle(self):
        # using slow node and fast node technique
        # if slow node moves by one step
        # the fast node moves by two steps
        # by the time fast node reaches the END the slow node will be pointing to the middle

        # case 1 -  
        if self.L_List.head == None:
            return -1

        slow_node = self.L_List.head
        fast_node = self.L_List.head

        while fast_node and fast_node.next != None:
            slow_node = slow_node.next
            fast_node = fast_node.next.next

        return slow_node.data 
    
# problem 2 - Display the nodes from end
    def print_nodes_from_end(self):

        # case 1 : If list is empty
        if self.L_List.head == None:
            return -1

        stack = []
        current = self.L_List.head

        while current != None:
            stack.append(current.data)
            current = current.next
        
        while stack:
            print(stack.pop())

# problem 3 - Check whether linked list length us even or odd(P-29)
    def check_length(self):
        # find the length of the linked list and find its even or odd
        
        # approach:
        # move a pointer in 2 steps at a time
        # if its pointing to a node its odd
        # else if pointing to None its even

        # case 1 : If list is empty
        if self.L_List.head == None:
            return -1


        current_node = self.L_List.head

        while current_node and current_node.next != None:
            current_node = current_node.next.next

        if current_node == None:
            print("The Length of Linked list is even")
        else:
            print("The Length of Linked list is odd")


if __name__ == "__main__":

    def find_middle_test():
        L_List = SinglyLinkedList()
        L_List.push(10)
        L_List.push(20)
        L_List.push(30)
        L_List.push(40)
        L_List.push(50)

        get_middle = LL_Problems(L_List)
        print(get_middle.find_middle())

    # find_middle_test()

    def print_nodes_from_end_test():
        L_List = SinglyLinkedList()
        L_List.push(10)
        L_List.push(20)
        L_List.push(30)
        L_List.push(40)
        L_List.push(50)

        print_reverse = LL_Problems(L_List)
        print(print_reverse.print_nodes_from_end())

    # print_nodes_from_end_test()

    def check_length():
        L_List = SinglyLinkedList()
        L_List.push(10)
        L_List.push(20)
        L_List.push(30)
        L_List.push(40)
        L_List.push(50)


        find_Length = LL_Problems(L_List)
        find_Length.check_length()

    check_length()