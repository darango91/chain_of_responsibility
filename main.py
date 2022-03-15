
import cliente as cl

from sucursales import serviprisa as sp
from sucursales.constans import AREA_NIVEL


if __name__ == '__main__':
    cliente_del_correo = cl.Cliente()

    # Empieza con el manejador local. Hasta aquí, no hay cadena de responsabilidad.
    # Todas las peticiones serán resueltas por el mismo objeto.
    sucursal_cali = sp.SucursalMunicipal(None, 'Cali')
    sucursal_cali_sur = sp.SucursalLocal(sucursal_cali, 'CaliSur')

    cliente_del_correo.solicitar_despacho(sucursal_cali_sur, AREA_NIVEL["NIVEL_MUNICIPAL"])

    # Note como el cliente de correo puede usar directamente la sucursal municipal,
    # demostrando el bajo acoplamiento del emisor con el receptor.
    cliente_del_correo.solicitar_despacho(sucursal_cali, AREA_NIVEL["NIVEL_MUNICIPAL"])
