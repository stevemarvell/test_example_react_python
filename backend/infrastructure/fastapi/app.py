from fastapi import Depends
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schema import SchemaError

from application import greeting_by_name_query
from di import dependency_manager

app = FastAPI()

@app.get("/greet")
def greet(name, greeting_repository=Depends(dependency_manager.greeting_repository)):
    try:
        greeting = greeting_by_name_query.handle(greeting_repository, {"name": name})
        return {"greeting": greeting}
    except SchemaError as e:
        raise RequestValidationError("Invalid or missing parameter")


origins = [
    "http://localhost",
    "http://localhost:3000",  # front end
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
