from dataclasses import dataclass
from typing import List
import datetime

@dataclass
class Day():
    date: datetime.datetime
    win: int
    loss: int
    tie: int
    mmr: int

@dataclass 
class Days(): 
    days: List[Day]

@dataclass
class Player():
    name: str
    played_days: Days
