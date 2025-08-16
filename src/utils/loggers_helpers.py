import json
from functools import wraps
import inspect
import logging
logger = logging.getLogger(__name__)

def log_request_response(url, response, headers=None, payload=None, params=None):
    """
    INFO: IP Address o dominio
    DEBUG: Request URL + Headers
    DEBUG: Payloads (datos enviados en el request)
    INFO: Status Code
    DEBUG: Response (body o json de respuesta)
    """
    log_stack_path()
    logger.info("DOMAIN: %s", url.split("/")[2])
    logger.debug("REQUEST URL: %s", url)
    logger.info("STATUS CODE: %s", response.status_code)
    if headers:
        logger.debug("REQUEST HEADERS:\n%s", json.dumps(headers, indent=4, ensure_ascii=False))

    if payload:
        logger.debug("PAYLOAD REQUEST:\n%s", json.dumps(payload, indent=4, ensure_ascii=False))

    if params:
        logger.debug("PARAMS REQUEST:\n%s", json.dumps(params, indent=4, ensure_ascii=False))

    try:
        logger.debug("RESPONSE JSON:\n%s", json.dumps(response.json(), indent=4, ensure_ascii=False))
    except Exception:
        logger.debug("RESPONSE TEXT:\n%s", response.text)

def log_stack_path():
    """
    Registra en los logs el path de funciones desde el frame 0 al 4 del stack de llamadas.

    INFO:
        Permite ver el flujo de ejecución de las funciones hasta cinco niveles,
        mostrando qué función llamó a cuál, lo que ayuda a depuración y trazabilidad.

    Ejemplo de salida:
        FUNCTION PATH: func0 -> func1 -> func2 -> func3 -> func4
    """
    stack = inspect.stack()
    # Tomar los primeros 5 frames o menos si el stack es más pequeño
    max_level = min(5, len(stack))
    path = " -> ".join(stack[i].function for i in range(max_level))
    logger.debug("FUNCTION PATH: %s", path)

def log_response(func):
    """
    Decorador que logea la respuesta de un método API.
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        response = func(self, *args, **kwargs)
        url = getattr(self, 'base_url', None)  # obtenemos la URL de la instancia
        # Usamos specific_header si se pasó, sino el header por defecto
        specific_header = kwargs.get('specific_header')
        headers_to_log = specific_header if specific_header is not None else getattr(self, 'header', None)

        log_request_response(url, response,
                             payload=kwargs.get('payload'),
                             params=kwargs.get('params'),
                             headers=headers_to_log
                             )
        return response
    return wrapper

