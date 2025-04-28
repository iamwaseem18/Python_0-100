class vector:
    def __init__(self,x,y,z):
        self.x = 7
        self.y = 8
        self.z = 10


    def __add__(self,other):
        result = vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self,other):
        result = self.x * other.x + self.y * other.y + self.z + other.z
        return result
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
v1 = vector(7,8,10)
print(v1)