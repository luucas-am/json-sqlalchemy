from pydantic import Field
from typing import Optional
from uuid import UUID
from datetime import datetime

from src.helpers.schema_base import ORMBaseModel


class GetOneTestResponse(ORMBaseModel):
    id: UUID = Field(description="Test ID")
    name: str = Field(description="Test Name")
    age: int = Field(description="Test Age")
    json: dict = Field(description="Test JSON")
    created_by: UUID = Field(description="Test Created By")
    created_at: datetime = Field(description="Test Created At")
    updated_by: Optional[UUID] = Field(description="Test Updated By", default=None)
    updated_at: Optional[datetime] = Field(description="Test Updated At", default=None)


class CreateOneTestPayload(ORMBaseModel):
    name: str = Field(description="Test Name")
    age: int = Field(description="Test Age")
    json: dict = Field(description="Test JSON")


class UpdateOneTestPayload(ORMBaseModel):
    name: Optional[str] = Field(description="Test Name", default=None)
    age: Optional[int] = Field(description="Test Age", default=None)
    json: Optional[dict] = Field(description="Test JSON", default=None)
