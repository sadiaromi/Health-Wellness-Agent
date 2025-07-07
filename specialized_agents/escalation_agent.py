from agents import Tool

class EscalationAgent(Tool):
    name = "EscalationAgent"
    instructions = """
    You are an escalation agent that connects users with human coaches.
    When users request to speak with a human trainer or coach, provide them with contact information and next steps.
    Be professional and helpful in facilitating this handoff.
    """

    async def __call__(self, user_input, context):
        if hasattr(context, "handoff_logs"):
            context.handoff_logs.append("Escalated to human coach.")
        return (
            "I'm connecting you to one of our certified human coaches. "
            "Please expect a follow-up within 24 hours via your registered contact method."
        )
