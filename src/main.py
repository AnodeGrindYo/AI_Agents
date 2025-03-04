import logging
from src.logger import logger
from src.config import get_config
from src.pipelines.pipeline_basique import conversation

def initialize_agents():
    """ Initialisation des agents IA (à implémenter plus tard). """
    logger.info("📢 Initialisation des agents IA...")
    # TODO: Charger et initialiser les agents
    pass

def initialize_tools():
    """ Initialisation des outils (à implémenter plus tard). """
    logger.info("🛠 Initialisation des outils...")
    # TODO: Charger et initialiser les outils
    pass

def initialize_pipelines():
    """ Initialisation des pipelines IA. """
    logger.info("🔗 Initialisation des pipelines...")
    try:
        logger.info("🧠 Test du pipeline LangChain...")
        response = conversation.predict(input="Bonjour, qui es-tu ?")
        logger.info(f"💬 Réponse du LLM: {response}")
    except Exception as e:
        logger.error(f"❌ Erreur lors de l'initialisation du pipeline : {e}")

def main():
    logger.info("🔹 Démarrage du projet LangChain & CrewAI")
    
    # Vérification des variables d'environnement
    debug_mode = get_config("DEBUG_MODE", "False")
    logger.info(f"🔍 Mode Debug: {debug_mode}")

    # Initialisation des composants
    initialize_agents()
    initialize_tools()
    initialize_pipelines()

    logger.info("✅ Initialisation terminée. Projet prêt à être utilisé !")

if __name__ == "__main__":
    main()
