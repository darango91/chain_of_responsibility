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
    implementar en la clase handler base (abstracta).
    """
    _nombre: str
    _nivel_geografico: str
    _next_handler: Handler = None

    def __init__(self, p_nombre: str):
        self._nombre = p_nombre

    def set_sucesor(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def entregar_envio(self, nivel_geografico: str) -> str:
        if self._next_handler:
            return self._next_handler.entregar_envio(nivel_geografico)
        return None

    def es_mi_zona(self, nivel_geografico_destino: str) -> bool:
        return self._nivel_geografico == nivel_geografico_destino


# (CONCRETEHANDLER1) define un manejador concreto para las sucursales locales      
class SucursalLocalHandler(AbstractHandler):
    def __init__(self, p_nombre: str):
        self._nivel_geografico = NivelArea.NIVEL_LOCAL
        super().__init__(p_nombre)

    def entregar_envio(self, nivel_geografico: str) -> str:
        if self.es_mi_zona(nivel_geografico):
            return f'   La entrega del paquete es responsabilidad de la sucursal {self._nombre} \n' \
                   f'   es una entrega a nivel {self._nivel_geografico}'
        else:
            return super().entregar_envio(nivel_geografico)


# (CONCRETEHANDLER2) define un manejador concreto para las sucursales municipales      
class SucursalMunicipalHandler(AbstractHandler):
    def __init__(self, p_nombre: str):
        self._nivel_geografico = NivelArea.NIVEL_MUNICIPAL
        super().__init__(p_nombre)

    def entregar_envio(self, nivel_geografico: str) -> str:
        if self.es_mi_zona(nivel_geografico):
            return f'   La entrega del paquete es responsabilidad de la sucursal {self._nombre} \n' \
                   f'   es una entrega a nivel {self._nivel_geografico}'
        else:
            return super().entregar_envio(nivel_geografico)


# (CONCRETEHANDLER3) define un manejador concreto para las sucursales nacionales
class SucursalNacionalHandler(AbstractHandler):
    _nivel_geografico = NivelArea.NIVEL_NACIONAL

    def entregar_envio(self, nivel_geografico: str) -> str:
        if self.es_mi_zona(nivel_geografico):
            return f'   La entrega del paquete es responsabilidad de la sucursal {self._nombre} \n' \
                   f'   es una entrega a nivel {self._nivel_geografico}'
        else:
            return super().entregar_envio(nivel_geografico)