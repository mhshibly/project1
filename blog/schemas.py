
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str

class Show_Blog(BaseModel):
    id: int
    title: str
    body: str


