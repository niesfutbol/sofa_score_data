from typing import Optional
from pydantic import BaseModel


class Shots(BaseModel):
    playerName: str
    expectedGoals: float
    expectedGoalsOnTarget: Optional[float]
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
    home_score: int
    away_id: int
    away_name: str
    away_score: int


class Match_Momentum(BaseModel):
    matchId: int
    momentum_porc: float


class Teams(BaseModel):
    name: str
    id: int
    score: int


class Row_Table(BaseModel):
    id: int
    pts: int
    idx: int


RESULTS: dict = {55: "results/serie_a"}


class Player(BaseModel):
    id: str
    name: str
    birthDate: dict
