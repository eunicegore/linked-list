
# Defines a node in the singly linked list
from itertools import count


class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
      self.head = None # keep the head private. Not accessible outside this class

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: ?
    # Space Complexity: ?
    def get_first(self):
        if self.head != None:
            return self.head.value
        return None

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def add_first(self, value):
        # new_node=Node(value)
        # new_node.next = self.head
        # self.head = new_node

        if self.head == None:
            new_node= Node(value)
            self.head = new_node
        else:
            new_node=Node(value, self.head)
            self.head=new_node
        return self.head

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: ?
    # Space Complexity: ?
    def search(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                return True
            else:
                current = current.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def length(self):
        count=0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count


    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: ?
    # Space Complexity: ?
    def get_at_index(self, index):
        current=self.head
        count=0
        while current != None:
            if count == index:
                return current.value
            current = current.next
            count += 1
        if index > count +1:
            return None

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: ? O(n)
    # Space Complexity: ? O(1)
    def get_last(self):
        if self.head is None:
            return None
        else:
            current=self.head
            while current.next != None:
                current=current.next
            return current.value
            

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def add_last(self, value):
        new_node=Node(value)
        current=self.head
        if current is None:
            self.head= new_node
        else:
            while current.next != None:
                current=current.next    
            current.next=new_node
        return self.head.value

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        
        if self.head is None:
            return None
        else:
            max_value=0
            current=self.head
            while current.next != None:
                if current.value>max_value:
                    max_value=current.value
                current=current.next
            if current.value>max_value:
                max_value=current.value
            return max_value


    # method to delete the first node found with specified value
    # Time Complexity: ?
    # Space Complexity: ?
    def delete(self, value):
        current = self.head
        if current != None:
            if current.value == value:
                self.head = current.next
                current=None
                return
        while current != None:
            if current.value == value:
                break
            prev = current
            current=current.next
        if current == None:
            return
        prev.next = current.next
        current=None
        

    # method to print all the values in the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: ?
    # Space Complexity: ?
    def reverse(self):
        prev=None
        current=self.head
        while current != None:
            following=current.next
            current.next=prev
            prev = current
            current = following
        self.head = prev
        return
  
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def find_middle_value(self):
        pass

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: ?
    def find_nth_from_end(self, n):
        pass

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
    def has_cycle(self):
        pass

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head == None:
            return

        # navigate to last node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.head # make the last node link to first node
