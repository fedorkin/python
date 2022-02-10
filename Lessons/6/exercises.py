#1
import time
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = {"red":7, "yellow":2, "green":5}
        
    def running(self):
        for c, t in cycle(self.__color.items()):
            print(c)
            time.sleep(t)
    
tl = TrafficLight()
tl.running()

#2
class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width
    
    def get_asphalt_mass_kg(self, kg_per_metter, thickness):
        return self._width * self._length * kg_per_metter * thickness
road = Road(5000, 20)
needTon = road.get_asphalt_mass_kg(25, 5)
print(f'{needTon} kg of asphalt need for building the road')

#3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage":wage, "bonus":bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'
    
    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

p = Position("Pavel", "Fedorov", "CEO", 1000000, 2000000)
print(p.get_full_name())
print(p.get_total_income())

#4
class Car():
    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print("The car went")
    
    def stop(self):
        print("The car stoped")
    
    def turn(self, direction):
        print(f"The car turned to {direction}")

    def show_speed(self):
        print(self.speed)
        
    def __str__(self):
        return f"Name:{self.name}, Speed:{self.speed}, Color:{self.color}, Is police:{self.is_police}"
        
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60 :
            print("The speed of the car is exceed")
        else:
            super().show_speed()
        

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40 :
            print("The speed of the car is exceed")
        else:
            super().show_speed()
            
class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

cars = [TownCar("TowCar", 50, "green"), TownCar("TowCar1", 80, "blue"), WorkCar("WorkCar", 50, "yellow"), PoliceCar("PoliceCar", 100, "red", True)]

print([str(c) for c in cars])
[c.show_speed() for c in cars]

#5
class Stationery():
    def __init__(self, title):
        self.title = title
    
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f"Title:{self.title}. Рисуем ручкой")
        
        
class Pencil(Stationery):
    def draw(self):
        print(f"Title:{self.title}. Рисуем карандашем")
        
        
class Handle(Stationery):
    def draw(self):
        print(f"Title:{self.title}. Рисуем маркером")
        
stationeries = [Pen("1"), Pen("2"), Pencil("3"), Handle("4")]
[s.draw() for s in stationeries]


        
        
        
        
        
        
        
        
