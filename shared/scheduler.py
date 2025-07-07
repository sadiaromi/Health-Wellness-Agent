from agents import Tool
from pydantic import BaseModel
from datetime import datetime, timedelta

class SchedulerInput(BaseModel):
    frequency: str = "weekly"

class SchedulerOutput(BaseModel):
    next_checkin: str
    reminder_message: str

class CheckinSchedulerTool(Tool):
    name = "checkin_scheduler"
    description = "Schedules progress check-ins and reminders"
    
    def run(self, input_data: SchedulerInput, context) -> SchedulerOutput:
        now = datetime.now()

        # Determine the next check-in date
        if input_data.frequency == "weekly":
            next_checkin = now + timedelta(weeks=1)
        elif input_data.frequency == "daily":
            next_checkin = now + timedelta(days=1)
        else:
            next_checkin = now + timedelta(weeks=1)  # default fallback

        
        reminder_message = (
            f"Your next check-in is scheduled for "
            f"{next_checkin.strftime('%Y-%m-%d %H:%M')}. Keep up the great work!"
        )

        # return the output
        return SchedulerOutput(
            next_checkin=next_checkin.strftime('%Y-%m-%d %H:%M'),
            reminder_message=reminder_message
        )
