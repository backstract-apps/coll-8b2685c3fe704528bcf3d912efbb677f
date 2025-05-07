from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/boring project/')
async def get_boring project(db: Session = Depends(get_db)):
    try:
        return await service.get_boring project(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/boring project/id/')
async def put_boring project_id(id: int, user_name: str, db: Session = Depends(get_db)):
    try:
        return await service.put_boring project_id(db, id, user_name)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/boring project/id')
async def delete_boring project_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_boring project_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/boring project/id')
async def get_boring project_id(raw_data: schemas.GetBoring projectId, db: Session = Depends(get_db)):
    try:
        return await service.get_boring project_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/boring project/')
async def post_boring project(raw_data: schemas.PostBoring project, db: Session = Depends(get_db)):
    try:
        return await service.post_boring project(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

