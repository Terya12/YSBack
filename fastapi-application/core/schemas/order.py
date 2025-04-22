from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from .order_item import OrderItemOut, OrderItemCreate


class OrderBase(BaseModel):
    user_id: int
    status: str = "pending"
    total_amount: float


class OrderCreate(OrderBase):
    items: List[OrderItemCreate]


class OrderOut(OrderBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    items: List[OrderItemOut]

    class Config:
        orm_mode = True