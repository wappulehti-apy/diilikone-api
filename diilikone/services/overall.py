from diilikone.models import (
    Deal,
    DealGroup,
    ProductType
)


def get_status_data():
    groups = DealGroup.query.all()
    deals = Deal.query.order_by(Deal.created_at.desc()).all()
    products = ProductType.query.all()

    total_sum = sum(deal.size for deal in deals)
    sorted_groups = sorted(
        groups, key=lambda deal_group: deal_group.total_size,
        reverse=True
    )
    new_deals = deals[:10]

    data = {
        'total_size': total_sum,
        'groups': sorted_groups,
        'salespersons': len(deals),
        'products': products,
        'new_deals': new_deals
    }
    return data
