# redis
from redis_om import (
    JsonModel,
    EmbeddedJsonModel
)

# formats, etc
from typing import List, Optional
from pydantic import PositiveInt, PositiveFloat, Field

# custom modules
from core.base_models import BaseModel

class ProductImage(EmbeddedJsonModel, BaseModel):
    '''
    This model holds images for a product
    '''
    alt: Optional[str] = Field(max_length=32)
    url: str

    # visiblity
    primary: bool
    is_public: bool = Field(default=True)
    is_active: bool = Field(default=True)

class Product(JsonModel, BaseModel):
    '''
    This model represents a single product and it's embedded images
    '''
    # product basic info
    name: str
    description: Optional[str]
    images: List[ProductImage]

    # amount
    mrp: Optional[PositiveFloat]
    price: PositiveFloat

    # metadata
    stock: PositiveInt
    tags: List[str]

    # visiblity
    is_public: bool = Field(default=True)
    is_active: bool = Field(default=True)
