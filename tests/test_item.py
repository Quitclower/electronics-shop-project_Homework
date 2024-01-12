"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


@pytest.fixture()
def test_calculate_total_price():
    assert Item("Смартфон", 10000, 20)
    assert Item("Ноутбук", 20000, 5)
