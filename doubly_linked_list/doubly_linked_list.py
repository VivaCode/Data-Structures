"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
      new_node = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    

  def remove_from_head(self):
    if self.head is None:
        return None
    elif self.head is self.tail:
        return_val = self.head.value
        self.head = None
        self.tail = None
        return return_val
    else:
        self.head = self.head.next
        self.head.prev = None

  def add_to_tail(self, value):
    new_tail = ListNode(value)
    if not self.head and not self.tail:
        self.head = new_tail
        self.tail = new_tail
    else:
        new_tail.prev = self.tail
        self.tail.next = new_tail
        sel.tail = new_tail

  def remove_from_tail(self):
    if not self.tail:
        return None
    elif self.tail is self.head:
        return_val = self.tail.value
        self.tail = None
        self.head = None
    else:
        return_val = self.tail.value
        self.tail = self.tail.prev
        self.tail.next = None
        return return_val

  def move_to_front(self, node):
    if self.head is None:
        return None
    elif node.prev is None:
        return None
    else:
        #make surrounding nodes point to each other
        prev_node = node.prev
        next_node = node.next
        prev_node = next_node

        node.next = self.head
        self.head.prev = node
        self.head = node


  def move_to_end(self, node):
    pass

  def delete(self, node):
    if self.head is self.tail:
        self.head = None
        self.tail = None 
    elif node is self.head:
        self.head = self.head.next
        self.head.prev = None
    elif node is self.tail:
        self.tail = self.tail.prev
        self.tail.next = None
    else:
        node.prev.next = node.next
        node.next.prev = node.prev
    
  def get_max(self):
    pass