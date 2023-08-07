from fastapi import APIRouter, HTTPException

from application import greeting_by_name_query

router = APIRouter()


# because the prefix is defined in the api
@router.get("/")
def greet(name):
    if not name:
        raise HTTPException(status_code=400, detail="Invalid or missing 'name' parameter")

    greeting = greeting_by_name_query.handle(name)
    return {"greeting": greeting}
