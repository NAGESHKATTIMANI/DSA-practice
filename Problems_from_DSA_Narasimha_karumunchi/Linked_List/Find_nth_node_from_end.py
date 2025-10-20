# the objective is to remove the nth Node from the List

from Stack_using_LL import SinglyLinkedList

class linkedListProblems:
    def __init__(self, L_List):
        self.L_List = L_List

    def find_node_from_last(self, position):
        current_node = self.L_List.head
        # starting the list length from 1 because the nth node is considered from 1 not 0
        list_length = 1     

        while current_node != None:
            current_node = current_node.next
            list_length += 1

        search_position = list_length - position 

        current_position = 1
        current_node = self.L_List.head

        if search_position > list_length:
            print("The given position is invalid !!")
            return
        
        while current_position < search_position and current_node != None:
            current_node = current_node.next
            current_position += 1
        
        if current_node == None:
            print("The list has less number of nodes")

        return current_node.data

    def find_nth_node_hash_V2(self, position):
        # using hash table using (key, value)
        # key = position of node value is address of the node

        if self.L_List.head == None:
            print("The list is empty")
            return
        
        # starting the current_position from 1 because the nth node is considered from 1 not
        current_position = 1
        address_dict = {}
        current_node = self.L_List.head
        list_length = 1


        while current_node != None:
            address_dict[current_position] = current_node
            current_position += 1
            current_node = current_node.next

            list_length += 1

        search_position  = list_length - position

        return address_dict.get(search_position)

        
    def find_nth_node_V3(self, position):
        # here we will use a technique where initailly a node will go n time ahead and 
        # when it reaches a position equal to search position
        # another node starts moving and by the time the first node reaches end
        # the second node will be in a position where it has to be so  return it
        lead_node = self.L_List.head
        nth_node = self.L_List.head

        # moving the lead n positions ahead(n = search position)

        # starting the current_position from 1 because the nth node is considered from 1 not
        current_position = 1
        while current_position < position:
            lead_node = lead_node.next
            current_position += 1
        
        while lead_node.next != None:
            lead_node = lead_node.next
            nth_node = nth_node.next

        return nth_node.data



if __name__ == "__main__":
    my_list = SinglyLinkedList()
    my_list.push(10)
    my_list.push(20)
    my_list.push(30)
    my_list.push(40)
    my_list.push(50)


    problems = linkedListProblems(my_list)

    nth_data = problems.find_node_from_last(2)
    print("Data of 2nd node from last:", nth_data)

    print(problems.find_nth_node_hash_V2(2))

    print(problems.find_nth_node_V3(2))