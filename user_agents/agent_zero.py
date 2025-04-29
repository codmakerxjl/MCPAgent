
from agents import Agent, OpenAIChatCompletionsModel
from configs.config_manager import ConfigManager
from clients.openai_client import OpenAIClient

class AgentZeroManager:
    def __init__(self, config: ConfigManager, openai_client: OpenAIClient):
        self._config = config
        self._openai_client = openai_client
        self.agent = self._initialize_agent()

    def _initialize_agent(self) -> Agent:
        return Agent(
            name=self._config.agent_config["name"],
            instructions=self._config.agent_config["instructions"],
            model=OpenAIChatCompletionsModel(
                model=self._openai_client.model_name,
                openai_client=self._openai_client.client
            )
        )
    

