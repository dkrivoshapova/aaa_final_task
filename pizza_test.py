import unittest
from pizza import get_pizza, PizzaSize, Pepperoni, Margarita, Pizza


class TestGetPizza(unittest.TestCase):
    def test_get_margarita_pizza(self):
        margarita_pizza = get_pizza('MARGARITA', 'XL')
        self.assertIsNotNone(margarita_pizza)
        self.assertIsInstance(margarita_pizza, Margarita)
        self.assertEqual(margarita_pizza.get_name(), 'Margarita')
        self.assertEqual(margarita_pizza.get_size(), PizzaSize.XL)

    def test_get_pepperoni_pizza(self):
        pepperoni_pizza = get_pizza('PEPPERONI', 'L')
        self.assertIsNotNone(pepperoni_pizza)
        self.assertIsInstance(pepperoni_pizza, Pepperoni)
        self.assertEqual(pepperoni_pizza.get_name(), 'Pepperoni')
        self.assertEqual(pepperoni_pizza.get_size(), PizzaSize.L)

    def test_get_hawaiian_pizza_invalid_size(self):
        hawaiian_pizza = get_pizza('HAWAIIAN', 'InvalidSize')
        self.assertIsNone(hawaiian_pizza)

    def test_get_invalid_pizza(self):
        invalid_pizza = get_pizza('INVALID_PIZZA_TYPE')
        self.assertIsNone(invalid_pizza)


class TestPizzaEquality(unittest.TestCase):
    def test_same_pizza_objects(self):
        pizza1 = Pizza(PizzaSize.L, 'Margarita', '🧀',
                       ['tomato sauce', 'mozzarella'])
        pizza2 = Pizza(PizzaSize.L, 'Margarita', '🧀',
                       ['tomato sauce', 'mozzarella'])
        self.assertEqual(pizza1 == pizza2, True)

    def test_different_pizza_objects(self):
        pizza1 = Pizza(PizzaSize.L, 'Margarita', '🧀',
                       ['tomato sauce', 'mozzarella'])
        pizza2 = Pizza(
            PizzaSize.XL, 'Pepperoni', '🍕',
            ['tomato sauce', 'mozzarella', 'pepperoni']
        )
        self.assertEqual(pizza1 == pizza2, False)

    def test_equal_pizza_objects_with_different_order_of_ingredients(self):
        pizza1 = Pizza(PizzaSize.L, 'Margarita', '🧀',
                       ['tomato sauce', 'mozzarella'])
        pizza2 = Pizza(PizzaSize.L, 'Margarita', '🧀',
                       ['mozzarella', 'tomato sauce'])
        self.assertEqual(pizza1 == pizza2, False)

    def test_non_pizza_object_comparison(self):
        pizza = Pizza(PizzaSize.L, 'Margarita', '🧀',
                      ['tomato sauce', 'mozzarella'])
        non_pizza_object = 'This is not a pizza'
        self.assertEqual(pizza == non_pizza_object, False)


if __name__ == '__main__':
    unittest.main()
