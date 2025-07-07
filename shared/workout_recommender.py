from agents import Tool
from pydantic import BaseModel
from typing import Dict, List

class WorkoutInput(BaseModel):
    goal_type: str
    experience_level: str = "beginner"
    available_days: int = 3

class WorkoutOutput(BaseModel):
    workout_plan: Dict[str, List[str]]
    duration_per_session: int

class WorkoutRecommenderTool(Tool):
    name = "workout_recommender"
    description = "Recommends workout plans based on goals and experience"
    
    def run(self, input_data: WorkoutInput, context) -> WorkoutOutput:
        goal_type = input_data.goal_type
        experience = input_data.experience_level
        days = input_data.available_days

        # Workout templates by goal
        if goal_type == "weight_loss":
            workouts = {
                "Day 1": ["30 min cardio", "Bodyweight squats 3x15", "Push-ups 3x10"],
                "Day 2": ["HIIT training 20 min", "Planks 3x30s", "Burpees 3x8"],
                "Day 3": ["Walking/Jogging 45 min", "Lunges 3x12", "Mountain climbers 3x15"]
            }
            duration = 45

        elif goal_type == "weight_gain":
            workouts = {
                "Day 1": ["Squats 4x8", "Deadlifts 4x6", "Bench press 4x8"],
                "Day 2": ["Pull-ups 4x6", "Rows 4x8", "Overhead press 4x8"],
                "Day 3": ["Leg press 4x10", "Dips 4x8", "Bicep curls 3x12"]
            }
            duration = 60

        else:  # maintenance/general fitness
            workouts = {
                "Day 1": ["Full body circuit", "Cardio 20 min", "Stretching 10 min"],
                "Day 2": ["Strength training", "Core work", "Flexibility"],
                "Day 3": ["Active recovery", "Light cardio", "Yoga"]
            }
            duration = 50

        # Trim based on available days
        if days < 3:
            workouts = {k: v for i, (k, v) in enumerate(workouts.items()) if i < days}

        # Save plan to context for future use
        context.workout_plan = {
            "plan": workouts,
            "duration": duration,
            "goal": goal_type
        }

        return WorkoutOutput(
            workout_plan=workouts,
            duration_per_session=duration
        )
