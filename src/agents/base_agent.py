import uuid
import logging
from src.logger import logger

class BaseAgent:
    def __init__(self, name: str, config: dict = None):
        """Initialisation de l'agent générique."""
        self.id = str(uuid.uuid4())  # Identifiant unique pour l'agent
        self.name = name
        self.config = config if config else {}
        logger.info(f"🛠 Agent '{self.name}' créé avec ID {self.id}")

    def run(self, *args, **kwargs):
        """Méthode à surcharger dans les sous-classes."""
        raise NotImplementedError("La méthode 'run()' doit être implémentée par les sous-classes.")

# Test de l'agent
if __name__ == "__main__":
    agent = BaseAgent("TestAgent")
    logger.info(f"Agent de test : {agent.name}, ID : {agent.id}")
