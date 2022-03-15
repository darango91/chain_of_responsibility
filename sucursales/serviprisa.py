from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from sucursales.constans import NivelArea


class Handler(ABC):
    """
    La interfaz Handler declara un metodo para construir la cadena de handlers
    tambien declara un metodo para manejar la peticion
    """

    @abstractmethod
    def set_sucesor(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def entregar_envio(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    El comportamiento por defecto del encadenado (chaining) se puede
    implementar en la clase handler base.
    """
    _nombre: str
    _nivel_geografico: str
    _next_handler: Handler = None

    def __init__(self, p_nombre: str, nivel_geografico: str):
        self._nombre = p_nombre
        self._nivel_geografico = nivel_geografico

    def set_sucesor(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def entregar_envio(self, nivel_geografico: str) -> str:
        if self.es_mi_zona(nivel_geografico):
            return f'   La entrega del paquete es responsabilidad de la sucursal {self._nombre} \n' \
                   f'   es una entrega a nivel {self._nivel_geografico}'
        elif self._next_handler:
            return self._next_handler.entregar_envio(nivel_geografico)
        return None

    def es_mi_zona(self, nivel_geografico_destino: str) -> bool:
        return self._nivel_geografico == nivel_geografico_destino


# (CONCRETEHANDLER1) define un manejador concreto para las sucursales locales      
class SucursalLocalHandler(AbstractHandler):
    def __init__(self, p_nombre: str):
        super().__init__(p_nombre, NivelArea.NIVEL_LOCAL)


# (CONCRETEHANDLER2) define un manejador concreto para las sucursales municipales      
class SucursalMunicipalHandler(AbstractHandler):
    def __init__(self, p_nombre):
        super().__init__(p_nombre, NivelArea.NIVEL_MUNICIPAL)


# (CONCRETEHANDLER2) define un manejador concreto para las sucursales municipales
class SucursalNacionalHandler(AbstractHandler):
    def __init__(self, p_nombre):
        super().__init__(p_nombre, NivelArea.NIVEL_NACIONAL)
