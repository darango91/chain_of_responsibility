
import cliente as cl

from sucursales import serviprisa as sp
from sucursales.constans import NivelArea


if __name__ == '__main__':
    cliente_del_correo = cl.Cliente()

    sucursal_cali_sur = sp.SucursalLocalHandler('CaliSur')
    sucursal_cali = sp.SucursalMunicipalHandler('Cali')
    sucursal_bogota = sp.SucursalNacionalHandler('Bogota_Nacional')

    sucursal_cali_sur.set_sucesor(sucursal_cali)
    sucursal_cali.set_sucesor(sucursal_bogota)

    print("Cadena: LOCAL")
    cliente_del_correo.solicitar_despacho(sucursal_cali_sur, NivelArea.NIVEL_LOCAL)

    print("Cadena: LOCAL > MUNICIPAL")
    cliente_del_correo.solicitar_despacho(sucursal_cali_sur, NivelArea.NIVEL_MUNICIPAL)

    print("Cadena: LOCAL > MUNICIPAL > NACIONAL")
    cliente_del_correo.solicitar_despacho(sucursal_cali_sur, NivelArea.NIVEL_NACIONAL)

    print("Intento Envio internacional, cadena: LOCAL > MUNICIPAL > NACIONAL > ???")
    cliente_del_correo.solicitar_despacho(sucursal_cali_sur, NivelArea.NIVEL_INTERNACIONAL)

    # Cierre de la cadena de responsabilidad, genera un ciclo infinito si no encuentra un responsable
    # de darle manejo a la peticion.
    # sucursal_bogota.set_sucesor(sucursal_cali_sur)
    #
    # print("Intento Envio internacional, cadena: LOCAL > MUNICIPAL > NACIONAL > LOCAL")
    # cliente_del_correo.solicitar_despacho(sucursal_cali_sur, NivelArea.NIVEL_INTERNACIONAL)
