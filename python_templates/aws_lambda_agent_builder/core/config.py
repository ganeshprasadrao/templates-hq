"""
Configuration settings for the LLM agent system.

This file defines the application settings using Pydantic BaseSettings,
providing type-safe configuration management with environment variable
support. Settings are cached using lru_cache for performance.

Common use cases:
- LLM model configuration
- API metadata configuration
- Agent behavior settings
- Environment-specific configurations
- Logging settings

Override settings by creating a .env file or setting environment variables.
"""

from pydantic_settings import BaseSettings
from typing import Optional
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings"""

    # OpenAI Configuration
    OPENAI_API_KEY: str
    MODEL_NAME: str = "gpt-4-turbo-preview"
    TEMPERATURE: float = 0.7
    STREAMING: bool = False

    # API Configuration
    API_TITLE: str = "AI Agent API"
    API_DESCRIPTION: str = (
        "API for interacting with an AI agent powered by LangChain and LangGraph"
    )
    API_VERSION: str = "1.0.0"

    # Logging Configuration
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()
