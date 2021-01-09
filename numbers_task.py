class MyContainer:
    def __init__(self, my_list):
        if MyContainer.check_for_validation(my_list):
            self.container = my_list or []
        else:
            raise ValueError

    @staticmethod
    def check_for_validation_for_list(my_list):
        counter = 0
        flag = True
        for elem in my_list:
            if MyContainer.check_for_validation_for_elem(elem):
                counter += 1
        if counter == len(my_list):
            flag = True
        else:
            flag = False
        return flag

    @staticmethod
    def check_for_validation_for_elem(elem):
        if isinstance(elem, int) and elem >= 0 and elem % 2 != 0:
            return True
        else:
            return False

    @staticmethod
    def check_for_validation(thing):
        if isinstance(thing, list):
            if MyContainer.check_for_validation_for_list(thing):
                return True
            else:
                return False
        else:
            if MyContainer.check_for_validation_for_elem(thing):
                return True
            else:
                return False

    def __setitem__(self, key, value):
        if key >= len(self.container):
            raise KeyError

        if MyContainer.check_for_validation_for_elem(value):
            self.container[key - 1] = value

        else:
            raise ValueError

    def __getitem__(self, index):
        return self.container[index - 1]

    def __len__(self):
        return len(self.container)

    def __str__(self):
        return f"{self.container}"


def main():
    my_container = MyContainer([1, 1, 3, 1, 3, 7, 7, 9, 5, 13, 11])
    print(my_container)
    print(f"Длина списка равна {len(my_container)}")
    print(my_container[11])
    my_container[10] = 2
    #for i in my_container:
     #   print(i)


if __name__ == '__main__':
    main()