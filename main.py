import asyncio
from agents import  set_tracing_disabled
from configs.config_manager import ConfigManager
from clients.openai_client import OpenAIClient
from servers.mcp_server import MCPServerManager
from user_agents.agent_zero import AgentZeroManager
from user_interact.interactive_session import InteractiveSession
async def main():
    # initialize the configuration manager and disable tracing
    config = ConfigManager()
    set_tracing_disabled(disabled=True)

    # initialize the server manager, OpenAI client, agent manager, and interactive session
    server_manager = MCPServerManager(config)
    openai_client = OpenAIClient(config)
    agent_manager = AgentZeroManager(config, openai_client)
    interac_session = InteractiveSession(agent_manager)
    # start the server and agent manager

    
    async with server_manager.start_server() as servers:  # servers is a list of MCPServer instances
        agent_manager.agent.mcp_servers = servers  # directly assign the servers to the agent manager
        await interac_session.start()
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\033[1;33mExisting\033[0m")