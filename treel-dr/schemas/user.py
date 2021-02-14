import pydantic
from typing import List, Optional
from datetime import datetime

class UserSchema(pydantic.BaseModel):
    first: Optional[str]
    last: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]
    interval: Optional[int]
    subscribed: Optional[List[str]]
    token: Optional[str]
    nextJob: Optional[datetime]
    lastJob: Optional[datetime]
    cb_p_key: Optional[str]
    cb_s_key: Optional[str]