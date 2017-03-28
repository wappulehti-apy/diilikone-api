from diilikone.models import (
    DealGroup,
    GroupProvision,
    IndividualProvision,
    ProductType
)


def calculate_individual_part(size):
    provision = IndividualProvision.query.filter_by(quantity=size).one()
    return provision.price_per_magazine


def calculate_group_part(group_id, size):
    if group_id:
        group = DealGroup.query.get(group_id)
        return GroupProvision.query.filter_by(
              quantity=group.total_size + size
          ).one().price_per_magazine
    else:
        return 0


def calculate_total_price_of_products(product_ids):
        total_prices = 0
        for product_id in product_ids:
            product = ProductType.query.get(product_id)
            total_prices += product.price
        return total_prices


def calculate_group_cut(group_id, size):
    group_part = calculate_group_part(group_id, size)
    if group_part == 0:
        return 0
    group = DealGroup.query.get(group_id)
    return (group_part * group.percentage * size) / 100


def calculate(data):
    size = data.get('size')
    group_id = data.get('group_id', None)
    product_ids = data.get('product_ids', [])
    deal_exists = data.get('deal_exists', False)

    individual_part = calculate_individual_part(size)
    if deal_exists:
        group_part = calculate_group_part(group_id, 0)
    else:
        group_part = calculate_group_part(group_id, size)
    products_price = calculate_total_price_of_products(product_ids)
    guild_cut = calculate_group_cut(group_id, size)

    total_provision = (
        (individual_part + group_part) * size - products_price - guild_cut
    )
    per_magazine = total_provision / size

    return {
      'total': round(total_provision, 2),
      'per_magazine': round(per_magazine, 2),
      'group': round(guild_cut, 2)
    }
