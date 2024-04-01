class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f'{self.name} летает')

    def eat(self):
        print(f'{self.name} ест')

    def sing(self):
        print(f'{self.name} поет - {self.voice}')

    def info(self):
        print(f'{self.name} - название')
        print(f'{self.voice} - голос')
        print(f'{self.color} - окрас')

class Pidgeon(Bird):
    def __init__(self, name, voice, color, favourite_food):
        super().__init__(name, voice, color)
        self.favourite_food = favourite_food

    def sing(self):
        print(f'{self.name} поет - Курлык Курлык')

    def walk(self):
        print(f'{self.name} ходит')


bird1 = Pidgeon('Гоша', 'Курлык', 'Белый', 'хлебные крошки')

bird1.sing()
bird1.info()
bird1.walk()