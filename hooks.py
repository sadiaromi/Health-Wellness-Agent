from agents import RunHooks
from datetime import datetime

def create_run_hooks():
    def on_agent_start(agent_name, context):
        pass  

    def on_agent_end(agent_name, context):
        pass  

    def on_tool_start(tool_name, context):
        pass  

    def on_tool_end(tool_name, result, context):
        pass  
    def on_handoff(from_agent, to_agent, context):
       
        context.handoff_logs.append(
            f"Handoff from {from_agent} to {to_agent} at {datetime.now()}"
        )

    return RunHooks(
        on_agent_start=on_agent_start,
        on_agent_end=on_agent_end,
        on_tool_start=on_tool_start,
        on_tool_end=on_tool_end,
        on_handoff=on_handoff
    )
