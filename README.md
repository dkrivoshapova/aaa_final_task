# aaa_final_task

## cli

Доставка пиццы без указания размера(по умолчанию L)
```bash
python3 cli.py order pepperoni --delivery
```
Доставка пиццы c указанием размера
```bash
python3 cli.py order pepperoni L --delivery
```
Заказ пиццы c указанием размера
```bash
python3 cli.py order pepperoni L 
```
Заказ пиццы c неверным названием 
```bash
python3 cli.py order pepper  
```
Вывод меню
```bash
python3 cli.py menu  
```

## test
```bash
python3 -m unittest -v pizza_test.py
```