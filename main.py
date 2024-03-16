class Category:
    cnt_category = 0
    cnt_unique_item = 0
    name: str
    description: str
    item: list

    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.item = item

        Category.cnt_category = 1
        Category.cnt_unique_item += 1

cat_1 = Category('Фрукты', 'ЗОЖ', [1, 2, 3, 4])
cat_2 = Category('Овощи', 'ЗОЖ', [1, 2, 3, 4])
cat_3 = Category('Фрукты', 'ЗОЖ', [1, 2, 3, 4])

print(f"Общее кол-во категорий: {Category.cnt_category}")
print(f"Общее кол-во уникальных продуктов: {Category.cnt_unique_item}")

class Product:
    name: str
    description: str
    price: float
    cnt_item: int

    def __init__(self, name, description, price, cnt_item):
        self.name = name
        self.description = description
        self.price = price
        self.cnt_item = cnt_item
