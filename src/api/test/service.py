from uuid import uuid4
from datetime import datetime, timezone
from sqlalchemy.orm import Session

from src.models.test import Test

from src.api.test.schemas import CreateOneTestPayload, UpdateOneTestPayload


class TestService:
    @staticmethod
    def get_all(db: Session) -> list[Test]:
        return db.query(Test).order_by(Test.created_at.asc()).all()

    @staticmethod
    def get_one(db: Session, id: str) -> Test:
        return db.query(Test).filter(Test.id == id).first()

    @staticmethod
    def create_one(db: Session, payload: CreateOneTestPayload) -> Test:
        test = Test(**payload.model_dump(exclude_none=True), created_by=uuid4())
        db.add(test)
        db.commit()
        db.refresh(test)
        return test

    @classmethod
    def update_one(cls, db: Session, id: str, payload: UpdateOneTestPayload) -> Test:
        test = cls.get_one(db=db, id=id)
        if not test:
            return None
        for key, value in payload.model_dump(exclude_none=True).items():
            setattr(test, key, value)
        test.updated_by = uuid4()
        test.updated_at = datetime.now(timezone.utc)
        db.commit()
        return test

    @classmethod
    def delete_one(cls, db: Session, id: str) -> Test:
        test = cls.get_one(db=db, id=id)
        if not test:
            return None
        db.delete(test)
        db.commit()
        return test
