from app.inventory import can_fulfill, remaining_stock


def test_exact_inventory_can_be_fulfilled():
    assert can_fulfill(10, 10) is True


def test_remaining_stock_never_negative():
    assert remaining_stock(10, 12) == 0
