

class Cliente:
    def solicitar_despacho(self, p_sucursal_contactada, p_nivel_geografico_destino):
        resultado = p_sucursal_contactada.entregar_envio(p_nivel_geografico_destino)

        if resultado:
            print(f"{resultado}")
        else:
            print(f"    El destino {p_nivel_geografico_destino} no es alcanzable aun")
