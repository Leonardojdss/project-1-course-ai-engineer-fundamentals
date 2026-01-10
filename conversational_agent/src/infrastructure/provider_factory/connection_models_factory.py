from src.infrastructure.provider_factory.openai import ConnectOpenAI
from src.infrastructure.provider_factory.ollama import ConnectOllama

class ConnectionModelFactory:
    @staticmethod
    def create_connection_model(type):
        if type == "openai":
            return ConnectOpenAI()
        elif type == "ollama":
            return ConnectOllama()
        else:
            raise ValueError(f"type of provider '{type}' not supported")