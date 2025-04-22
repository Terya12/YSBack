from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


# --- OrderItem ---

class OrderItemBase(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    price: float


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = 1
    price: float


class OrderItemOut(OrderItemBase):
    id: int

    class Config:
        orm_mode = True