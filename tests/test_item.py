"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item


def test__init__():
    assert Item('Смартфон', 10000, 20)
    assert Item('Ноутбук', 20000, 5)


def test_calculate_total_price():
    assert Item.calculate_total_price()
    assert Item.calculate_total_price(self=Item)


def test_apply_discount():
    assert Item.pay_rate == 1.0
