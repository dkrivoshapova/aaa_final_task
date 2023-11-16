from pizza import PizzaMargarita


def log(message):
    def decorator(func):
        if callable(message):
            print(f'{message.__name__} - 2c')

        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            t = 10
            print(message.format(t))
        return wrapper
    return decorator


@log
def bake(pizza):
    """Готовит пиццу"""
    pass


@log('🛵 Доставили за {} с')
def delivery(pizza):
    """Доставляет пиццу"""
    pass


@log('🏠 Забрали за {}с!')
def pickup(pizza):
    """Самовывоз"""


if __name__ == '__main__':
    pizza = PizzaMargarita()
    bake(pizza)
    delivery(pizza)
    pickup(pizza)
