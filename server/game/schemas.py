from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

# Country Schema
class DailyCountryBase(BaseModel):
    country_name: str

class DailyCountryDisplay(DailyCountryBase):
    id: int
    date: date
    
    class Config:
        from_attributes = True

class DailyCountryCreate(DailyCountryBase):
    class Config:
        from_attributes = True

# Question Schema
class QuestionBase(BaseModel):
    question: str
    answer: str

class QuestionCreate(QuestionBase):
    user_id: int
    country_id: int

class QuestionDisplay(QuestionBase):
    id: int
    asked_at: datetime

    class Config:
        from_attributes = True

# Guess Schema
class GuessBase(BaseModel):
    guess: str

class GuessCreate(GuessBase):
    country_id: int

class GuessDisplay(GuessBase):
    id: int
    guessed_at: datetime
    response: str
    
    class Config:
        from_attributes = True

# Daily Usage Schema
class DailyUsageBase(BaseModel):
    date: date
    questions_asked: int
    guesses_made: int

class DailyUsageCreate(DailyUsageBase):
    user_id: int

class DailyUsageDisplay(DailyUsageBase):
    id: int

    class Config:
        from_attributes = True
