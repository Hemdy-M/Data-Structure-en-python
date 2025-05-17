# Data Structure : Linked List

class LinkedList:
    def __init__(self, val, **kwargs) -> None:
        self.val = val
        try:
            self.nextVal = kwargs.get("nextp") # `nextp` means `next position`
        except:
            self.nextVal = None
        
        self.values: list = []
    
    def getElements(self, currentVal) -> list:
        try:
            if currentVal.val == None:
                return self.values
        except AttributeError:
            return self.values
        
        self.values.append(currentVal.val)
        self.getElements(currentVal.nextVal)
        return self.values

num2 = LinkedList(5)
num = LinkedList(12, nextp=num2)
print(num.getElements(num))