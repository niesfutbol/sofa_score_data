from pydantic import BaseModel


class Shots(BaseModel):
    playerName: str
    expectedGoals: float
    expectedGoalsOnTarget: float
    eventType: str
    teamId: int
    playerId: int
    x: float
    y: float
    min: int


class Matches(BaseModel):
    matchId: int
