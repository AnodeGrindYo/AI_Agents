import logging

# Configuration des logs
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Création du logger
logger = logging.getLogger(__name__)

# Exemple d'utilisation
if __name__ == "__main__":
    logger.info("Logger initialisé avec succès.")
