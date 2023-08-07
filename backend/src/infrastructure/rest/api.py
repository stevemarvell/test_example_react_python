from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from flask import Request
from starlette import status
from starlette.responses import JSONResponse

from infrastructure.rest.routes.greeter import router as greeter_router

api = FastAPI()


@api.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": exc.errors()},
    )


origins = [
    "http://localhost",
    "http://localhost:3000",  # front end
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

api.include_router(greeter_router, prefix="/greet", tags=["greeter"])
