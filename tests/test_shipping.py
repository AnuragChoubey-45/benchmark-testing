from app.customer import Customer
from app.shipping import shipping_fee


def test_premium_gets_free_shipping_at_500():
    assert shipping_fee(Customer("p1", "premium"), 500) == 0


def test_regular_needs_1000_for_free_shipping():
    assert shipping_fee(Customer("r1", "regular"), 500) == 79
