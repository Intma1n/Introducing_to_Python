import requests
import collections
from pprint import pprint

TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'


def sort_by_first_key(res_list_counter):
    return res_list_counter[0]


def sort_by_second_key(res_list_counter):
    return res_list_counter[1]


def check_validation_bdate(date_of_birth):
    """

    :param date_of_birth:
    :return: Тру если дата норм, Фолс, если нет
    """
    flag = True
    str(date_of_birth)
    splitted_date_of_birth = date_of_birth.split('.')
    if len(splitted_date_of_birth) == 2:
        flag = False
    return flag


def calc_age(uid):
    """

    :param uid:
    :return Отсортированный список, в котором каждый эемент - кортеж из возраста и частоты его повторения:
    """
    my_id = f'https://api.vk.com/method/users.get?v=5.71&access_token={TOKEN}&user_ids={uid}'
    my_friends = f'https://api.vk.com/method/friends.get?v=5.71&access_token={TOKEN}&user_id={uid}&fields=bdate'
    response_my_id = requests.get(my_id)
    my_html_id = response_my_id.json()
    response_my_friends = requests.get(my_friends)
    my_json_friends = response_my_friends.json()
    res_list = []
    for i in range(47):
        age = 0
        count = 0
        try:
            bdate_for_one = my_json_friends['response']['items'][i]['bdate']
            if not check_validation_bdate(bdate_for_one):
                raise KeyError

            splitted_bdate_for_one = str(bdate_for_one).split('.')
            age = 2021 - int(splitted_bdate_for_one[2])
            res_list.append(age)

            # При анализе ответа, полученного методом friends.get, можно заметить,
            # что bdate есть не у всех пользователей и у некоторых в bdate отсутствует год рождения.
            # Поэтому необходимо пропускать этот случай.
            # Примеры возможных значений: "bdate":"6.6", "bdate":"25.8.1993".
            # Для вычисления возраста, необходимо взять текущий год ,
            # и вычесть из него год рождения пользователя, полученный из API (без учета месяца и числа).

        except KeyError:
            continue

    res_list_counter = collections.Counter()
    for age in res_list:
        res_list_counter[age] += 1

    res_list_counter = res_list_counter.most_common(len(res_list_counter))

    res_list_counter.sort(key=sort_by_first_key)
    res_list_counter.sort(key=sort_by_second_key)

    return res_list_counter


def main():
    user_id = '254989146'
    res = calc_age(user_id)
    print(res)


if __name__ == '__main__':
    main()
