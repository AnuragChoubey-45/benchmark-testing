from app.customer import Customer
from app.pricing import final_price


def test_premium_gets_20_percent_discount():
    assert final_price(Customer("p1", "premium"), 1000) == 800


def test_regular_gets_5_percent_discount():
    assert final_price(Customer("r1", "regular"), 1000) == 950
