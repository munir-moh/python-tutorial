class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def get_perimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter
t = Triangle(5,6,7)
perimeter = t.get_perimeter()
print ("The perimeter of t Triangle is is", perimeter)