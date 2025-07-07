from agents import Tool

class InjurySupportAgent(Tool):
    name = "InjurySupportAgent"
    instructions = """
    You are an injury support specialist agent.
    Help users with physical limitations, injuries, and modified workout plans.
    Always prioritize safety and recommend consulting healthcare providers.
    Provide alternative exercises and rehabilitation-focused routines.
    """

    async def __call__(self, user_input, context):
        if hasattr(context, "handoff_logs"):
            context.handoff_logs.append("Injury support agent engaged.")
        return (
            "You're dealing with an injury—safety comes first! "
            "I recommend gentle mobility exercises and avoiding strain. "
            "Always consult a physical therapist if pain persists."
        )
