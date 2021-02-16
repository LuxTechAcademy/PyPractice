class Stack:
	def __init__(self):
		self.items =[]

	def push(self, item):
		self.items.append(item)
		return self 


stack = Stack()

stack.push(2)
stack.push(3) 

print(stack.items)



		