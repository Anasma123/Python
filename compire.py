class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def __lt__(self,other):
        if self.area()<other.area():
            return True
        else:
            return False
        
    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def area(self):
        return self.length * self.width



length1 = float(input("Enter the length of Rectangle 1: "))
width1 = float(input("Enter the width of Rectangle 1: "))
length2 = float(input("Enter the length of Rectangle 2: "))
width2 = float(input("Enter the width of Rectangle 2: "))

rect1 = Rectangle(length1, width1)
rect2 = Rectangle(length2, width2)

if rect1< rect2:
    print("Rectangle 1 has a smaller area than Rectangle 2.")
else:
    print("Rectangle 1 has a larger or equal area to Rectangle 2.")
