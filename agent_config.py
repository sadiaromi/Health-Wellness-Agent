import os
import re
from openai import OpenAI
from context import UserSessionContext
# Tools
from shared.goal_analyzer import GoalAnalyzerTool, GoalInput
from shared.meal_planner import MealPlannerTool, MealPlanInput
from shared.workout_recommender import WorkoutRecommenderTool, WorkoutInput
from shared.scheduler import CheckinSchedulerTool, SchedulerInput
from shared.tracker import ProgressTrackerTool, TrackerInput
# Specialized Agents
from specialized_agents.escalation_agent import EscalationAgent
from specialized_agents.nutrition_expert import NutritionExpertAgent
from specialized_agents.injury_support import InjurySupportAgent

class HealthWellnessAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.context = UserSessionContext(name="User", uid=1)

        # Tools
        self.goal_tool = GoalAnalyzerTool()
        self.meal_tool = MealPlannerTool()
        self.workout_tool = WorkoutRecommenderTool()
        self.schedule_tool = CheckinSchedulerTool()
        self.tracker_tool = ProgressTrackerTool()

        # Agents
        self.nutrition_agent = NutritionExpertAgent()
        self.injury_agent = InjurySupportAgent()
        self.escalation_agent = EscalationAgent()

    async def run(self, user_input: str) -> str:
        text = user_input.lower()

        try:
            if any(word in text for word in ['goal', 'lose', 'gain', 'target']):
                result = self.goal_tool.run(GoalInput(goal_text=user_input), self.context)
                return f"""🎯 **GOAL ANALYSIS**
**Target:** {result.goal_type.replace('_', ' ').title()}
**Amount:** {result.quantity}{result.metric} in {result.duration}
**Strategy:** {'Calorie deficit + cardio' if 'lose' in text else 'Protein + strength training'}
**Timeline:** {'0.5-1kg/week safe' if 'lose' in text else '0.25-0.5kg/week healthy'}
**Success Tips:** Stay consistent, track progress, be patient! 💪"""

            elif any(word in text for word in ['nutrition', 'vitamin', 'cholesterol', 'diabetic']):
                result = await self.nutrition_agent(user_input, self.context)
                return f"""🩺 **NUTRITION EXPERT**
**Specialist Advice:** {result[:150]}...
**Medical Note:** Always consult your doctor
**Follow-up:** Regular health checkups
**Safety First:** Professional guidance recommended! 👨‍⚕️"""

            elif any(word in text for word in ['meal', 'diet', 'food', 'eat']):
                goal_type = self.context.goal.get('type', 'general') if self.context.goal else 'general'
                result = await self.meal_tool.run(
                    MealPlanInput(dietary_preferences=user_input, goal_type=goal_type),
                    self.context
                )
                return f"""🥗 **MEAL PLAN READY**
**Duration:** 7 days complete plan
**Calories:** {result.calories_per_day} per day
**Type:** {'Vegetarian' if 'vegetarian' in text else 'High-protein' if 'protein' in text else 'Balanced'}
**Key Foods:** {'Dal, paneer, quinoa' if 'vegetarian' in text else 'Chicken, fish, eggs' if 'protein' in text else 'All food groups'}
**Timing:** Eat every 3-4 hours for best results! 🍽️"""

            elif any(word in text for word in ['workout', 'exercise', 'gym']):
                goal_type = self.context.goal.get('type', 'general') if self.context.goal else 'general'
                result = self.workout_tool.run(WorkoutInput(goal_type=goal_type), self.context)
                return f"""💪 **WORKOUT PLAN**
**Duration:** {result.duration_per_session} minutes per session
**Frequency:** {len(result.workout_plan)} days per week
**Focus:** {'Fat burning + cardio' if 'lose' in str(goal_type) else 'Strength + muscle building'}
**Type:** {'HIIT + core work' if 'belly' in text else 'Full body routine'}
**Progress:** Increase intensity weekly! 🏋️‍♂️"""

            elif any(word in text for word in ['schedule', 'reminder', 'check']):
                result = self.schedule_tool.run(SchedulerInput(frequency="weekly"), self.context)
                return f"""📅 **SCHEDULE SET**
**Next Check-in:** {result.next_checkin}
**Frequency:** Weekly progress reviews
**Reminders:** Daily workout & meal alerts
**Tracking:** Weight, measurements, energy
**Consistency:** Key to success! ⏰"""

            elif any(word in text for word in ['progress', 'lost', 'walked', 'track']):
                numbers = re.findall(r'\d+(?:\.\d+)?', user_input)
                value = float(numbers[0]) if numbers else None
                result = self.tracker_tool.run(
                    TrackerInput(progress_update=user_input, metric_value=value), self.context
                )
                return f"""📊 **PROGRESS LOGGED**
**Update:** {user_input}
**Status:** {result.encouragement_message}
**Next Goal:** {result.next_milestone}
**Total Logs:** {len(self.context.progress_logs)}
**Motivation:** Every step counts! 🌟"""

            elif any(word in text for word in ['injury', 'pain', 'hurt', 'knee', 'back']):
                result = await self.injury_agent(user_input, self.context)
                return f"""🛑 **INJURY SUPPORT**
**Care Instructions:** {result[:150]}...
**Safety:** Rest and proper treatment
**Recovery:** Follow professional guidance
**Warning:** See doctor if severe! 🏥"""

            elif any(word in text for word in ['human', 'coach', 'professional', 'help']):
                result = await self.escalation_agent(user_input, self.context)
                return f"""🤝 **PROFESSIONAL SUPPORT**
**Human Expert:** {result[:150]}...
**Available:** Certified trainers & nutritionists
**Platforms:** Online consultations ready
**Emergency:** Medical help when needed! 👨‍⚕️"""

        except Exception:
            pass

        return """🏥 **HEALTH GUIDANCE**
**Daily Basics:** Balanced diet, exercise, sleep  
**Prevention:** Regular checkups, stay active  
**Wellness:** Mental health equally important  
**Lifestyle:** Work-life balance essential  
**Questions:** Ask specific health concerns! 😊"""

def create_health_wellness_agent():
    return HealthWellnessAgent()
