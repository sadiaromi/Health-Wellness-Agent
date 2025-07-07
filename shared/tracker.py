from agents import Tool
from pydantic import BaseModel
from typing import Dict
from datetime import datetime
import random

class TrackerInput(BaseModel):
    progress_update: str
    metric_value: float = None

class TrackerOutput(BaseModel):
    progress_recorded: bool
    encouragement_message: str
    next_milestone: str

class ProgressTrackerTool(Tool):
    name = "progress_tracker"
    description = "Tracks user progress and provides feedback"
    
    def run(self, input_data: TrackerInput, context) -> TrackerOutput:
        # Record progress into user context
        progress_entry = {
            "date": datetime.now().strftime('%Y-%m-%d'),
            "update": input_data.progress_update,
            "value": input_data.metric_value,
            "timestamp": datetime.now().isoformat()
        }
        context.progress_logs.append(progress_entry)
        
        # Generate a random motivational message
        encouragement = random.choice([
            "Great progress! Keep up the excellent work!",
            "You're doing amazing! Stay consistent!",
            "Fantastic effort! You're on the right track!",
            "Well done! Every step counts towards your goal!"
        ])
        
        # Determine next milestone based on user's goal
        if context.goal and context.goal.get('quantity'):
            target = context.goal['quantity']
            current = input_data.metric_value or 0
            remaining = abs(target - current)
            next_milestone = f"Keep going! {remaining:.1f} {context.goal.get('metric', 'units')} to go!"
        else:
            next_milestone = "Continue with your current routine!"
        
        return TrackerOutput(
            progress_recorded=True,
            encouragement_message=encouragement,
            next_milestone=next_milestone
        )
