import json
import os
from pathlib import Path
from typing import Dict, Any

class ConfigManager:
    def __init__(self, config_path: str = "configs/config.json"):
        self.config = self._load_config(config_path)
        self._validate_config()
        self._convert_legacy_format()  # 【新增】兼容旧格式转换
        




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
                # 【新增】验证 MCP_SERVER 为列表且包含必要字段
        if not isinstance(self.config["MCP_SERVER"], list):
            raise TypeError("MCP_SERVER 必须为列表类型")
            
        for server in self.config["MCP_SERVER"]:
            required = ['name', 'command', 'args']
            missing = [field for field in required if field not in server]
            if missing:
                raise ValueError(f"服务器配置 {server.get('name')} 缺失字段: {missing}")
            
    def _convert_legacy_format(self):
        """【新增】兼容旧版单服务器配置格式"""
        if isinstance(self.config["MCP_SERVER"], dict):
            self.config["MCP_SERVER"] = [self.config["MCP_SERVER"]]

    @property
    def mcp_config(self) -> list:  # 【修改】返回类型调整为列表
        return self.config["MCP_SERVER"]

    @property
    def openai_config(self) -> Dict[str, str]:
        return self.config["OPENAI_CONFIG"]



    @property
    def agent_config(self) -> Dict[str, str]:
        return self.config["AGENT_CONFIG"]