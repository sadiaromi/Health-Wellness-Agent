from agents import Tool

class NutritionExpertAgent(Tool):
    name = "NutritionExpertAgent"
    instructions = """
    You are a specialized nutrition expert agent.
    Handle complex dietary needs including diabetes, allergies, and specific medical conditions.
    Provide detailed nutritional guidance and meal modifications.
    Always recommend consulting with healthcare providers for medical conditions.
    """

    async def __call__(self, user_input, context):
        if hasattr(context, "handoff_logs"):
            context.handoff_logs.append("Nutrition expert engaged.")
        return (
            "As a nutrition expert, here's how I can help: "
            "Based on your dietary needs, I suggest adjustments like avoiding processed foods, "
            "focusing on whole grains, and maintaining a balanced intake. "
            "Please consult your doctor for medical advice."
        )
