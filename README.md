# 🧠 Health & Wellness Planner Agent

An AI-powered assistant built using the **OpenAI-compatible Agents SDK**.  
This agent helps users plan their fitness and diet goals, generate personalized meal/workout plans, track progress, and escalate to specialized agents — all through a **Streamlit web app**.

# 📁 Folder Structure
```

health/
├── agent_config.py # Main agent logic (tool selection, routing)
├── context.py # User session state (goal, diet, progress)
├── streamlit_app.py # Streamlit frontend with PDF export
├── .env # API key stored here
├── guardrail.py # Input/output validation
├── hooks.py # Lifecycle event logging

├── agents/
│ ├── escalation_agent.py # Escalate to human
│ ├── injury_support.py # Injury-related support agent
│ ├── nutrition_expert.py # Dietary restrictions expert

├── shared/
│ ├── goal_analyzer.py # Parses goals like "lose 5kg in 2 months"
│ ├── meal_planner.py # Generates weekly meal plan
│ ├── workout_recommender.py # Suggests workouts based on goal
│ ├── scheduler.py # Schedules weekly check-ins
│ └── tracker.py # Tracks progress updates


```
---

# 🛠 Setup & Run the App

## 🔹 Step 1: Create & Activate Virtual Environment

uv venv
# For Windows
.\venv\Scripts\activate


## 🔹 Step 2: Add Your API Key to .env File


OPENAI_API_KEY=your-api-key-here


## 🔹 Step 3: Run the Streamlit App


streamlit run streamlit_app.py


---

# 🚀 Features

- 💬 Health-related conversation
- 🔄 Dynamic responses from tools/agents
- 📄 Option to export response as a PDF

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

- 🧰 *User*: I want to lose 5kg in 2 months  
      *Tool Used*: GoalAnalyzerTool structures the goal  

- 🧰 *User*: I   m vegetarian  
     *Tool Used*: MealPlannerTool provides a 7-day meal plan  

- 🧠 *User*: I have back pain  
    *Agent Triggered*: InjurySupportAgent responds  

- 🧠 *User*: I want a real coach  
      *Agent Triggered*: EscalationAgent connects to a human  



---

# 📌 Final Notes

- Uses any OpenAI-compatible SDK (e.g., OpenRouter)  
- Frontend: Streamlit only  
- Simple, modular, and production-ready
