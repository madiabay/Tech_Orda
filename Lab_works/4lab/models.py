from dataclasses import dataclass

@dataclass
class Person:
    first_name: str
    last_name: str
    __age: int

    def __post_init__(self):
        self.full_name = f'{self.first_name} {self.last_name}'
    
    def __str__(self) -> str:
        return f'full name: {self.full_name}, age: {self.__age}' 

@dataclass
class Driver(Person):
    experience: int

    def __str__(self) -> str:
        return super().__str__() + f', experience: {self.experience}'

@dataclass
class Engine: # двигатель, мотор
    power: int
    company: str

    def __str__(self) -> str:
        return f'power: {self.power}, company: {self.company}'

@dataclass
class Car(Driver, Engine):
    marka: str
    carClass: str
    weight: int

    def __init__(self, first_name: str, last_name: str, age: int, experience: int, power: int, company: str, marka: str, carClass: str, weight: int):
        Driver.__init__(self, first_name, last_name, age, experience)
        Engine.__init__(self, power, company)
        self.marka = marka
        self.carClass = carClass
        self.weight = weight
    
    def start(self):
        print('Here goes!!!')

    def stop(self):
        print('Stop!!!')

    def turnRight(self):
        print('Turn Right!!!')

    def turnLeft(self):
        print('Turn Left!!!')
    

    def __str__(self) -> str:
        car_info = f'marka: {self.marka}, carClass: {self.carClass}, weight: {self.weight}'
        return Driver.__str__(self) + '\n' + Engine.__str__(self) + '\n' + car_info

@dataclass
class Lorry(Car):
    carrying: int

    def __str__(self) -> str:
        return super().__str__() + f', carrying: {self.carrying}'

@dataclass
class SportCar(Car):
    speed: int

    def __str__(self) -> str:
        return super().__str__() + f', carrying: {self.speed}'




# a = Person('Aibek', 'Almabekuly', 21)
# print(a)
# b = Driver('Aibek', 'Almabekuly', 21, 5)
# print(b)
# c = Engine(25000, 'AMG')
# print(c)
# d = Car('Aibek', 'Almabekuly', 21, 5, 25000, 'AMG', 'BWB', 'B', 1600)
# print(d)
# e = Lorry(25000, 'AMG', 'Aibek', 'Almabekuly', 21, 5, 'bwb', 'b', 1600, 500)
# print(e)
# f = SportCar(25000, 'AMG', 'Aibek', 'Almabekuly', 21, 5, 'mers', 'a', 1000, 300)
# print(f)