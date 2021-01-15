from abc import ABC, abstractmethod


class Engine:
    def __init__(self):
        self.list_of_achievements = {'Вознесшийся': 'Получить 60-й уровень',
                                     'Исследователь': 'Исследовать все локации',
                                     'Хранитель мудрости': 'Выполнить все задания',
                                     'Покоритель подземелий': 'Пройти все подземелья',
                                     'Часть команды': 'Вступить в гильдию',
                                     'Герой': 'Пройти все рейды',
                                     'Победивший тьму': 'Убить самого плохого',
                                     'Спаситель': 'Спасти самого хорошего',
                                     'Вестник судьбы': 'Собрать 10 шкур лысого медведя'}

    def generate_achievement(self, name_of_achievement):
        return self.list_of_achievements[name_of_achievement]


class ObservableEngine(Engine):
    def __init__(self):
        super().__init__()
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self):
        for subscriber in self.__subscribers:
            subscriber.update()


class AbstractObserver(ABC):
    @abstractmethod
    def update(self):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self, name):
        self.achievements = set()
        self.name = name

    def update_achievements(self, name_of_achievement):
        engine = Engine()
        new_achievement = engine.generate_achievement(name_of_achievement)
        self.achievements.add(new_achievement)
        return self.achievements

    def update(self):
        print(f'Игрок под ником {self.name} пополнил свой список достижений! {self.achievements}')


class FullNotificationPrinter(AbstractObserver):
    def __init__(self, name):
        self.achievements = list()
        self.name = name

    def update_achievements(self, name_of_achievement):
        engine = Engine()
        new_achievement = engine.generate_achievement(name_of_achievement)
        self.achievements.append(new_achievement)
        return self.achievements

    def update(self):
        print(f'Игрок под ником {self.name} заработал достижение {self.achievements[0]}')


def main():
    notifier1 = FullNotificationPrinter('Гузен')
    notifier2 = ShortNotificationPrinter('Стролл')
    notifier3 = FullNotificationPrinter('Интмайн')

    notifier1.update_achievements('Вознесшийся')
    notifier2.update_achievements('Исследователь')
    notifier2.update_achievements('Вестник судьбы')
    notifier3.update_achievements('Хранитель мудрости')

    engine = ObservableEngine()
    engine.subscribe(notifier1)
    engine.subscribe(notifier2)
    engine.subscribe(notifier3)

    engine.notify()


if __name__ == '__main__':
    main()
