from fastapi import APIRouter,HTTPException,Depends, status
from sqlalchemy.orm import Session
from ..db import models 


def getAll(db : Session) : 
    products = db.query(models.Product).all()
    return products