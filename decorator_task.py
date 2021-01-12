from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.positive_effects = []
        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,
            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        }

    def get_positive_effects(self):
        return self.positive_effets.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(Hero):
    def get_positive_effects(self):
        pass

    def get_negative_effects(self):
        pass


class AbstractNegative(AbstractEffect):
    def __init__(self,effect):
        self.effect = effect

    def get_negative_effects(self):
        pass


class AbstractPositive(AbstractEffect):
    def __init__(self, effect):
        self.effect = effect

    def get_positive_effects(self):
        pass


class Berserk(AbstractPositive):
    pass


class Blessing(AbstractPositive):
    pass


class Weakness(AbstractNegative):
    pass


class EvilEye(AbstractNegative):
    pass


class Curse(AbstractNegative):
    pass

