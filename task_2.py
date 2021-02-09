'''2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и
костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
Sergey Romanov, [08.02.21 22:33]
Типа есть общее понятие одежда, а есть довольно конкретные понятия - куртки, джинсы, майки, трусы. Есть уже конкретные объекты - куртка Boss, джинсы Lacoste Ultra Fashion 2.0 и так далее
общее понятие - одежда - абсктрактный класс. Джинсы - дочерний класс (от абстракта). Джинсы лакост ультра фешн 2 0 - объект или экземпляр класса Джинсы

'''

from abc import ABC, abstractmethod


class Clothes(ABC):
    full_cloth = 0

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.cloth = 0

    def full_clothes(self):
        return f'общий расход ткани = {Clothes.full_cloth}'

    @abstractmethod
    def cloth_calculator(self):
        pass


class Coat(Clothes):
    """пальто"""

    def cloth_calculator(self):
        self.cloth = round(self.size / 6.5 + 0.5, 2)  # V/6.5 + 0.5
        Clothes.full_cloth += self.cloth
        return f'пальто {self.name} размер {self.size} расход ткани = {self.cloth} '

    @property
    def product_size(self):
        return f'размер пальто {self.name} {self.size}'

    @product_size.setter
    def product_size(self, new_size):
        Clothes.full_cloth -= self.cloth
        self.size = new_size


class Costume(Clothes):
    """костюм"""

    def cloth_calculator(self):
        self.cloth = round(2 * self.size * 0.01 + 0.3, 2)  # (2 * H + 0.3) эта формула сьела много ткани!!! поменял!!!
        Clothes.full_cloth += self.cloth
        return f'костюм {self.name} размер {self.size} расход ткани = {self.cloth} '

    @property
    def product_size(self):
        return f'размер костюма {self.name} {self.size}'

    @product_size.setter
    def product_size(self, new_size):
        Clothes.full_cloth -= self.cloth
        self.size = new_size


a = Coat('Armany', 5)
print(a.cloth_calculator())
a.product_size = 8
print(a.cloth_calculator())
print(a.full_clothes())

b = Costume('Briony', 170)
print(b.cloth_calculator())
print(a.full_clothes())



