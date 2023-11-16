from enum import Enum


class PizzaType(Enum):
    '''
    Перечисление текущих рецептов пицц в пиццерии,
    которые можно приготовить
    '''
    MARGARITA = 'MARGARITA',
    PEPPERONI = 'PEPPERONI',
    HAWAIIAN = 'HAWAIIAN'


class PizzaSize(Enum):
    '''
    Перечисление текущих размеров пицц в пиццерии,
    которые можно приготовить
    '''
    L = 'L',
    XL = 'XL'


class Pizza:
    '''
    Базовый класс для пицц, которые можно
    приготовить в пиццерии
    '''

    def __init__(self, size: PizzaSize, name: str, symbol: str,
                 ingridients: list[str]):
        self.__size = size
        self.__name = name
        self.__emoj = symbol
        self.__ingridients = ingridients

    def dict(self) -> dict:
        recipe = {'name': self.__name, 'ingridients': self.__ingridients}
        return recipe

    def __eq__(self, other) -> bool:
        if not isinstance(other, Pizza):
            return False
        if self.__size != other.get_size():
            return False
        if self.__name != other.get_name():
            return False
        if self.__ingridients != other.get_ingridients():
            return False
        return True

    def __str__(self):
        return f'{self.__name} {self.__emoj} : {", ".join(self.__ingridients)}'

    def get_size(self):
        return self.__size

    def get_name(self):
        return self.__name

    def get_ingridients(self):
        return self.__ingridients


class PizzaMargarita(Pizza):
    def __init__(self, size: PizzaSize = PizzaSize.L):
        super().__init__(size, 'Margarita', '🧀', [
            'tomato sauce', 'mozzarella', 'tomatoes'])


class PizzaPepperoni(Pizza):
    def __init__(self, size: PizzaSize = PizzaSize.L):
        super().__init__(size, 'Pepperoni', '🍕', [
            'tomato sauce', 'mozzarella', 'pepperoni'])


class PizzaHawaiian(Pizza):
    def __init__(self, size: PizzaSize = PizzaSize.L):
        super().__init__(size, 'Hawaiian', '🍍', [
            'tomato sauce', 'mozzarella', 'chicken', 'pineapples'])


def get_pizza(pizza_type: str, pizza_size: str = 'L') -> Pizza:
    '''
    Factory Method
    '''
    try:
        pizza = PizzaType[pizza_type.upper()]
        size = PizzaSize[pizza_size.upper()]
        if pizza == PizzaType.MARGARITA:
            return PizzaMargarita(size)
        if pizza == PizzaType.PEPPERONI:
            return PizzaPepperoni(size)
        if pizza == PizzaType.HAWAIIAN:
            return PizzaHawaiian(size)
    except KeyError:
        return None


if __name__ == '__main__':
    p = get_pizza('margarita', 'XL')
    print(p.dict())
    menu = []
    for pizza in PizzaType:
        my_pizza = get_pizza(pizza.name, 'XL')
        menu.append(my_pizza)
    my_pizza = get_pizza('margarita', 'L')
    print(menu[0] == menu[1])
    print(menu[0] == my_pizza)
    print(menu[0] == 0)
    print(menu[0] == p)
