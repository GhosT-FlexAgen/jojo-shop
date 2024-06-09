from pydantic import BaseModel
from typing import Optional


class RegisterUser(BaseModel):
    name: str
    email: str
    password: str
    role: Optional[str] = "user"
    is_active: Optional[bool]
