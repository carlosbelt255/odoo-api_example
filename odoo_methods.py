from config import get_odoo_connection

def read_partners(partner_ids):
    """
    Lee registros de socios (res.partner) en Odoo.
    :param partner_ids: Lista de IDs de socios a leer
    :return: Lista de socios con los campos especificados
    """
    try:
        models, uid = get_odoo_connection()
        return models.execute_kw(
            'odood_db', uid, 'dfa7cd1203b06bb8a145a35e33f89a42c6354008',
            'res.partner', 'read',
            [partner_ids],
            {'fields': ['name', 'phone', 'country_id', 'comment', 'function', 'email']}
        )
    except Exception as e:
        print(f"Error al leer socios: {e}")
        return None

def create_partner(data):
    """
    Crea un nuevo socio (res.partner) en Odoo.
    :param data: Diccionario con los campos del socio
    :return: ID del socio creado
    """
    try:
        models, uid = get_odoo_connection()
        return models.execute_kw(
            'odood_db', uid, 'dfa7cd1203b06bb8a145a35e33f89a42c6354008',
            'res.partner', 'create',
            [data]
        )
    except Exception as e:
        print(f"Error al crear socio: {e}")
        return None

def update_partner(partner_id, data):
    """
    Actualiza un socio existente (res.partner) en Odoo.
    :param partner_id: ID del socio a actualizar
    :param data: Diccionario con los campos a actualizar
    :return: True si se actualizó, False si no
    """
    try:
        models, uid = get_odoo_connection()
        return models.execute_kw(
            'odood_db', uid, 'dfa7cd1203b06bb8a145a35e33f89a42c6354008',
            'res.partner', 'write',
            [[partner_id], data]
        )
    except Exception as e:
        print(f"Error al actualizar socio: {e}")
        return False
