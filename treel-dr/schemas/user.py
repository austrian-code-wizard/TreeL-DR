import pydantic
from typing import List, Optional
from datetime import datetime

class UserSchema(pydantic.BaseModel):
    first: Optional[str]
    last: Optional[str]
    phoneNumber: Optional[str]
    email: str
    interval: Optional[str]
    subscribed: Optional[List[str]]
    token: Optional[str]
    nextJob: Optional[datetime]