import re
from abc import ABC, abstractmethod


class System:
    def __init__(self, text):
        tmp = re.sub(r'\W', ' ', text.lower())
        tmp = re.sub(r' +', ' ', tmp).strip()
        self.text = tmp

    def get_processed_text(self, processor):
        result = processor.process_text(self.text)
        print(*result, sep = '\n')


class TextProcessor:
    @abstractmethod
    def process_text(self, text):
        pass


class WordCounter:
    def count_words(self, text):
        self.__words = dict()
        for word in text.split():
            self.__words[word] = self.__words.get(word, 0) + 1

    def get_count(self, word):
        return self.__words.get(word, 0)

    def get_all_words(self):
        return self.__words.copy()


class WordCounterAdapter(TextProcessor):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def process_text(self, text):
        self.adaptee.count_words(text)
        words = self.adaptee.get_all_words().keys()
        return sorted(words,
                      key=lambda
                          x:self.adaptee.get_count(x),
                      reverse=True)


def main():
    text = 'Summer is miles and miles away and no one would ask me to stay'
    system = System(text)
    system.text
    counter = WordCounter()
    adapter = WordCounterAdapter(counter)
    system.get_processed_text(adapter)


if __name__ == '__main__':
    main()