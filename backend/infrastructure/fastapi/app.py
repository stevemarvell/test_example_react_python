from fastapi import Depends
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from schema import SchemaError
from werkzeug.exceptions import BadRequest, InternalServerError

from application import greeting_by_name_query
from di import dependency_manager

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    raise BadRequest()


@app.get("/greet")
def greet(name, greeting_repository=Depends(dependency_manager.greeting_repository)):
    try:
        greeting = greeting_by_name_query.handle(greeting_repository, {"name": name})
        return {"greeting": greeting}
    except SchemaError as e:
        raise BadRequest(e.args[0])
    except BadRequest as e:
        raise e
    except Exception as e:
        raise InternalServerError(e.args[0])

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
