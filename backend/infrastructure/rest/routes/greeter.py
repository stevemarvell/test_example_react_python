from fastapi import APIRouter, HTTPException, Depends
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
        raise HTTPException(status_code=400, detail="Invalid or missing parameter")
    except Exception as e:
        raise HTTPException(status_code=500, detail="The Sky is Falling")
