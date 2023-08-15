from fastapi import APIRouter, Depends
from werkzeug.exceptions import BadRequest, HTTPException
from schema import SchemaError

from application import greeting_by_name_query
from di import dependency_manager

router = APIRouter()


@router.get("/")
def greet(name, greeting_repository=Depends(dependency_manager.greeting_repository)):
    try:
        greeting = greeting_by_name_query.handle(greeting_repository, {"name": name})
        return {"greeting": greeting}
    except SchemaError as e:
        raise BadRequest()
    except Exception as e:
        raise HTTPException(code=500, detail="The Sky is Falling")
