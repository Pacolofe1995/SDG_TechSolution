from typing import Any
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.core.alchemy.database import engine, Base, Session  # importa tu sesión y base
from app.core.alchemy.models import Topic 

import json

router = APIRouter()


@router.get("/")
def home():
    """
    Root endpoint of the SDG Project API.
    Returns a welcome message confirming that the API is operational.
    """

    message = "Welcome! The API is up and running smoothly."
    return JSONResponse(content = message, status_code = 200)