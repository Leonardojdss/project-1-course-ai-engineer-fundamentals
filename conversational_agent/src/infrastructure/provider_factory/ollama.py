from src.infrastructure.provider_factory.connection_models import ConnectionModelNaturalLanguage

class ConnectOllama(ConnectionModelNaturalLanguage):

    def connection(self):
        print("Connecting to Ollama.")