from fastapi import APIRouter, Depends

from src.api.test.schemas import (
    GetOneTestResponse,
    CreateOneTestPayload,
    UpdateOneTestPayload,
)
from src.api.test.service import TestService

from src.database import get_db

tests_router = APIRouter(
    prefix="/api/tests", tags=["Tests"], dependencies=[Depends(get_db)]
)


@tests_router.get("/", response_model=list[GetOneTestResponse], status_code=200)
async def get_all_tests(db=tests_router.dependencies[0]):
    return TestService.get_all(db=db)


@tests_router.get("/{test_id}", response_model=GetOneTestResponse, status_code=200)
async def get_one_test(test_id: str, db=tests_router.dependencies[0]):
    return TestService.get_one(db=db, id=test_id)


@tests_router.post("/", response_model=GetOneTestResponse, status_code=201)
async def create_one_test(
    payload: CreateOneTestPayload, db=tests_router.dependencies[0]
):
    return TestService.create_one(db=db, payload=payload)


@tests_router.put("/{test_id}", response_model=GetOneTestResponse, status_code=200)
async def update_one_test(
    test_id: str, payload: UpdateOneTestPayload, db=tests_router.dependencies[0]
):
    return TestService.update_one(db=db, id=test_id, payload=payload)


@tests_router.delete("/{test_id}", response_model=GetOneTestResponse, status_code=200)
async def delete_one_test(test_id: str, db=tests_router.dependencies[0]):
    return TestService.delete_one(db=db, id=test_id)
