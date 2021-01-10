from re import findall
from contracts import contract, new_contract


@new_contract
def is_str_empty(my_string):
    if len(my_string) == 0:
        error_message = 'Введи, что-то долбаеб'
        raise ValueError(error_message)


@contract(returns='str,is_str_empty')
def get_user_equation():
    user_task = input('Input your equation ')
    return user_task


@contract(returns='tuple')
def get_kind_of_solving():
    my_equation = get_user_equation()
    my_kind = input('Укажите метод решения: (1 - Теорема Виетта, 2 - Дискриминант) ')
    if my_kind == '1':
        my_solving = SolvingQuadraticEquation(my_equation)
        my_res = my_solving.solving_by_viett()
    elif my_kind == '2':
        my_solving = SolvingQuadraticEquation(my_equation)
        my_res = my_solving.solving_by_discriminant()
    else:
        raise ValueError("Ты кто такой, чтобы это делать?")
    return my_res


class SolvingQuadraticEquation:
    def __init__(self, user_equation):
        self.user_equation = user_equation

    def get_coeff(self):
        user_task = '5 4 3'
        return findall('\d+', self.user_equation)

    def solving_by_discriminant(self):
        user_coeff = SolvingQuadraticEquation.get_coeff(self)
        a = int(user_coeff[0])
        b = int(user_coeff[1])
        c = int(user_coeff[2])
        d = (b * b) - (4 * a * c)
        if (d ** 1 / 2) % 1 != 0:
            ValueError("No solutions!")
        x1 = (-b - d ** 1 / 2) // (2 * a)
        x2 = (-b + d ** 1 / 2) // (2 * a)
        res = (x1, x2)
        return res

    def solving_by_viett(self):
        user_coeff = SolvingQuadraticEquation.get_coeff(self)
        a = int(user_coeff[0])
        b = int(user_coeff[1])
        c = int(user_coeff[2])
        D = (b ** 2 - 4 * a * c) ** 0.5
        x1 = x2 = 0
        points = [i for i in range(-100, 100)]
        if D >= 0:
            for i in points:
                x1 = i
                for j in points:
                    x2 = j
                    if x1 + x2 == -b / a and x1 * x2 == c / a:
                        res = (x1, x2)
                        return res
        if D < 0:
            return ValueError("No solutions!")


def main():
    my_solving = get_kind_of_solving()
    print(my_solving)


if __name__ == '__main__':
    main()