#cnt_category - общее кол-во категорий, cnt_unique_item - общее кол-во уникальных продуктов
import pytest

from main import Category, Product

@pytest.fixture
def test_category_summa():
    return Category("Фрукты", "ЗОЖ", [1, 2, 3, 4])


def test_summ(test_category_summa):
    assert test_category_summa.cnt_category == 1
    assert test_category_summa.cnt_unique_item == 4


@pytest.fixture()
def category_fruit():
    return Category('Фрукты', 'ЗОЖ', [1, 2, 3, 4])


def test_category(category_fruit):
    assert category_fruit.name == 'Фрукты'
    assert category_fruit.description == 'ЗОЖ'
    assert category_fruit.item == [1, 2, 3, 4]

@pytest.fixture()
def product_apple():
    return Product('Яблоко', 'Антоновка', 50, 25)


def test_product(product_apple):
    assert product_apple.name == 'Яблоко'
    assert product_apple.description == 'Антоновка'
    assert product_apple.price == 50
    assert product_apple.cnt_item == 25


