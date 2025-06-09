from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.core.classes.suscriberClass import SuscriberClass
from app.models import CreateUser, CheckCredentials, ActivateSuscription, DesActivateSuscription

router = APIRouter()
suscriber = SuscriberClass()

# -------------------------------------------------------------------------------------------------
@router.post("/users", summary="Register a new user")
def register_user(createUser: CreateUser):
    """
    Registers a new subscriber with name, email and password.
    """
    response = suscriber.addNewSuscriber(createUser.name, createUser.email, createUser.password)
    return JSONResponse(content=response["content"], status_code=response["status"])

# -------------------------------------------------------------------------------------------------
@router.post("/users/login", summary="Authenticate a user")
def login_user(checkCredential: CheckCredentials):
    """
    Authenticates a subscriber using email and password.
    """
    response = suscriber.checkCredentials(checkCredential.email, checkCredential.password)
    return JSONResponse(content=response["content"], status_code=response["status"])

# -------------------------------------------------------------------------------------------------
@router.post("/subscriptions/activate", summary="Activate a subscription")
def activate_subscription(activate: ActivateSuscription):
    """
    Activates a subscription by its ID.
    """
    response = suscriber.activateSubscription(activate.id)
    return JSONResponse(content=response["content"], status_code=response["status"])

# -------------------------------------------------------------------------------------------------
@router.post("/subscriptions/deactivate", summary="Deactivate a subscription")
def deactivate_subscription(desActivate: DesActivateSuscription):
    """
    Deactivates a subscription by its ID.
    """
    response = suscriber.deactivateSubscription(desActivate.id)
    return JSONResponse(content=response["content"], status_code=response["status"])
