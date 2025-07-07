from agents import Tool
from pydantic import BaseModel
from typing import List
import asyncio

class MealPlanInput(BaseModel):
    dietary_preferences: str
    goal_type: str

class MealPlanOutput(BaseModel):
    meal_plan: List[str]
    calories_per_day: int

class MealPlannerTool(Tool):
    name = "meal_planner"
    description = "Creates a 7-day meal plan based on dietary preferences and goals"
    
    async def run(self, input_data: MealPlanInput, context) -> MealPlanOutput:
        await asyncio.sleep(1)  # Simulated delay for async behavior
        
        dietary_prefs = input_data.dietary_preferences.lower()
        goal_type = input_data.goal_type.lower()

        # Select base meals
        if "vegetarian" in dietary_prefs:
            base_meals = [
                "Breakfast: Oatmeal with berries and nuts",
                "Lunch: Quinoa salad with vegetables",
                "Dinner: Lentil curry with brown rice",
                "Snack: Greek yogurt with fruits"
            ]
        elif "vegan" in dietary_prefs:
            base_meals = [
                "Breakfast: Smoothie bowl with plant protein",
                "Lunch: Buddha bowl with tofu",
                "Dinner: Chickpea stir-fry with vegetables",
                "Snack: Nuts and seeds mix"
            ]
        else:
            base_meals = [
                "Breakfast: Eggs with whole grain toast",
                "Lunch: Grilled chicken salad",
                "Dinner: Salmon with quinoa and vegetables",
                "Snack: Protein shake"
            ]

        # Adjust calories based on goal
        if goal_type == "weight_loss":
            calories = 1800
        elif goal_type == "weight_gain":
            calories = 2400
        else:
            calories = 2000

        # Build a 7-day plan
        meal_plan = [
            f"Day {day}: {', '.join(base_meals)}" for day in range(1, 8)
        ]

        # Store in context safely
        if hasattr(context, "meal_plan"):
            context.meal_plan = meal_plan
        if hasattr(context, "diet_preferences"):
            context.diet_preferences = input_data.dietary_preferences

        return MealPlanOutput(
            meal_plan=meal_plan,
            calories_per_day=calories
        )
