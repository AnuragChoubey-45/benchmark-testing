from .customer import Customer


def can_access_admin(customer: Customer) -> bool:
    # In this toy system, only the explicitly marked admin tier has admin access.
    return customer.tier == "admin"


def can_view_reports(customer: Customer) -> bool:
    return customer.tier in {"admin", "premium"}
