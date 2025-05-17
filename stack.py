# Data structure : Stack (FILO : First In Last Out)

class Stack:
    def __init__(self):
        self.__values: list = []
        self.__the_last_entered_value = None
    
    # Add an element at the top of the stack
    def push(self, val):
        self.__values.append(val)
        self.__the_last_entered_value = val
    
    # Remove the element at the top of the stack
    def pop(self):
        val = self.__the_last_entered_value
        self.__the_last_entered_value = self.__values[len(self.__values)-2]
        self.__values.remove(self.__the_last_entered_value)
        return val # the return is here to not discard the `popped` value if we need to use it

stack = Stack()
stack.push(12)
stack.push(3)
print(stack.pop()) # 3
print(stack.pop()) # 12