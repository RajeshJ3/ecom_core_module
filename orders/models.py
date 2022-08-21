# redis
from redis_om import (
    Migrator,
    JsonModel,
    EmbeddedJsonModel
)

# formats, etc
from typing import List, Optional

from redis_om import Field

# custom modules
from base_models import BaseModel


class Customer(EmbeddedJsonModel, BaseModel):
    '''
    This model represents a customer
    '''

    first_name: str
    last_name: str
    email: str


class Order(JsonModel, BaseModel):
    '''
    This model represents a single order and it's embedded items
    '''
    # authentication
    token: str = Field(index=True)

    # order details
    order_items: List[str]
    # init, pending, completed, cancelled, declined, refunded
    status: str = Field(index=True, default="init")

    # customer
    customer: Optional[Customer]

    # other
    invoice_url: Optional[str]

def run_orders_migrator():
    print("Migrating orders", end=" ")
    Migrator().run()
    print("[DONE]")
