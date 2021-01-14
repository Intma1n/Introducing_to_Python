from abc import ABC, abstractmethod


class NotifyManager:
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass


class MessageNotifier(AbstractObserver):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'Уебище {self.name} идет в {message}')


def main():
    notifier_1 = MessageNotifier('Константин Розизнаный')
    notifier_2 = MessageNotifier('Алексей Колесник')

    manager = NotifyManager()
    manager.subscribe(notifier_1)
    manager.subscribe(notifier_2)

    manager.notify('Пизду')


if __name__ == '__main__':
    main()