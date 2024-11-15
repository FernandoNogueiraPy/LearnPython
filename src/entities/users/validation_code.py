from pydantic import BaseModel
from datetime import datetime


class ValidationCode(BaseModel):
    code: str
    expires_at: datetime
    change_password: bool
