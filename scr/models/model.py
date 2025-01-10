from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from datetime import date
from decimal import Decimal


class Subscription(SQLModel, table=True):
    id: int = Field(primary_key=True)
    comporation: str
    site: Optional[str] = None
    subscription_date: date
    price_subscription: Decimal

class Payments(SQLModel, table=True):
    id: int = Field(primary_key=True)
    Subscription_id: int = Field(foreign_key='subscription.id')
    subscription: Subscription = Relationship()
    date: date
