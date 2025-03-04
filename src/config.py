from src.logger import logger
from src.env_loader import get_env

# Configuration centralisée
def get_config(param, default=None):
    return get_env(param, default)

# Exemple d'utilisation
if __name__ == "__main__":
    logger.info("Configuration chargée avec succès.")
    logger.info(f"LangChain Version: {get_config('LANGCHAIN_VERSION', 'Non spécifiée')}")
