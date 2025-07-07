from agents import Tool
from pydantic import BaseModel
from typing import Optional
import re

class GoalInput(BaseModel):
    goal_text: str

class GoalOutput(BaseModel):
    goal_type: str
    quantity: Optional[float] = None
    metric: Optional[str] = None
    duration: Optional[str] = None
    is_valid: bool

class GoalAnalyzerTool(Tool):
    name = "goal_analyzer"
    description = "Analyzes and structures user health goals"

    def run(self, input_data: GoalInput, context) -> GoalOutput:
        goal_text = input_data.goal_text.lower()

        # Step 1: Goal type detection
        if any(word in goal_text for word in ['gain', 'muscle', 'bulk']):
            goal_type = "weight_gain"
        elif any(word in goal_text for word in ['lose', 'fat', 'reduce']):
            goal_type = "weight_loss"
        elif any(word in goal_text for word in ['maintain', 'stay', 'keep']):
            goal_type = "maintenance"
        else:
            goal_type = "general_fitness"

        # Step 2: Extract quantity and metric
        quantity = None
        metric = None
        weight_match = re.search(r'(\d+(?:\.\d+)?)\s*(kg|lbs?|pounds?)', goal_text)
        if weight_match:
            quantity = float(weight_match.group(1))
            metric = weight_match.group(2)

        # Step 3: Extract duration
        duration = None
        duration_match = re.search(r'(\d+)\s*(weeks?|months?|days?)', goal_text)
        if duration_match:
            duration = f"{duration_match.group(1)} {duration_match.group(2)}"

        # Step 4: Update context
        if hasattr(context, "goal"):
            context.goal = {
                "type": goal_type,
                "quantity": quantity,
                "metric": metric,
                "duration": duration,
                "original_text": input_data.goal_text
            }

        # Step 5: Return structured goal output
        is_valid = (
            goal_type in ["weight_gain", "weight_loss", "maintenance"]
            and quantity is not None
            and metric is not None
            and duration is not None
        )

        return GoalOutput(
            goal_type=goal_type,
            quantity=quantity,
            metric=metric,
            duration=duration,
            is_valid=is_valid
        )
