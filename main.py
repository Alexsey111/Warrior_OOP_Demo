class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f'{self.name} лег спать')
        self.endurance += 2

    def eat(self):
        print(f'{self.name} сел есть')
        self.power += 1

    def hit(self):
        print(f'{self.name} ведет бой')
        self.endurance -= 6

    def walk(self):
        print(f'{self.name} гуляет')

    def info(self):
        print(f'Имя война {self.name}')
        print(f'Сила война {self.power}')
        print(f'Выносливость война {self.endurance}')
        print(f'Цвет волос война {self.hair_color}')

war1 = Warrior('Павел', 76, 54, 'красный')
war2 = Warrior('Егор', 64, 72, 'белый')

war1.sleep()
war1.eat()
war1.walk()
war1.hit()
war1.info()

war2.sleep()
war2.eat()
war2.walk()
war2.hit()
war2.info()