from agents import InputGuardrail, OutputGuardrail
import re

class GoalValidationError(Exception):
    pass

# ----------------- Input Validation Functions -----------------
def validate_goal_input(input_text: str) -> bool:
    """Ensure goal input contains quantity, metric, and duration."""
    if not input_text or len(input_text.strip()) < 5:
        return False
    has_number = bool(re.search(r'\d+', input_text))
    has_unit = bool(re.search(r'(kg|lbs?|pounds?|weeks?|months?|days?)', input_text.lower()))
    return has_number and has_unit

def validate_dietary_input(input_text: str) -> bool:
    """Validate dietary preference keywords."""
    valid_diets = ['vegetarian', 'vegan', 'keto', 'paleo', 'mediterranean', 'omnivore', 'none']
    return any(diet in input_text.lower() for diet in valid_diets)

# ----------------- Input Guardrails -----------------
input_guardrails = [
    InputGuardrail(
        name="goal_validation",
        condition=lambda x: "goal" in x.lower() or "lose" in x.lower() or "gain" in x.lower(),
        action=lambda x: x if validate_goal_input(x)
        else "Please provide a specific goal with quantity and timeframe (e.g., 'lose 5kg in 2 months')"
    )
]

# ----------------- Output Guardrails -----------------
def validate_structured_output(output):
    """Ensure tool outputs are structured as dictionaries."""
    if isinstance(output, dict):
        return output
    elif hasattr(output, 'dict'):
        return output.dict()
    return {"content": str(output), "validated": True}

output_guardrails = [
    OutputGuardrail(
        name="structure_validation",
        condition=lambda x: True,
        action=validate_structured_output
    )
]
