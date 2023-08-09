from fastapi import APIRouter, HTTPException

from di import dependency_manager

from application import greeting_by_name_query

router = APIRouter()


# because the prefix is defined in the api
@router.get("/")
def greet(name):
    if not name:
        raise HTTPException(status_code=400, detail="Invalid or missing 'name' parameter")

    greeting_repository = dependency_manager.greeting_repository()
    greeting = greeting_by_name_query.handle(greeting_repository, name)

    return {"greeting": greeting}
