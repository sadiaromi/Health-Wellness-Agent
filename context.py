from typing import Optional, List, Dict
from pydantic import BaseModel

class UserSessionContext(BaseModel):
    """
    Holds user-specific session data for tracking progress, goals, and preferences.
    This is shared across tools and agents.
    """
    name: str
    uid: int
    goal: Optional[dict] = None
    diet_preferences: Optional[str] = None
    workout_plan: Optional[dict] = None
    meal_plan: Optional[List[str]] = None
    injury_notes: Optional[str] = None
    handoff_logs: List[str] = []
    progress_logs: List[Dict[str, str]] = []
