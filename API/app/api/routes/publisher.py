from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.core.classes.publisherClass import PublisherClass
from app.models import UserInfromation, Notification, NewArticle, SearchedTopic

router = APIRouter()
publisher = PublisherClass()

# ------------------------------------------------------------------------------
@router.get("/topics", summary="Get all available topics")
def list_topics():
    """
    Returns the list of all available topics to which users can subscribe.
    """
    response = publisher.getTopics()
    return JSONResponse(content=response["content"], status_code=response["status"])

# ------------------------------------------------------------------------------
@router.get("/users", summary="Get all registered users")
def list_users():
    """
    Returns a list of all registered users (subscribers) in the system.
    """
    response = publisher.getUsersInfo()
    return JSONResponse(content=response["content"], status_code=response["status"])

# ------------------------------------------------------------------------------
@router.post("/topics/{topic}/subscribers", summary="Get users subscribed to a specific topic")
def get_users_by_topic(searchedTopic: SearchedTopic):
    """
    Returns all users subscribed to a given topic.
    """
    response = publisher.getUsersInfoSuscribedToAtopic(searchedTopic.topic)
    return JSONResponse(content=response["content"], status_code=response["status"])

# ------------------------------------------------------------------------------
@router.post("/users/{email}/subscriptions", summary="Get topics a user is subscribed to")
def get_user_subscriptions(userInformation: UserInfromation):
    """
    Returns the list of topics to which a user (by email) is currently subscribed.
    """
    response = publisher.getUserSuscriptions(userInformation.email)
    return JSONResponse(content=response["content"], status_code=response["status"])

# ------------------------------------------------------------------------------
@router.post("/notifications", summary="Send notification to all users")
def notify_all_users(notification: Notification):
    """
    Sends a notification message to all active subscribers in the system.
    """
    response = publisher.sendNotificationToAllSuscribers(notification.notification)
    return JSONResponse(content=response["content"], status_code=response["status"])

# ------------------------------------------------------------------------------
@router.post("/topics/{topic}/notifications", summary="Send notification to users of a specific topic")
def notify_users_by_topic(newArticle: NewArticle):
    """
    Sends a notification message to all users subscribed to the specified topic.
    """
    response = publisher.sendNotificationToUsersSuscribedToATopic(newArticle.topic)
    return JSONResponse(content=response["content"], status_code=response["status"])
