# redis
from redis_om import (
    Migrator,
    JsonModel,
    EmbeddedJsonModel
)

# formats, etc
from typing import List, Optional
from pydantic import PositiveInt

from redis_om import Field

# custom modules
from base_models import BaseModel


class Address(EmbeddedJsonModel, BaseModel):
    '''
    This model represents address of a customer
    '''

    street: str
    line2: Optional[str]
    city: str
    state: str
    zip_code: str
    country: str


class Customer(EmbeddedJsonModel, BaseModel):
    '''
    This model represents a customer
    '''

    first_name: str
    last_name: str
    email: str
    phone: str

    address: Address


class OrderItem(EmbeddedJsonModel, BaseModel):
    '''
    This model holds items for a order
    '''

    product: str
    quantity: PositiveInt


class Order(JsonModel, BaseModel):
    '''
    This model represents a single order and it's embedded items
    '''
    # authentication
    token: str = Field(index=True)

    # order details
    order_items: List[OrderItem]
    status: str = Field(index=True, default="init") # init, pending, completed, cancelled, declined, refunded

    # customer
    customer: Optional[Customer]

    # other
    invoice_url: Optional[str]

def run_orders_migrator():
    print("Migrating orders", end=" ")
    Migrator().run()
    print("[DONE]")
