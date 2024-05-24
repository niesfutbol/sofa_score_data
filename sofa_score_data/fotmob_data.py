from pydantic import BaseModel


class Shots(BaseModel):
    playerName: str
