from openai import AsyncOpenAI
from configs.config_manager import ConfigManager
from agents.lifecycle import RunHooks
from utils.logger import Logger
import asyncio
from agents import  Runner
class OpenAIClient:
    def __init__(self, config: ConfigManager):
        self._config = config
        self.client = self._initialize_client()

    def _initialize_client(self) -> AsyncOpenAI:
        return AsyncOpenAI(
            base_url=self._config.openai_config["BASE_URL"],
            api_key=self._config.openai_config["API_KEY"]
        )

    @property
    def model_name(self) -> str:
        return self._config.openai_config["MODEL_NAME"]

