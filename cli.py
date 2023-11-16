import click
from pizza import get_pizza
from random import randint
from pizza import PizzaType


@click.command()
@click.option("--delivery", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
@click.argument("size", nargs=1, default="L")
def order(pizza: str, delivery: bool, size: str):
    """Готовит и доставляет пиццу"""
    new_pizza = get_pizza(pizza, size)
    if new_pizza is None:
        click.echo(f"❌ {pizza} нет в нашем меню!")
    else:
        click.echo(f"🍕 Приготовили за {randint(1,5)}c!")
        if delivery:
            click.echo(f"🚗 Доставили за {randint(1,5)}c!")


@click.command()
def menu():
    """Выводит меню"""
    for pizza in PizzaType:
        my_pizza = get_pizza(pizza.name)
        print("-", my_pizza)


@click.group()
def cli():
    pass


cli.add_command(order)
cli.add_command(menu)

if __name__ == "__main__":
    cli()
