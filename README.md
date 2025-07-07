# 🧠 Health & Wellness Planner Agent

An AI-powered assistant built using the **OpenAI-compatible Agents SDK**.  
This agent helps users plan their fitness and diet goals, generate personalized meal/workout plans, track progress, and escalate to specialized agents — all through a **Streamlit web app**.

# 📁 Folder Structure


healthy/
â”‚
â”œâ”€â”€ agent_config.py       # Main agent logic (tool selection, routing)
â”œâ”€â”€ context.py            # User session state (goal, diet, progress)
â”œâ”€â”€ streamlit_app.py      # Streamlit frontend with PDF export
â”œâ”€â”€ .env                  # API key stored here
â”‚
â”œâ”€â”€ agents/
â”‚   â”œâ”€â”€ escalation_agent.py    # Escalate to human
â”‚   â”œâ”€â”€ injury_support.py      # Injury-related support agent
â”‚   â”œâ”€â”€ nutrition_expert.py    # Dietary restrictions expert
â”‚
â”œâ”€â”€ shared/
â”‚   â”œâ”€â”€ goal_analyzer.py       # Parses goals like "lose 5kg in 2 months"
â”‚   â”œâ”€â”€ meal_planner.py        # Generates weekly meal plan
â”‚   â”œâ”€â”€ workout_recommender.py # Suggests workouts based on goal
â”‚   â”œâ”€â”€ scheduler.py           # Schedules weekly check-ins
â”‚   â”œâ”€â”€ tracker.py             # Tracks progress updates
â”‚
â”œâ”€â”€ tools/
â”‚   â”œâ”€â”€ tool.py                # Base Tool class
â”‚
â”œâ”€â”€ guardrail.py              # Input/output validation
â”œâ”€â”€ hooks.py                  # Lifecycle event logging


---

# 🛠 Setup & Run the App

## 🔹 Step 1: Create & Activate Virtual Environment

bash
# For Windows
.\venv\Scripts\activate


## 🔹 Step 2: Add Your API Key to .env File

env
OPENAI_API_KEY=your-api-key-here


## 🔹 Step 3: Run the Streamlit App

bash
streamlit run streamlit_app.py


---

# 🚀 Features

💬 Health-related conversation
🔄 Dynamic responses from tools/agents
📄 Option to export response as a PDF

---

# 🤖 Agent Features

## 🧩 Tools

| Tool Name              | Function                                                |
|------------------------|---------------------------------------------------------|
| GoalAnalyzerTool       | Understands goals like "lose 5kg in 2 months"           |
| MealPlannerTool        | Creates meal plans based on dietary preferences         |
| WorkoutRecommenderTool | Suggests exercise routines                              |
| CheckinSchedulerTool   | Sets check-in reminders                                 |
| ProgressTrackerTool    | Logs user progress                                      |

---

## 🧠 Specialized Agents

| Agent Name            | Trigger                                                 |
|-----------------------|----------------------------------------------------------|
| NutritionExpertAgent  | User mentions diabetes, allergies, special diets         |
| InjurySupportAgent    | User mentions pain or injury                             |
| EscalationAgent       | User requests human help                                 |

---

# ✅ Guardrails

- InputGuardrails: Validate goal format  
- OutputGuardrails: Ensure structured JSON output  

---

# 🔄 Lifecycle Hooks

- Log when agent/tool starts or ends  
- Monitor handoffs to expert agents  

---

# 💡 Example Conversation Flow

- *User*: I want to lose 5kg in 2 months  
  â†’ *Tool Used*: GoalAnalyzerTool structures the goal  

- *User*: Iâ€™m vegetarian  
  â†’ *Tool Used*: MealPlannerTool provides a 7-day meal plan  

- *User*: I have back pain  
  â†’ *Agent Triggered*: InjurySupportAgent responds  

- *User*: I want a real coach  
  â†’ *Agent Triggered*: EscalationAgent connects to a human  



---

# 📌 Final Notes

- Uses any OpenAI-compatible SDK (e.g., OpenRouter)  
- Frontend: Streamlit only  
- Simple, modular, and production-ready
