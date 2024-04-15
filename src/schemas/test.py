from pydantic import Field
from datetime import datetime
from uuid import UUID
from typing import Optional

from src.helpers.schema_base import ORMBaseModel


class TestSchema(ORMBaseModel):
    id: UUID = Field(description="Test ID")
    name: str = Field(description="Test Name")
    age: int = Field(description="Test Age")
    json: dict = Field(description="Test JSON")

    created_by: UUID = Field(description="Test Created By")
    created_at: datetime = Field(description="Test Created At")
    updated_by: Optional[UUID] = Field(description="Test Updated By", default=None)
    updated_at: Optional[datetime] = Field(description="Test Updated At", default=None)
