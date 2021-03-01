from pydantic import BaseModel
from typing import Optional, Dict


class RedisCollectionCreateRequest(BaseModel):
    key: str
    data: Dict = None