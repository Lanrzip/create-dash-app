from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import List, Dict
from datetime import datetime, date
from uuid import UUID


class TestDataModelIn(BaseModel):
    name: str = Field(..., example="John Doe")
    email: EmailStr = Field(..., example="")


class TestDataModelOut(BaseModel):
    id: UUID = Field(..., example="123e4567-e89b-12d3-a456-426614174000")
    name: str = Field(..., example="John Doe")
    email: EmailStr = Field(..., example="johndoe@example.com")
    url: HttpUrl = Field(..., example="http://example.com")
    age: int = Field(..., ge=0, le=120, example=30)
    balance: float = Field(..., example=100.50)
    is_active: bool = Field(..., example=True)
    created_at: datetime = Field(..., example="2023-01-01T00:00:00")
    birth_date: date = Field(..., example="1990-01-01")
    meta: Dict[str, str] = Field(..., example={"key1": "value1", "key2": "value2"})


    class Config:
        from_attributes = True