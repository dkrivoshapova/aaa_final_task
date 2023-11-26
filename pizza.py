from enum import Enum
from typing import Optional


class PizzaType(Enum):
    """
    List of current pizza recipes available at the pizzeria.
    """

    MARGARITA = "MARGARITA"
    PEPPERONI = "PEPPERONI"
    HAWAIIAN = "HAWAIIAN"


class PizzaSize(Enum):
    """
    List of current pizza sizes available at the pizzeria.
    """

    L = "L"
    XL = "XL"


class Pizza:
    """
    Represents a base class for a pizza.

    Attributes:
    - size (PizzaSize): Size of the pizza.
    - name (str): Name of the pizza.
    - emoji (str): Emoji symbol representing the pizza.
    - ingredients (List[str]): List of ingredients in the pizza.
    """

    def __init__(self, size: PizzaSize, name: str, symbol: str,
                 ingridients: list[str]):
        self.__size = size
        self.__name = name
        self.__emoj = symbol
        self.__ingridients = ingridients

    def dict(self) -> dict:
        """
        Returns a dictionary representation of the pizza's recipe.

        Returns:
        - dict: Dictionary containing the name and ingredients of the pizza.
        """
        recipe = {"name": self.__name, "ingridients": self.__ingridients}
        return recipe

    def __eq__(self, other) -> bool:
        """
        Checks if two pizzas are equal.

        Returns:
        - bool: True if two pizzas are equal, False otherwise.
        """
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
        """
        Returns a string representation of the Pizza object.

        Returns:
        - str: String describing the pizza's name, emoji, and ingredients.
        """
        return f'{self.__name} {self.__emoj}: {", ".join(self.__ingridients)}'

    def get_size(self) -> PizzaSize:
        """
        Returns the size of the pizza.

        Returns:
        - PizzaSize: Size of the pizza.
        """
        return self.__size

    def get_name(self) -> str:
        """
        Returns the name of the pizza.

        Returns:
        - str: Name of the pizza.
        """
        return self.__name


class Margarita(Pizza):
    """
    Represents a Margarita pizza, inheriting from the Pizza class.

    Parameters:
    - size (PizzaSize, optional): Size of the pizza (default is PizzaSize.L).
    """

    def __init__(self, size: PizzaSize = PizzaSize.L):
        super().__init__(
            size, "Margarita", "🧀", ["tomato sauce", "mozzarella", "tomatoes"]
        )


class Pepperoni(Pizza):
    """
    Represents a Pepperoni pizza, inheriting from the Pizza class.

    Parameters:
    - size (PizzaSize, optional): Size of the pizza (default is PizzaSize.L).
    """

    def __init__(self, size: PizzaSize = PizzaSize.L):
        super().__init__(
            size, "Pepperoni", "🍕", ["tomato sauce", "mozzarella", "pepperoni"]
        )


class Hawaiian(Pizza):
    """
    Represents a Hawaiian pizza, inheriting from the Pizza class.

    Parameters:
    - size (PizzaSize, optional): Size of the pizza (default is PizzaSize.L).
    """

    def __init__(self, size: PizzaSize = PizzaSize.L):
        super().__init__(
            size,
            "Hawaiian",
            "🍍",
            ["tomato sauce", "mozzarella", "chicken", "pineapples"],
        )


def get_pizza(pizza_type: str, pizza_size: str = "L") -> Optional[Pizza]:
    """
    Returns a specific pizza based on the provided pizza type and size.

    Parameters:
    - pizza_type (str): Type of the pizza ("MARGARITA", "PEPPERONI",
      or "HAWAIIAN").
    - pizza_size (str, optional): Size of the pizza ("S", "M", or "L").
      Default is "L".

    Returns:
    - Optional[Pizza]: An instance of the requested Pizza type and size. 
    Returns None if the provided pizza type or size is invalid.
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
    p_2 = get_pizza("margarita", "XL")
    p_3 = get_pizza("HAWAIIAN", "L")
    print(p == p_2)
    print(p == p_3)
    print(p == 0)
