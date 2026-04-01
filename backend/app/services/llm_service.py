"""LLM服务模块"""

from langchain_openai import ChatOpenAI
from ..config import get_settings
from langchain.chat_models import init_chat_model
from langchain_deepseek import ChatDeepSeek
from langchain_core.language_models import BaseChatModel

# 全局LLM实例
_llm_instance = None


def get_llm() -> BaseChatModel:
    """
    获取LLM实例(单例模式)
    
    Returns:
        HelloAgentsLLM实例
    """
    global _llm_instance
    
    if _llm_instance is None:
        settings = get_settings()
        
        # HelloAgentsLLM会自动从环境变量读取配置
        # 包括OPENAI_API_KEY, OPENAI_BASE_URL, OPENAI_MODEL等
        # _llm_instance = init_chat_model(
        #     model=settings.openai_model,
        #     model_provider="openai",
        # )
        

        _llm_instance = ChatDeepSeek(
            model="deepseek-chat",
            temperature=0.5,
            max_tokens=4096,
            timeout=120,
            max_retries =3,
        )
        
        print(f"✅ LLM服务初始化成功")
        # print(f"   提供商: {_llm_instance.provider}")
        # print(f"   模型: {_llm_instance.model}")
    
    return _llm_instance


def reset_llm():
    """重置LLM实例(用于测试或重新配置)"""
    global _llm_instance
    _llm_instance = None

