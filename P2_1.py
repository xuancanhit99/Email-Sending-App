# # 1
# class Soda:
#     def __init__(self, additive=None):
#         # Инициализация класса с добавкой (если она есть)
#         self.additive = additive
#
#     def show_my_drink(self):
#         # Проверяем, есть ли добавка
#         if self.additive:
#             print(f"Газировка и {self.additive}")
#         else:
#             print("Обычная газировка")
#
#
# # Пример использования класса
# soda_with_lemon = Soda("лимон")
# soda_with_lemon.show_my_drink()
#
# plain_soda = Soda()
# plain_soda.show_my_drink()
#
# print("--------------------------------------------------------")

# # 2
# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.sides = [a, b, c]
#
#     def is_triangle(self):
#         if not all(isinstance(side, (int, float)) for side in self.sides):
#             return "Нужно вводить только числа!"
#         if not all(side > 0 for side in self.sides):
#             return "С отрицательными числами ничего не выйдет!"
#         if self.sides[0] + self.sides[1] > self.sides[2] and self.sides[0] + self.sides[2] > self.sides[1] and \
#                 self.sides[1] + self.sides[2] > self.sides[0]:
#             return "Ура, можно построить треугольник!"
#         else:
#             return "Жаль, но из этого треугольник не сделать."
#
#
# # checker = TriangleChecker("a", 4, 5)
# # print(checker.is_triangle())
# # checker = TriangleChecker(-3, 4, 5)
# # print(checker.is_triangle())
# # checker = TriangleChecker(1, 4, 5)
# # print(checker.is_triangle())
# checker = TriangleChecker(3, 4, 5)
# print(checker.is_triangle())  # Outputs: Ура, можно построить треугольник!
# print("--------------------------------------------------------")


# 3
class Raboch:
    cnt = 0

    def __init__(self, name, vozrast):
        self.name = name
        self.vozrast = vozrast
        Raboch.cnt += 1

    @classmethod
    def display_count(cls):
        print(f"Количество рабочих: {cls.cnt}")

    def display_raboch(self):
        print(f"Рабочий: {self.name}, Возраст: {self.vozrast}")


class Deti:
    def __init__(self, name, vozrast):
        self.name = name
        self.vozrast = vozrast

    def school(self):
        return "Школа №1"


raboch1 = Raboch("Иван", 35)
raboch1.display_raboch()
Raboch.display_count()

deti1 = Deti("Маша", 7)
print(f"Ребенок: {deti1.name}, Возраст: {deti1.vozrast}, Школа: {deti1.school()}")
print("--------------------------------------------------------")


class KgToLb:
    def __init__(self, kg):
        self._kg = kg

    @property
    def kg(self):
        return self._kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self._kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

    def to_lb(self):
        return self._kg * 2.205


obj1 = KgToLb(20)
print(obj1.kg)  # Outputs: 20
obj1.kg = 30
print(obj1.kg)  # Outputs: 30
print(obj1.to_lb())  # Outputs: 66.15
