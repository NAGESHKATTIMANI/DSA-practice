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

    find_middle_test()