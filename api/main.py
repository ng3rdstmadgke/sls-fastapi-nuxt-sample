import os
from fastapi import FastAPI, APIRouter
from mangum import Mangum
from starlette.requests import Request

router = APIRouter()
@router.get("/hello")
def hello():
    return {"Hello": "World"}

@router.get("/event")
def event(request: Request):
    return {
        "event": request.scope["aws.event"],
    }

app = FastAPI()
app.include_router(router, prefix="/api")

handler = Mangum(app)