"""
============================================================================
Implementation Exercise: Singly Linked List
============================================================================

-------
Phase 1:
-------
1. Node and LinkedList initialization
2. Getting a node by its position
3. Adding a node to the list's tail
4. Adding a node to list's head
5. Removing the head node
6. Removing the tail node
7. Returning the list length

-------
Phase 2:
-------

1. Check whether the list contains_value a value
2. Inserting a node value into the list at a specific position
3. Updating a list node's value at a specific position
4. Removing a node value from the list at a specific position
5. Format the list as a string whenever `print()` is invoked
"""

# Phase 1

# TODO: Implement a Linked List Node class here
class Node:
  # TODO: Set the `_value` `_next` node instance variables
  def __init__(self, value, next=None):
    self._value = value
    self._next = next


# TODO: Implement a Singly Linked List class here
class LinkedList:
  # TODO: Set the `_head` node, `_tail` node, and list `_length` instance variables
  def __init__(self, head=None, tail=None, length=0):
    self._head = head
    self._tail = tail
    self._length = length

  # TODO: Implement the get_node method here
  def get_node(self, position):
    if self._head:
      current = self._head
      c_pos = 0

      while current:
        if c_pos == position:
          return current
        else:
          current = current._next
          c_pos+=1

  # TODO: Implement the add_to_tail method here
  def add_to_tail(self, value):
    new_node = Node(value)

    if self._head:
      current = self._head
      while current._next:
        current = current._next

      current._next = new_node
    else:
      self._head = new_node

    self._tail = new_node
    self._length+=1

  # TODO: Implement the add_to_head method here
  def add_to_head(self, value):
    new_node = Node(value)
    new_node._next = self._head
    self._head = new_node
    self._length+=1

  # TODO: Implement the remove_head method here
  def remove_head(self):
    if self._head == self._tail:
      self._head = None
      self._tail = None
      self._length = 0
    elif self._head:
      next_node = self._head._next
      self._head = next_node
      self._length-=1

  # TODO: Implement the remove_tail method here
  def remove_tail(self):
    if self._head == self._tail:
      self._head = None
      self._tail = None
      self._length = 0
    elif self._tail:
      current = self._head

      while current._next:
        current = current._next

      current._next = None
      self._tail = current
      self._length-=1

  # TODO: Implement the __len__ method here
  def __len__(self):
    return self._length

# Phase 2

  # TODO: Implement the contains_value method here
  def contains_value(self, target):
    current = self._head

    while current:
      if current._value == target:
        return True
      current = current._next

    return False

  # TODO: Implement the insert_value method here
  def insert_value(self, position, value):
    if position == 0:
      self.add_to_head(value)
      return True

    new_node = Node(value)
    pos = 0
    current = self._head

    while current and pos < position-1:
      current = current._next
      pos+=1

    if pos == position-1:
      temp = current._next
      current._next = new_node
      new_node._next = temp
      self._length+=1
      return True
    else:
      return False

  # TODO: Implement the update_value method here
  def update_value(self, position, value):
    node = self.get_node(position)

    if node:
      node._value = value
      return True
    else:
      return False

  # TODO: Implement the remove_node method here
  def remove_node(self, position):
    if position == 0:
      self.remove_head()
      return True

    prev_node = self.get_node(position-1)

    if prev_node._next == self._tail:
      self.remove_tail()
      return True

    try:
      temp = prev_node._next._next
      prev_node._next = temp
      self._length-=1
      return True
    except:
      return False


  # TODO: Implement the __str__ method here
  def __str__(self):
    if self._head:
      string = f'{self._head._value}'
      current = self._head._next

      while current:
        string += f', {current._value}'
        current = current._next

      return string
    else:
      return 'Empty List'

# Phase 1 Manual Testing:

# 1. Test Node and LinkedList initialization
#node = Node('hello')
#print(node)                                     # <__main__.Node object at ...>
#print(node._value)                              # hello
#linked_list = LinkedList()
#print(linked_list)                              # <__main__.LinkedList object at ...>

# # 2. Test getting a node by its position
#print(linked_list.get_node(0))                # None

# # 3. Test adding a node to the list's tail
#linked_list.add_to_tail('new tail node')
#print(linked_list.get_node(0))                # <__main__.Node object at ...>
#print(linked_list.get_node(0)._value)         # `new tail node`

# # 4. Test adding a node to list's head
#linked_list.add_to_head('new head node')
#print(linked_list.get_node(0))                # <__main__.Node object at ...>
#print(linked_list.get_node(0)._value)         # `new head node`

# # 5. Test removing the head node
#linked_list.remove_head()
#print(linked_list.get_node(0)._value)         # `new tail node` because `new head node` has been removed
#print(linked_list.get_node(1))                # `None` because `new head node` has been removed

# # 6. Test removing the tail node
#print(linked_list.get_node(0)._value)         # `new tail node`
#linked_list.remove_tail()
#print(linked_list.get_node(0))                # None

# # 7. Test returning the list length
#print(len(linked_list))                                 # 2

# Phase 2 Manual Testing

# # 1. Test whether the list contains_value a value
#linked_list = LinkedList()
#linked_list.add_to_head('new head node')
#print(linked_list.contains_value('new head node'))      # True
#print(linked_list.contains_value('App Academy node'))   # False

# # 2. Test inserting a node value into the list at a specific position
#linked_list.insert_value(0, 'hello!')
#print(linked_list.get_node(0)._value)                   # `hello!`

# # 3. Test updating a list node's value at a specific position
#linked_list.update_value(0, 'goodbye!')
#print(linked_list.get_node(0)._value)                   # `goodbye!`

# # 4. Test removing a node value from the list at a specific position
#print(linked_list.get_node(1)._value)                   # `new head node`
#linked_list.remove_node(1)
#print(linked_list.get_node(1))                          # None

# # 5. Format the list as a string whenever `print()` is invoked
#new_linked_list = LinkedList()
#print(new_linked_list)                  # Empty List
#new_linked_list.add_to_tail('puppies')
#print(new_linked_list)                  # puppies
#new_linked_list.add_to_tail('kittens')
#print(new_linked_list)                  # puppies, kittens

#test = LinkedList()
#test.add_to_head(1)
#test.add_to_head(2)
#test.add_to_head(3)
#test.add_to_head(4)
#test.add_to_head(5)
#print(test)
#test.insert_value(4, 13)
#test.remove_node(5)
#print(test)
