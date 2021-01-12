from abc import ABC, abstractmethod


class Creature(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Animal(Creature):
    def move(self):
        print('I walk slowly')

    def eat(self):
        print('I eat grass')


class AbstractDecorator(Creature):
    def __init__(self, obj):
        self.obj = obj

    def move(self):
        self.obj.move()

    def eat(self):
        self.obj.eat()


class FastAnimal(AbstractDecorator):
    def move(self):
        print('I walk fast')


def main():
    new_animal = Animal()
    new_animal.move()
    new_animal.eat()

    print()

    new_fast_animal = FastAnimal(new_animal)
    new_fast_animal.move()
    new_fast_animal.eat()


if __name__ == '__main__':
    main()