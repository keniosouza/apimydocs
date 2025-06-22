import re
from typing import Optional, List
from pydantic import BaseModel, EmailStr, field_validator
from datetime import date, datetime

# Schema base para produtos
class ProductSchemaBase(BaseModel):
    product_id: Optional[int] = None
    user_id: Optional[int] = None
    situation_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    date_register: Optional[datetime] = None
    date_update: Optional[datetime] = None

    class Config:
        from_attributes = True