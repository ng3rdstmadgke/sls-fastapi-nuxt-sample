import os
from fastapi import FastAPI, APIRouter
from mangum import Mangum
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter()
@router.get("/hello")
def hello():
    return {"Hello": "World"}

@router.get("/event")
def event(request: Request):
    return {
        "event": request.scope["aws.event"],
    }

app = FastAPI(root_path=os.getenv("API_BASE_PATH", ""))
app.include_router(router, prefix="/api")
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
app.mount("/", StaticFiles(directory=f"{PROJECT_ROOT}/front_dist", html=True), name="front")

# CORS: https://fastapi.tiangolo.com/tutorial/cors/
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

handler = Mangum(app)