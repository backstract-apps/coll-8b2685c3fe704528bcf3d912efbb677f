from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_boring project(db: Session):

    Boring Project_all = db.query(models.Boring project).all()
    Boring Project_all = [new_data.to_dict() for new_data in Boring Project_all] if Boring Project_all else Boring Project_all

    res = {
        'Boring Project_all': Boring Project_all,
    }
    return res

async def put_boring project_id(db: Session, id: int, user_name: str):

    Boring Project_edited_record = db.query(models.Boring project).filter(models.Boring project.id == id).first()
    for key, value in {'id': id, 'user_name': user_name}.items():
          setattr(Boring Project_edited_record, key, value)
    db.commit()
    db.refresh(Boring Project_edited_record)
    Boring Project_edited_record = Boring Project_edited_record.to_dict() 

    res = {
        'Boring Project_edited_record': Boring Project_edited_record,
    }
    return res

async def delete_boring project_id(db: Session, id: int):

    Boring Project_deleted = None
    record_to_delete = db.query(models.Boring project).filter(models.Boring project.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        Boring Project_deleted = record_to_delete.to_dict() 

    res = {
        'Boring Project_deleted': Boring Project_deleted,
    }
    return res

async def get_boring project_id(db: Session, raw_data: schemas.GetBoring projectId):
    id:int = raw_data.id
    devil_name:str = raw_data.devil_name


    record_to_be_added = {'id': id, 'devil_name': devil_name}
    new_devil = models.Devil(**record_to_be_added)
    db.add(new_devil)
    db.commit()
    db.refresh(new_devil)
    devil_inserted_record = new_devil.to_dict()



    file_upload: str = file_upload

    res = {
        'devil_inserted_record': devil_inserted_record,
    }
    return res

async def post_boring project(db: Session, raw_data: schemas.PostBoring project):
    id:int = raw_data.id
    name:str = raw_data.name
    last_name:str = raw_data.last_name


    record_to_be_added = {'id': id, 'name': name}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        'users_inserted_record': users_inserted_record,
    }
    return res

