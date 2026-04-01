"""测试高德地图MCP客户端"""

import sys
import os

# 添加项目路径到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.agents.mcp_client import test_mcp_client

if __name__ == "__main__":
    print("🧪 开始测试高德地图MCP客户端...")
    
    # 设置测试环境变量（如果没有配置）
    if not os.getenv("AMAP_API_KEY"):
        print("⚠️  未检测到高德地图API密钥，将使用默认工具集进行测试")
        # 设置一个测试密钥（实际使用时需要替换为真实密钥）
        os.environ["AMAP_API_KEY"] = "test_key"
    
    # 运行测试
    success = test_mcp_client()
    
    if success:
        print("✅ MCP客户端测试完成")
    else:
        print("❌ MCP客户端测试失败")
        
    print("\n📝 使用说明:")
    print("1. 在.env文件中设置AMAP_API_KEY=你的高德地图API密钥")
    print("2. 确保已安装amap-mcp-server: uvx amap-mcp-server")
    print("3. 重新运行测试以验证连接")