#1
class Matrix():
    def __init__(self, matrix):
        self.value = matrix
    
    def __add__(self, otherMatrix):
        numberRow = len(self.value )
        numberColumn = len(self.value[0])
        result = [[0 for i in range(numberColumn)] for j in range(numberRow)]
        
        for i in range(numberRow):
            for j in range(numberColumn):
                result[i][j] = self.value[i][j] + otherMatrix.value[i][j]
        return Matrix(result)
                
    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.value]))
            
    
m1 = Matrix([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])
m2 = Matrix([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])
m3 = m1 + m2
print(m3)

#2
from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def consumption():
        pass

class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
    
    @property
    def consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height
    
    @property
    def consumption(self):
        return self.height * 2 + 0.3

coat = Coat("Пальто", 5)
suit = Suit("Костюм", 5)
print(f"Материал для пальто: {coat.consumption:0.2f}")
print(f"Материал для костюма: {suit.consumption:0.2f}")

#3
class Cell():
    def __init__(self, quantity):
        self.quantity = quantity
    
    def __add__(self, otherCell):
        return Cell(self.quantity + otherCell.quantity)
    
    def __sub__(self, otherCell):
        return Cell(self.quantity - otherCell.quantity)
    
    def __mul__(self, otherCell):
        return Cell(self.quantity * otherCell.quantity)
    
    def __truediv__(self, otherCell):
        return Cell(round(self.quantity / otherCell.quantity))
    
    def __str__(self):
        return str(self.quantity)
    
    def make_order(self, cellsInRow):
        result = '\n'.join(['*' * self.quantity for _ in range(cellsInRow // self.quantity)])
        
        remainer = cellsInRow % self.quantity
        if remainer > 0:
            result += '\n' + '*' * remainer
            
        return result
            

c1 = Cell(4)
c2 = Cell(2)

print(f"{c1} + {c2} = {c1 + c2}")
print(f"{c1} - {c2} = {c1 - c2}")
print(f"{c1} * {c2} = {c1 * c2}")
print(f"{c1} / {c2} = {c1 / c2}")
print(c1.make_order(13))