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


RESULTS: dict = {
    42: "results/champions_league",
    55: "results/serie_a",
    54: "results/bundesliga",
    87: "results/laliga",
    47: "results/premierleague",
    230: "results/ligaMX",
}


class Player(BaseModel):
    id: int
    name: str
    birthDate: dict


class Member(BaseModel):
    id: int
    name: str
