from pydantic import BaseModel


class Shots(BaseModel):
    playerName: str
    expectedGoals: float
    expectedGoalsOnTarget: float
