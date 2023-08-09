from fastapi import APIRouter, HTTPException, Depends
from application import greeting_by_name_query
from di import dependency_manager

router = APIRouter()

@router.get("/")
def greet(name, greeting_repository=Depends(dependency_manager.greeting_repository)):
    if not name:
        raise HTTPException(status_code=400, detail="Invalid or missing 'name' parameter")

    greeting = greeting_by_name_query.handle(greeting_repository, name)

    return {"greeting": greeting}
