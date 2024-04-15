from uuid import uuid4, UUID
from datetime import datetime, timezone

from sqlalchemy import String, DateTime, Integer, JSON
from sqlalchemy.dialects.postgresql import UUID as UUID_, JSONB
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Test(Base):
    __tablename__ = "tests"

    id: Mapped[UUID] = mapped_column(
        UUID_(as_uuid=True), primary_key=True, default=uuid4
    )
    name: Mapped[str] = mapped_column(String(64), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    json: Mapped[JSON] = mapped_column(JSONB, nullable=False)

    created_by: Mapped[UUID] = mapped_column(UUID_(as_uuid=True), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.now(timezone.utc)
    )
    updated_by: Mapped[UUID] = mapped_column(UUID_(as_uuid=True), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
