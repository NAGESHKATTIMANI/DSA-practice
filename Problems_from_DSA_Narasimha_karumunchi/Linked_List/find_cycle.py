from Stack_using_LL import SinglyLinkedList

class Linked_List_Problems:
    def __init__(self, L_List):
        self.L_List = L_List
    
    def find_cycle(self):
        # we can say that there is a cycle in Linked list
        # if the there is duplicate of address this says there is a cycle
        # no two nodes can have same addeess if so then there is a cycle

        # maintain a dictionary helps so find duplicate

        address_set = set()

        current_node = self.L_List.head

        while current_node and current_node.next != None:
            if current_node.next not in address_set:
                address_set.add(current_node)
                current_node = current_node.next
            else:
                return True
        return False
    

    def find_cycle_v2(self):
        # using slow node and fast node
        # when slow node move 1 node   The fast node moves 2 nodes 
        # by this algo if there is a cycle 
        # both fast node and slow node meets at a point

        slow_node = self.L_List.head
        fast_node = self.L_List.head

        while fast_node and fast_node.next != None:
            slow_node = slow_node.next
            fast_node = fast_node.next.next

            if slow_node == fast_node:
                return True
        return False
    
    def find_cycle_V2(self):
        
        slow_node = self.L_List.head
        fast_node = self.L_List.head

        while fast_node and fast_node.next != None:
            slow_node = slow_node.next
            fast_node = fast_node.next.next

            if slow_node == fast_node:
                slow_node = self.L_List.head
                
                while slow_node != fast_node: 
                    slow_node = slow_node.next
                    fast_node = fast_node.next
                
                return slow_node
        return -1

"""
We can find at which points there was a cycle 
By Floyds Algorithm:

- There are two node slow_node(tortise_node) and fast_node(hare_node)
- The Tortise moves 1 node at a time and fast node moves 2 nodes at a time
- If there is a cycle both meet a point
- now move the slow_node to head 
- Move both node one node eachtime 
- at a point they will meet where one node is pointing to two node
- There is the cycle at the slow_node
"""






if __name__ == "__main__":
    S_List = SinglyLinkedList()

    S_List.push(10)
    S_List.push(20)
    S_List.push(30)
    S_List.push(40)
    S_List.push(50)

    problems = Linked_List_Problems(S_List)

    print(problems.find_cycle())

