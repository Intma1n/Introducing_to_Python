def get_input():
    user_n = int(input('Номер крайнего элемента ряда Фибоначчи: '))
    return user_n


def fibonacci_cycle_method(n):
    fib1 = 1
    fib2 = 1
    i = 0
    fib_list = []
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
        fib_list.append(fib2)
    return fib_list


def fibonacci_recursion_method(n):
    fib_list = []
    if n in (1, 2):
        return 1
    fib_elem = fibonacci_recursion_method(n - 1) + fibonacci_recursion_method(n - 2)
    fib_list.append(fib_elem)
    return fib_elem


def main():
    my_n = get_input()
    my_fibonacci_cycle_method = fibonacci_cycle_method(my_n)
    my_fibonacci_recursion_method = fibonacci_recursion_method(my_n)
    print(f'Третьего дня циклическим методом были выявлены следующие числа Фибоначчи: {my_fibonacci_cycle_method}')
    print('---------------------------------------------------')
    print(f'Разведка доложила, что был выбран рекурсивный метод. Оказывается, числа Фибоначии равны: {my_fibonacci_recursion_method}')


if __name__ == '__main__':
    main()