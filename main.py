
import cliente as cl

from sucursales import serviprisa as sp
from sucursales.constans import NivelArea


if __name__ == '__main__':
    cliente_del_correo = cl.Cliente()

    # Empieza con el manejador local. Hasta aquí, no hay cadena de responsabilidad.
    # Todas las peticiones serán resueltas por el mismo objeto.

    sucursal_cali_sur = sp.SucursalLocalHandler('CaliSur')
    sucursal_cali = sp.SucursalMunicipalHandler('Cali')
    sucursal_bogota = sp.SucursalNacionalHandler('Bogota_Nacional')

    sucursal_cali_sur.set_sucesor(sucursal_cali).set_sucesor(sucursal_bogota)

    print("Cadena LOCAL")
    cliente_del_correo.solicitar_despacho(sucursal_cali_sur, NivelArea.NIVEL_LOCAL)

    print("Cadena LOCAL > MUNICIPAL")
    cliente_del_correo.solicitar_despacho(sucursal_cali_sur, NivelArea.NIVEL_MUNICIPAL)

    print("Cadena LOCAL > MUNICIPAL > NACIONAL")
    cliente_del_correo.solicitar_despacho(sucursal_cali_sur, NivelArea.NIVEL_NACIONAL)

    print("Envio internacional")
    cliente_del_correo.solicitar_despacho(sucursal_cali_sur, NivelArea.NIVEL_INTERNACIONAL)

