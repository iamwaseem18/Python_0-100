class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y


    def __add__(self,other):
        result = vector(self.x + other.x, self.y + other.y)
        return result

    def __mul__(self,other):
        result = self.x * other.x + self.y * other.y
        return result
    
    def __str__(self):
        return f"Vector({self.x},{self.y})"
    

#Implementation
v1 = vector(1,2)
v2 = vector(3,4)

print(v1+v2)
print (v1*v2)