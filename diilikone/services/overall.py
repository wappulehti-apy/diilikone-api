from diilikone.models import (
    Deal,
    DealGroup,
    ProductType
)
from sqlalchemy import func


def get_status_data():
    groups = DealGroup.query.all()
    deals = Deal.query.order_by(Deal.created_at.desc()).all()
    products = ProductType.query.all()
    total_sum = sum(deal.size for deal in deals)

    # get deals with backpacks
    deals_with_backpacks = ProductType.query.filter_by(
        name='Reppu').first().deals

    # of those deals, how many have NOT fetched backpack
    backpacks_to_be_fetched = sum(
        1 for d in deals_with_backpacks if not d.backpack_received)

    # get deals with products with name shirt
    deals_with_shirts = Deal.query.join(
        Deal.product_types).filter(ProductType.name.ilike("%paita%")).all()

    # calculate deals that have NOT received shirt
    shirts_to_be_fetched = sum(
        1 for d in deals_with_shirts if not d.shirt_received)

    magazines_to_be_fetched = Deal.query.with_entities(
        func.sum(Deal.size - Deal.magazines_received)).scalar()

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
        'new_deals': new_deals,
        'shirts_to_be_fetched': shirts_to_be_fetched,
        'backpacks_to_be_fetched': backpacks_to_be_fetched,
        'total_shirts': len(deals_with_shirts),
        'total_backpacks': len(deals_with_backpacks),
        'magazines_to_be_fetched': magazines_to_be_fetched,
    }
    return data
