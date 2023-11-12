class Pizza():
    def __init__(self, name: str, size: str):
        self.__name = name
        self.__size = size
        self.__recipe = Recipe.get_recipe(name)


class Recipe():
    recipes = {}

    def __init__(self, name: str, symbol: str, ingredients: list[str]):
        self.__name = name
        self.__symbol = symbol
        self.__ingredients = ingredients
        __class__.recipes[name] = ingredients

    def __str__(self):
        ingredients = ', '.join(self.__ingredients)
        return f'{self.__name} {self.__symbol}: {ingredients}'

    @classmethod
    def get_recipe(cls, name):
        if name in __class__.recipes:
            return __class__.recipes[name]


m = Recipe('Margherita', '🧀', ["tomato sauce", "mozzarella", "tomatoes"])
p = Recipe('Pepperoni', '🍕', ["tomato sauce", "mozzarella", "pepperoni"])
h = Recipe('Hawaiian', '🍍', ["tomato sauce",
           "mozzarella", "chicken", "pineapples"])
print(Recipe.get_recipe('Margherita'))
