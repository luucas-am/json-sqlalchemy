from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from src.api.test.controller import tests_router

server = FastAPI(title="JSON Test")

cors_origins = ["http://localhost:8001"]
server.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@server.get("/", tags=["Home"], status_code=200, response_model=None)
async def home():
    return RedirectResponse("/docs")


server.include_router(tests_router)
