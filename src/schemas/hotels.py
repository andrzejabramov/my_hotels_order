from pydantic import BaseModel


class HotelsAdd(BaseModel):
    title: str
    location: str
