from abc import ABC, abstractmethod


class Creature(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def move(self):
        pass


class FirstAnimal(Creature):
    def eat(self):
        print('I eat grass')

    def move(self):
        print('I walk slowly')


class AbstractDecorator(Creature):
    def __init__(self, obj):
        self.obj = obj

    def eat(self):
        self.obj.eat()

    def move(self):
        self.obj.move()


class FastAnimal(AbstractDecorator):
    def move(self):
        print('I walk very fast')


if __name__ == '__main__':
    my_first = FirstAnimal()
    my_first.move()
    my_first.eat()

    print()
    
    my_fast = FastAnimal(my_first)
    my_fast.move()
    my_fast.eat()