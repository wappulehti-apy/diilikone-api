from diilikone.models import (
    Deal,
    DealGroup,
    ProductType
)


def get_status_data():
    groups = DealGroup.query.all()
    deals = Deal.query.all()
    products = ProductType.query.all()

    total_sum = sum(deal.size for deal in deals)
    sorted_groups = sorted(
        groups, key=lambda deal_group: deal_group.total_size,
        reverse=True
    )

    data = {
        'total_size': total_sum,
        'groups': sorted_groups,
        'salespersons': len(deals),
        'products': products
    }
    return data
