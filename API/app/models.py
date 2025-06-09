from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
    name     : str
    email    : EmailStr
    password : str

class CheckCredentials(BaseModel):
    email    : EmailStr
    password : str

class UserInfromation(BaseModel):
    email    : EmailStr

class ActivateSuscription(BaseModel):
    id       : int

class DesActivateSuscription(BaseModel):
    id       : int

class NewArticle(BaseModel):
    topic    : str

class Notification(BaseModel):
    notification    : str

class SearchedTopic(BaseModel):
    topic   : str