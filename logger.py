from pizza import get_pizza
from random import randint
from typing import Callable


def log(message) -> Callable:
    def decorator(func: Callable) -> Callable:
        if callable(message):
            print(f"{message.__name__} - 2c")

        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            time: int = randint(5, 10)
            print(message.format(time))

        return wrapper

    return decorator


@log
def bake(pizza):
    """Готовит пиццу"""
    pass


@log("🛵 Доставили за {} с")
def delivery(pizza):
    """Доставляет пиццу"""
    pass


@log("🏠 Забрали за {}с!")
def pickup(pizza):
    """Самовывоз"""
    pass


if __name__ == "__main__":
    pizza = get_pizza("margarita", "L")
    bake(pizza)
    delivery(pizza)
    pickup(pizza)
