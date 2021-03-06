"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""
# Решение Задачи №1

from abc import ABCMeta, abstractmethod
from collections import namedtuple

Enterprise = namedtuple('Enterprise', 'name quarter_1 quarter_2 quarter_3 quarter_4 year')

enterprise_count = int(input('Введите количество предприятий для анализа: '))
enterprises = [0 for _ in range(enterprise_count)]
profit_sum = 0

class BasicFeature(metaclass=ABCMeta):

    @abstractmethod
    def get_avg(self):
        pass

for i in range(enterprise_count):
    name = input(f'Введите название {i + 1}-го предприятия: ')
    quarters = [float(j) for j in input('Введите через пробел прибыль в каждом квартале: ').split()]

    year = 0
    for quarter in quarters:
        year += quarter

    profit_sum += year
    enterprises[i] = Enterprise(name, *quarters, year)
    # print(enterprises[i])

if enterprise_count == 1:
    print(f'Для анализа передано 1 предприятие: {enterprises[0].name}. Eго годовая прибыль: {enterprises[0].year}')

else:
    profit_average = profit_sum / enterprise_count

    less = []
    more = []

    for i in range(enterprise_count):

        if enterprises[i].year < profit_average:
            less.append(enterprises[i])

        elif enterprises[i].year > profit_average:
            more.append(enterprises[i])

    print(f'\nСредняя годовая прибыль по предприятиям: {profit_average: .2f}')

    print(f'Предприятия, чья прибыль меньше {profit_average: .2f}:')
    for ent in less:
        print(f'Предприятие "{ent.name}" с прибылью {ent.year: .2f}')

    print(f'\nПредприятия, чья прибыль больше {profit_average: .2f}:')
    for ent in more:
        print(f'Предприятие "{ent.name}" с прибылью {ent.year: .2f}')
