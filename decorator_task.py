from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects =[]
        self.negative_effects = []
        self.stats = {
            "HP": 128, #health points
            "MP": 42, #magic points
            "SP": 100, #skill points
            "Strength": 15, #сила
            "Perception": 4, #восприятие
            "Endurance": 8, #выносливость
            "Charisma": 2, #харизма
            "Intelligence": 3, #ителлект
            "Agility": 8, #ловкость
            "Luck": 1 #удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(Hero):
    def __init__(self, base):
        super().__init__()
        self.base = base

    def get_positive_effects(self):
        self.base.positive_effects.copy()

    def get_stats(self):
        self.base.stats.copy()

    def get_negative_effects(self):
        self.base.negative_effects.copy()


class AbstractPositive(AbstractEffect):
    def get_positive_effects(self):
        self.base.get_positive_effects()

    def get_stats(self):
        self.base.get_stats()


class AbstractNegative(AbstractEffect):
    def get_positive_effects(self):
        self.base.get_positive_effects()

    def get_stats(self):
        self.base.get_stats()


class Berserk(AbstractPositive):
    def get_positive_effects(self):
        self.positive_effects.append('Berserk')

    def get_stats(self):
        pass


class Blessing(AbstractPositive):
    def get_positive_effects(self):
        self.positive_effects.append('Blessing')

    def get_stats(self):
        pass


class Weakness(AbstractNegative):
    def get_negative_effects(self):
        self.positive_effects.append('Weakness')

    def get_stats(self):
        pass


class EvilEye(AbstractNegative):
    def get_negative_effects(self):
        self.positive_effects.append('EvilEye')

    def get_stats(self):
        pass


class Curse(AbstractNegative):
    def get_negative_effects(self):
        self.positive_effects.append('Curse')

    def get_stats(self):
        pass


def main():
    hero = Hero()
    print(hero.get_stats())
    print(hero.stats)
    print(hero.get_negative_effects())
    print(hero.get_positive_effects())

    print()

    brs1 = Berserk(hero)
    print(brs1.get_stats())
    print(brs1.get_negative_effects())
    print(brs1.get_positive_effects())


if __name__ == '__main__':
    main()