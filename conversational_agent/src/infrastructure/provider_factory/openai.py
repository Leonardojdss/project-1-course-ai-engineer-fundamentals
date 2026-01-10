from openai import OpenAI
from src.infrastructure.provider_factory.connection_models import ConnectionModelNaturalLanguage

class ConnectOpenAI(ConnectionModelNaturalLanguage):

    def connection(self):
        print("Connecting to OpenAI.")