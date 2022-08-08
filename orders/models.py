# redis
from redis_om import (
    JsonModel,
    EmbeddedJsonModel
)

# formats, etc
from typing import List
from pydantic import PositiveInt, Field

# custom modules
from core.base_models import BaseModel

class OrderItem(EmbeddedJsonModel, BaseModel):
    '''
    This model holds items for a order
    '''

    from core.products.models import Product

    product: Product
    quantity: PositiveInt


class Order(JsonModel, BaseModel):
    '''
    This model represents a single order and it's embedded items
    '''
    # details
    order_items: List[OrderItem]

    # visiblity
    is_active: bool = Field(default=True)
