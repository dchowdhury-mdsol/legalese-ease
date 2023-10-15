import logging

# Reference: https://docs.python.org/3/library/logging.html

def setup_logging():
    """
    Configures and returns a logging object to output information with specified formatting.
    
    Returns:
    logging.Logger: The configured logger object.
    """
    
    # Basic configuration for logging: 
    # - Level set to INFO to capture essential runtime information.
    # - Formatting includes timestamp, log level, and message.
    logging.basicConfig(level=logging.INFO, 
                        format="%(asctime)s [%(levelname)s]: %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")
    
    # Retrieve and return logger instance
    logger = logging.getLogger()
    return logger

