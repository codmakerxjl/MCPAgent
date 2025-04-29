# interact/interactive_session.py
import asyncio
from utils.logger import Logger
from agents.run import Runner
from agents.lifecycle import RunHooks

class InteractiveSession:
    def __init__(self, agent_manager):
        self.agent_manager = agent_manager

    class TracingHooks(RunHooks):
        def __init__(self, parent):
            self.parent = parent  
            
        async def on_agent_start(self, context, agent):
            Logger.agent_start(agent.name)

        async def on_tool_start(self, context, agent, tool):
            Logger.tool_call(tool.name)

        async def on_tool_end(self, context, agent, tool, result):
            Logger.tool_result(tool.name, result)

        async def on_handoff(self, context, from_agent, to_agent):
            Logger.handoff(from_agent.name, to_agent.name)

    async def start(self):
        tracing_hooks = self.TracingHooks(self)
        Logger.info("File assistant is running! Enter your question (type 'quit' to exit)")
        
        while True:
            try:
                user_input = await asyncio.get_event_loop().run_in_executor(
                    None, 
                    lambda: input("\n\033[1;34mYou:\033[0m ")
                )
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    Logger.warn("Exiting...")
                    break
                    
                Logger.request(user_input)

                # Process the request
                Logger.thinking()
                result = await Runner.run(
                    starting_agent=self.agent_manager.agent,
                    input=user_input,
                    max_turns=50,
                    hooks=tracing_hooks
                )

                # Print the response (with cyan highlight)
                Logger.response(result.final_output)

            except (KeyboardInterrupt, asyncio.CancelledError):
                Logger.interrupt()
                break
            except Exception as e:
                Logger.error(f"An error occurred while processing the request: {str(e)}")
                if 'user_input' in locals():
                    Logger.error(f"Request content with error: {user_input}")