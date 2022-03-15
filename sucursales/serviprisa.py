from sucursales.constans import AREA_NIVEL


# (HANDLER) define la interfaz para los manejadores de la cadena de responsabilidad
class ISucursal:

    def __init__(self, p_sucesor=None, p_nombre=None, p_nivel_geografico=AREA_NIVEL["NO_NIVEL"]):
        self._sucesor = p_sucesor
        self.nombre = p_nombre
        self.nivel_geografico = p_nivel_geografico
    
    def entregar_envio(self, p_nivel_geografico):
        # define el reenvío generico de la responsabilidad al sucesor
        if self._sucesor:
            self._sucesor.entregar_envio(p_nivel_geografico)
        else:
            print(f'La entrega del paquete es responsabilidad de la sucursal {self.nombre}')
            print('Se usará el método de entrega por defecto')
            
    def es_mi_nivel_geografico(self, p_nivel_geografico_destino):
        return self.nivel_geografico == p_nivel_geografico_destino
            
    def establecer_sucesor(self, p_sucesor):
        self._sucesor = p_sucesor


# (CONCRETEHANDLER1) define un manejador concreto para las sucursales locales      
class SucursalLocal(ISucursal):

    def __init__(self, p_sucesor, p_nombre):
        super().__init__(p_sucesor, p_nombre, AREA_NIVEL["NIVEL_LOCAL"])
    
    def entregar_envio(self, p_nivel_geografico_destino):
        # Maneja la responsabilidad
        if self.es_mi_nivel_geografico(p_nivel_geografico_destino):
            print(f'La entrega del paquete es responsabilidad de la sucursal {self.nombre}')
            print('Se usará el método de entrega del nivel local')
        else:
            # Reenvía la responsabilidad al siguiente sucesor de la cadena, usando el método definido en la interfaz
            super().entregar_envio(p_nivel_geografico_destino)


# (CONCRETEHANDLER2) define un manejador concreto para las sucursales municipales      
class SucursalMunicipal(ISucursal):
    
    def __init__(self, p_sucesor, p_nombre):
        super().__init__(p_sucesor, p_nombre, AREA_NIVEL["NIVEL_MUNICIPAL"])
        
    def entregar_envio(self, p_nivel_geografico_destino):
        # Maneja la responsabilidad
        if self.es_mi_nivel_geografico(p_nivel_geografico_destino):
            print(f'La entrega del paquete es responsabilidad de la sucursal {self.nombre}')
            print('Se usará el método de entrega del nivel municipal')
        else:
            # Reenvía la responsabilidad al siguiente sucesor de la cadena, usando el método definido en la interfaz
            super().entregar_envio(p_nivel_geografico_destino)
