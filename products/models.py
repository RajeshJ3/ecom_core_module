# redis
from redis_om import (
    Migrator,
    JsonModel
)

# formats, etc
from typing import List, Optional
from pydantic import PositiveFloat, PositiveInt

from redis_om import Field

# custom modules
from base_models import BaseModel


class Product(JsonModel, BaseModel):
    '''
    This model represents a single product
    '''
    # product basic info
    name: str = Field(index=True)
    description: Optional[str]

    # media
    thumbnail_url: str
    image_url: str

    # amount
    price: PositiveFloat = Field(index=True)

    # metadata
    tags: List[str] = Field(index=True)

    # analytics
    downloads: PositiveInt = Field(default=1)

def run_products_migrator():
    print("Migrating products", end=" ")
    Migrator().run()
    print("[DONE]")
