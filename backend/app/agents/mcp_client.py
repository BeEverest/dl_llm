import asyncio
from typing import List, Any
from langchain_mcp_adapters.client import MultiServerMCPClient
from ..config import get_settings

class AmapMCPClient:
    """高德地图 MCP 客户端封装"""
    
    def __init__(self):
        self.settings = get_settings()
        self.mcp_client = None
        self._tools = None
        
    async def initialize(self) -> None:
        """异步初始化 MCP 客户端"""
        if self.mcp_client is not None:
            return
            
        print("🔄 初始化高德地图 MCP 客户端...")
        import os
        env = os.environ.copy()
        if self.settings.amap_api_key:
            env["AMAP_MAPS_API_KEY"] = self.settings.amap_api_key
            
        server_config = {
            "amap": {
                "transport": "stdio",
                "command": "uvx",
                "args": ["amap-mcp-server"],
                "env": env
            }
        }
        self.mcp_client = MultiServerMCPClient(server_config)
        self._tools = await self.mcp_client.get_tools()
        print("✅ 高德地图 MCP 客户端初始化成功")
        
    async def get_tools(self) -> List[Any]:
        """获取 MCP 提供的工具列表"""
        if self._tools is None:
            await self.initialize()
        return self._tools

# 全局单例
_amap_mcp_client = None

def get_amap_mcp_client() -> AmapMCPClient:
    """获取高德 MCP 客户端实例(单例)"""
    global _amap_mcp_client
    if _amap_mcp_client is None:
        _amap_mcp_client = AmapMCPClient()
    return _amap_mcp_client
