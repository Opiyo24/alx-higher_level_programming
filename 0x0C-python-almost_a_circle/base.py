# Base for a pyton object with init, attrubutes and methods
class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
    
    def display_attributes(self):
        print(f"Attribute 1: {self.attribute1}")
        print(f"Attribute 2: {self.attribute2}")
    
    def calculate_sum(self):
        return self.attribute1 + self.attribute2

#usage:
obj = MyClass(10, 20) # Creating an instance of myclass
obj.display_attributes()
result = obj.calculate_sum()
print(f"Sum of attributes: {result}")
