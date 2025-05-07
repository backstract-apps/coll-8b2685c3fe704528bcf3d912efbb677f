from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Boring project(BaseModel):
    id: int
    user_name: str


class ReadBoring project(BaseModel):
    id: int
    user_name: str
    class Config:
        from_attributes = True




class GetBoring projectId(BaseModel):
    id: int
    devil_name: str

    class Config:
        from_attributes = True



class PostBoring project(BaseModel):
    id: int
    name: str
    last_name: str

    class Config:
        from_attributes = True

