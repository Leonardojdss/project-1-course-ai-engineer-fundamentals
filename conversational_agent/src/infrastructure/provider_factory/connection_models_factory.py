from src.infrastructure.provider_factory.openai import ConnectOpenAI
from src.infrastructure.provider_factory.ollama import ConnectOllama

class ConnectionModelFactory:
    provider = str
    
    @staticmethod
    def create_connection_model(provider: str):
        if provider == "openai":
            return ConnectOpenAI()
        elif provider == "ollama":
            return ConnectOllama()
        else:
            raise ValueError(f"type of provider '{provider}' not supported")