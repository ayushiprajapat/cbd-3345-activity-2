import unittest
from app import calculate_cart_value, validate_cart_items

def test_calculate_cart_value_empty_cart():
    assert calculate_cart_value([]) == 0

def test_calculate_cart_value_invalid_product_ids():
    cart_items = [{"product_id": None, "quantity": 2, "price_per_unit": 200}]
    assert calculate_cart_value(cart_items) == 0

def test_calculate_cart_value_negative_quantities():
    cart_items = [{"product_id": "1", "quantity": -1, "price_per_unit": 1200}]
    assert calculate_cart_value(cart_items) == 0



# Test for validate_cart_items
def test_validate_cart_items():
    valid_cart = [{"product_id": "1", "quantity": 2, "price_per_unit": 1200}]
    invalid_cart = [{"product_id": "3", "quantity": -1, "price_per_unit": 50}]
    assert validate_cart_items(valid_cart) is True
    assert validate_cart_items(invalid_cart) is False



