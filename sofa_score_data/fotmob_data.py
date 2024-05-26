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
    matchName: str
    home_id: int
    home_name: str


class Match_Momentum(BaseModel):
    matchId: int
    momentum_porc: float


class Teams(BaseModel):
    name: str
    id: int
    score: int
