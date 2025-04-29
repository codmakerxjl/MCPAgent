import os
from contextlib import asynccontextmanager
from agents.mcp import MCPServerStdio
from configs.config_manager import ConfigManager
from typing import AsyncIterator, List

class MCPServerManager:
    def __init__(self, config: ConfigManager):
        self._config = config
        self._servers_config = config.mcp_config  # Directly get the server config list
        
        # Keep the original validation logic (execute for each server)
        for server_cfg in self._servers_config:
            if 'files_path' in server_cfg:
                self._validate_sample_files(server_cfg)

    def _validate_sample_files(self, server_cfg: dict):
        """Create the directory for each server with sample_files_path"""
        if 'sample_files_path' in server_cfg:
            sample_dir = server_cfg["sample_files_path"]
            if not os.path.exists(sample_dir):
                os.makedirs(sample_dir, exist_ok=True)
                print(f"Created sample directory at {sample_dir}")

    @asynccontextmanager
    async def start_server(self) -> AsyncIterator[List[MCPServerStdio]]:
        servers = []
        try:
            for server_cfg in self._servers_config:
                # Create server instance and connect manually
                server = MCPServerStdio(
                    name=server_cfg["name"],
                    params={
                        "command": server_cfg["command"],
                        "args": server_cfg["args"]
                    }
                )
                await server.connect()  # Explicitly call the connect method
                servers.append(server)
                print(f"✅ Connected to server: {server_cfg['name']}")
                
            yield servers
        finally:
            # Ensure all connections are closed
            for server in servers:
                await server.disconnect()
                print(f"⛔ Disconnected from server: {server.name}")