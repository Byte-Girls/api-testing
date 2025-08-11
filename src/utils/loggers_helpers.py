import logging
import json

logger = logging.getLogger(__name__)

def log_request_response(url, response, headers=None, payload=None):
    """
    INFO: IP Address o dominio
    DEBUG: Request URL + Headers
    DEBUG: Payloads (datos enviados en el request)
    INFO: Status Code
    DEBUG: Response (body o json de respuesta)
    """
    logger.info("DOMAIN: %s", url.split("/")[2])
    logger.debug("REQUEST URL: %s", url)
    logger.info("STATUS CODE: %s", response.status_code)

    if headers:
        logger.debug("REQUEST HEADERS:\n%s", json.dumps(headers, indent=4, ensure_ascii=False))

    if payload:
        logger.debug("PAYLOAD REQUEST:\n%s", json.dumps(payload, indent=4, ensure_ascii=False))

    logger.debug("RESPONSE:\n%s", json.dumps(response.json(), indent=4, ensure_ascii=False))
    logger.debug("RESPONSE TEXT:\n%s", json.dumps(response.text, indent=4, ensure_ascii=False))

