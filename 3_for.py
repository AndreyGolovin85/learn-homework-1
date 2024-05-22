"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

sales_data = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    total_sales = {}
    for product in sales_data:
        total_sales[product['product']] = sum(product['items_sold'])

    average_sales = {}
    for product in sales_data:
        average_sales[product['product']] = sum(product['items_sold']) / len(product['items_sold'])

    total_sales_all = sum([sum(product['items_sold']) for product in sales_data])
    average_sales_all = sum([sum(product['items_sold']) for product in sales_data]) / len(
        [product['items_sold'] for product in sales_data])
    
    print("Всего продано продукта:")
    for product, sales in total_sales.items():
        print(f"{product}: {sales}")

    print("\nВ среднем продано:")
    for product, sales in average_sales.items():
        print(f"{product}: {sales}")

    print("\nВсего продано:", total_sales_all)
    print("Средняя продажа:", average_sales_all)


if __name__ == "__main__":
    main()
