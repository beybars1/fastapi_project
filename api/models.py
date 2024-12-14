import re
from typing import Optional
import uuid
from pydantic import BaseModel, EmailStr, constr, validator
from fastapi import HTTPException

### api models

LETTER_MATCH_PATTERN = re.compile(r'^[a-zA-Zа-яА-Я\-]+$')

class TunedModel(BaseModel):
    class Config:
        """converts even non dict to json"""
        orm_mode=True
    
class ShowUser(TunedModel): #output query
    user_id:uuid.UUID
    name:str
    surname:str
    email:EmailStr
    is_active:bool

class UserCreate(BaseModel): #input query
    name:str
    surname:str
    email:EmailStr
    password: str
   
    @validator("name")
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(status_code=422, detail="Name should contain only letters!")
        return value
        
    @validator("surname")
    def validate_surname(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(status_code=422, detail="Surname should contain only letters!")
        return value
    
class DeleteUserResponse(BaseModel): # deleted user response
    deleted_user_id: uuid.UUID
    
class UpdateUserResponse(BaseModel): # updated user response
    updated_user_id: uuid.UUID

class UpdateUserRequest(BaseModel): # updated user response
    name: Optional[constr(min_length=1)]
    surname: Optional[constr(min_length=1)]
    email: Optional[EmailStr]
    
    @validator("name")
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(status_code=422, detail="Name should contain only letters!")
        return value
        
    @validator("surname")
    def validate_surname(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(status_code=422, detail="Surname should contain only letters!")
        return value
    

class Token(BaseModel):
    access_token: str
    token_type: str