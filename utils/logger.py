import logging

# Configuración del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def log_error(message):
    """Registra un mensaje de error en el logger."""
    logger.error(message)

def log_info(message):
    """Registra un mensaje informativo en el logger."""
    logger.info(message)
