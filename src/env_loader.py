import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

def get_env(param, default=None):
    """ Récupère une variable d'environnement avec une valeur par défaut. """
    return os.getenv(param, default)

# Exemple d'utilisation
if __name__ == "__main__":
    print(f"LangChain Version: {get_env('LANGCHAIN_VERSION', 'Non spécifiée')}")
