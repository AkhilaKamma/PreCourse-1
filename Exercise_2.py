#Time Complexity :
#pop: O(1)
#Push: O(1)
#Space Complexity: O(n) to store n nodes 

class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Stack:
    def __init__(self):
      self.top = None #This is because initially the stack is empty
        
    def push(self, data):
      new_node = Node(data)
      new_node.next = self.top  # New node points to current top
      self.top = new_node       # New node becomes the new top
        
    def pop(self):
      if self.top is None:
            return "Stack is empty cannot pop."
      popped_value = self.top.data
      self.top = self.top.next  # Move top to the next node
      return popped_value

        
a_stack = Stack()
while True:
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    operation = do[0].strip().lower()
    if operation == 'push':
        a_stack.push(int(do[1]))
    elif operation == 'pop':
        popped = a_stack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == 'quit':
        break
