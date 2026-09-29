from app.auth import can_access_admin, can_view_reports
from app.customer import Customer


def test_only_admin_can_access_admin():
    assert can_access_admin(Customer("a", "admin")) is True
    assert can_access_admin(Customer("p", "premium")) is False


def test_premium_can_view_reports():
    assert can_view_reports(Customer("p", "premium")) is True
