from enum import Enum
from typing import Optional


class PizzaType(Enum):
    """
    Перечисление текущих рецептов пицц в пиццерии,
    которые можно приготовить
    """

    MARGARITA = ("MARGARITA",)
    PEPPERONI = ("PEPPERONI",)
    HAWAIIAN = "HAWAIIAN"


class PizzaSize(Enum):
    """
    Перечисление текущих размеров пицц в пиццерии,
    которые можно приготовить
    """

    L = ("L",)
    XL = "XL"


class Pizza:
    """
    Базовый класс для пицц, которые можно
    приготовить в пиццерии
    """

    def __init__(self, size: PizzaSize, name: str, symbol: str,
                 ingridients: list[str]):
        self.__size = size
        self.__name = name
        self.__emoj = symbol
        self.__ingridients = ingridients

    def dict(self) -> dict:
        recipe = {"name": self.__name, "ingridients": self.__ingridients}
        return recipe

    def __eq__(self, other) -> bool:
        if not isinstance(other, Pizza):
            return False
        if self.__size != other.__size:
            return False
        if self.__name != other.__name:
            return False
        if self.__ingridients != other.__ingridients:
            return False
        return True

    def __str__(self) -> str:
        return f'{self.__name} {self.__emoj}: {", ".join(self.__ingridients)}'

    def get_size(self) -> PizzaSize:
        return self.__size

    def get_name(self) -> str:
        return self.__name


class Margarita(Pizza):
    def __init__(self, size: PizzaSize = PizzaSize.L):
        super().__init__(
            size, "Margarita", "🧀", ["tomato sauce", "mozzarella", "tomatoes"]
        )


class Pepperoni(Pizza):
    def __init__(self, size: PizzaSize = PizzaSize.L):
        super().__init__(
            size, "Pepperoni", "🍕", ["tomato sauce", "mozzarella", "pepperoni"]
        )


class Hawaiian(Pizza):
    def __init__(self, size: PizzaSize = PizzaSize.L):
        super().__init__(
            size,
            "Hawaiian",
            "🍍",
            ["tomato sauce", "mozzarella", "chicken", "pineapples"],
        )


def get_pizza(pizza_type: str, pizza_size: str = "L") -> Optional[Pizza]:
    """
    Factory Method
    """
    try:
        pizza = PizzaType[pizza_type.upper()]
        size = PizzaSize[pizza_size.upper()]
        if pizza == PizzaType.MARGARITA:
            return Margarita(size)
        if pizza == PizzaType.PEPPERONI:
            return Pepperoni(size)
        if pizza == PizzaType.HAWAIIAN:
            return Hawaiian(size)
    except KeyError:
        return None


if __name__ == "__main__":
    p = get_pizza("margarita", "XL")
    if p is not None:
        print(p.dict())
    menu = []
    for pizza in PizzaType:
        my_pizza = get_pizza(pizza.name, "XL")
        menu.append(my_pizza)
    my_pizza = get_pizza("margarita", "L")
    print(menu[0] == menu[1])
    print(menu[0] == my_pizza)
    print(menu[0] == 0)
    print(menu[0] == p)
