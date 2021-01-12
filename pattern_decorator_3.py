from abc import ABC, abstractmethod


class Creature(ABC):
    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def make_noise(self):
        pass


class Animal(Creature):
    def feed(self):
        print('I eat grass')

    def move(self):
        print('I walk forward')

    def make_noise(self):
        print('WOOOO!')

    def __str__(self):
        return 'Eto eniaml'


class AbstractDeocrator(Creature):
    def __init__(self, obj):
        self.obj = obj

    def feed(self):
        self.obj.feed()

    def move(self):
        self.obj.move()

    def make_noise(self):
        self.obj.make_noise()


class Swimming(AbstractDeocrator):
    def move(self):
        print('I swim')

    def make_noise(self):
        print('...')


class Predator(AbstractDeocrator):
    def feed(self):
        print('I eat other animals')


class Fast(AbstractDeocrator):
    def move(self):
        self.obj.move()
        print('Fast!')

    def __str__(self):
        return 'ETO FAST ANIMAL, PIZDES'


def main():
    animal = Animal()
    animal.feed()
    animal.move()
    animal.make_noise()

    print()

    swimming = Swimming(animal)
    swimming.feed()
    swimming.move()
    swimming.make_noise()

    print()

    predator = Predator(animal)
    predator.feed()
    predator.move()
    predator.make_noise()

    print()

    fast = Fast(animal)
    fast.feed()
    fast.move()
    fast.make_noise()

    faster = Fast(animal)
    faster.feed()
    faster.move()
    faster.make_noise()

    print()

    print(faster.obj)
    #print(faster.obj.obj)
    #faster.base.base = faster.base.base.base
    #faster.feed()
    #faster.move()
    #faster.make_noise()


def my_main():
    my_animal = Animal()
    my_animal.move()
    my_animal.feed()
    my_animal.make_noise()

    print()

    my_fast = Fast(my_animal)
    my_fast.move()
    my_fast.feed()
    my_fast.make_noise()

    print()

    my_new_fast = Fast(my_fast)
    my_new_fast.move()
    my_new_fast.feed()
    my_new_fast.make_noise()
    print(my_new_fast.obj)
    print(my_new_fast.obj.obj)


if __name__ == '__main__':
    my_main()