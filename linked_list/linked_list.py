"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next
  
  def __repr__(self):
    return f"{self.value}"

  def __str__(self):
    return f"{self.value}"

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    new_node = Node(value)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      curr_node = self.tail
      curr_node.set_next(new_node)
      self.tail = new_node
      

  def remove_head(self):
    if self.head == None:
      return self.head
    elif self.head is self.tail:
      node = self.head
      self.head = node.get_next()
      self.tail = node.get_next()
      return node.get_value()
    else:
      node = self.head
      self.head = node.get_next()
      return node.get_value()

  def contains(self, value):
    if self.head == None:
      return False
    else:
      node = self.head
      while(True):
        if node.get_value() == value:
          return True
        if  node.get_next() == None:
          break
        node = node.get_next()
      
      return False

  def get_max(self):
    max = 0
    if self.head == None:
      return None
    else:
      node = self.head
      while(True):
        if node.get_value() > max:
          max = node.get_value()
        if node.get_next() == None:
          break
        node = node.get_next()

    return max


    
