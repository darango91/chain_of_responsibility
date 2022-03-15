

class Cliente:

    def __init__(self):
        pass

    def solicitar_despacho(self, p_sucursal_contactada, p_nivel_geografico_destino):
        p_sucursal_contactada.entregar_envio(p_nivel_geografico_destino)
