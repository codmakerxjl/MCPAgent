import json
import os
from pathlib import Path
from typing import Dict, Any
from dotenv import load_dotenv
load_dotenv()
class ConfigManager:
    def __init__(self, config_path: str = "configs/config.json"):
        self.config = self._load_config(config_path)
        self._validate_config()
        self._convert_legacy_format()  # [NEW] Compatible with legacy format conversion

    def _load_config(self, path: str) -> Dict[str, Any]:
        config_path = Path(__file__).parent.parent / path
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise RuntimeError(f"Config file not found at {config_path}")
        except json.JSONDecodeError:
            raise RuntimeError("Invalid JSON format in config file")

    def _validate_config(self):
        required_sections = ["OPENAI_CONFIG", "MCP_SERVER", "AGENT_CONFIG"]
        for section in required_sections:
            if section not in self.config:
                raise ValueError(f"Missing required config section: {section}")
        # [NEW] Validate MCP_SERVER is a list and contains required fields
        if not isinstance(self.config["MCP_SERVER"], list):
            raise TypeError("MCP_SERVER must be a list type")
        for server in self.config["MCP_SERVER"]:
            required = ['name', 'command', 'args']
            missing = [field for field in required if field not in server]
            if missing:
                raise ValueError(f"Server config {server.get('name')} missing fields: {missing}")

    def _convert_legacy_format(self):
        """[NEW] Compatible with legacy single-server config format"""
        if isinstance(self.config["MCP_SERVER"], dict):
            self.config["MCP_SERVER"] = [self.config["MCP_SERVER"]]

    @property
    def mcp_config(self) -> list:  # [MOD] Return type changed to list
        return self.config["MCP_SERVER"]

    @property
    def openai_config(self) -> Dict[str, str]:
        # Copy the config and override API_KEY with env if present
        cfg = self.config["OPENAI_CONFIG"].copy()
        api_key = os.getenv("API_KEY")
        if api_key:
            cfg["API_KEY"] = api_key
        return cfg

    @property
    def agent_config(self) -> Dict[str, str]:
        return self.config["AGENT_CONFIG"]