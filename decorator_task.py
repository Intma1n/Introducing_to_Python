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


class AbstractEffect(Hero, ABC):
    def __init__(self, base):
        super().__init__()
        self.base = base

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    @abstractmethod
    def get_stats(self):
        pass

    def get_negative_effects(self):
        return self.base.get_negative_effects()


class AbstractPositive(AbstractEffect):
    def get_positive_effects(self):
        self.base.get_positive_effects()


class AbstractNegative(AbstractEffect):
    def get_negative_effects(self):
        self.base.get_negative_effects()


class Berserk(AbstractPositive):
    def get_positive_effects(self):
        effects = self.positive_effects
        effects.append('Berserk')
        return effects

    def get_stats(self):
        my_stats = self.base.get_stats()
        raising_stats = ["Strength", 'Endurance', 'Agility', 'Luck']
        for stat in raising_stats:
            my_stats[stat] += 7

        decline_stats = ['Perception', 'Charisma', 'Intelligence']
        for stat in decline_stats:
            my_stats[stat] -= 3

        my_stats['HP'] += 50

        return my_stats


class Blessing(AbstractPositive):
    def get_positive_effects(self):
        effects = self.positive_effects
        effects.append('Blessing')
        return effects

    def get_stats(self):
        my_stats = self.base.get_stats()
        raising_stats = list(my_stats.keys)
        for stat in raising_stats:
            my_stats[stat] += 2
        return my_stats


class Weakness(AbstractNegative):
    def get_negative_effects(self):
        effects = self.positive_effects
        effects.append('Weakness')
        return effects

    def get_stats(self):
        my_stats = self.base.get_stats()
        decline_stats = ['Strength', 'Endurance', 'Agility']
        for stat in decline_stats:
            my_stats[stat] -= 4
        return my_stats


class EvilEye(AbstractNegative):
    def get_negative_effects(self):
        effects = self.positive_effects
        effects.append('EvilEye')
        return effects

    def get_stats(self):
        my_stats = self.base.get_stats()
        decline_stats = ['Luck']
        for stat in decline_stats:
            my_stats[stat] -= 10
        return my_stats


class Curse(AbstractNegative):
    def get_negative_effects(self):
        effects = self.positive_effects
        effects.append('Curse')
        return effects

    def get_stats(self):
        my_stats = self.base.get_stats()
        raising_stats = list(my_stats.keys())
        for stat in raising_stats:
            my_stats[stat] -= 2
        return my_stats


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

    print()

    brs2 = Berserk(brs1)

    cur1 = Curse(brs2)
    print(cur1.get_stats())
    print(cur1.get_positive_effects())
    print(cur1.get_negative_effects())


if __name__ == '__main__':
    main()