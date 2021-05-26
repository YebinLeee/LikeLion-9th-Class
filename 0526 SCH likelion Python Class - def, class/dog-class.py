class Dog:
    def __init__(self, name, age, favorite, weight):
        self.name=name
        self.age=age
        self.favorite=favorite
        self.weight=weight

class Airplane:
    def __init__(self, name, max, speed):
        self.name=name
        self.max=max
        self.speed=speed

tory=Dog("토리", "10", "먹기", "6.1kg")
print(tory.name, tory.age, tory.favorite, tory.weight)

korAirline=Airplane("대한항공", "200명", "400km/h")
usAirline=Airplane("US Air line", "300명", "250km/h")
print(korAirline.name, korAirline.max, korAirline.speed)
print(usAirline.name, usAirline.max, usAirline.speed)