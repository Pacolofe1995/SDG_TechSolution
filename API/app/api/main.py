from fastapi import APIRouter
from app.api.routes import home
from app.api.routes import publisher
from app.api.routes import subscribers

api_router = APIRouter()
api_router.include_router(home.router, tags=["Home"])
api_router.include_router(publisher.router, tags=["Publisher"])
api_router.include_router(subscribers.router, tags=["Suscribers"])

