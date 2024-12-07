import json
from config import get_odoo_connection

def read_partners(partner_ids):
    """
    Lee registros de socios (res.partner) en Odoo.
    :param partner_ids: Lista de IDs de socios a leer
    :return: JSON con los socios leídos o un mensaje de error
    """
    try:
        models, uid = get_odoo_connection()
        partners = models.execute_kw(
            'odood_db', uid, 'dfa7cd1203b06bb8a145a35e33f89a42c6354008',
            'res.partner', 'read',
            [partner_ids],
            {'fields': ['name', 'phone', 'country_id', 'comment', 'function', 'email']}
        )
        return json.dumps({
            "status": "success",
            "data": partners
        })
    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": f"Error al leer socios: {e}"
        })

def create_partner(data):
    """
    Crea un nuevo socio (res.partner) en Odoo.
    :param data: Diccionario con los campos del socio
    :return: JSON con el ID del socio creado o un mensaje de error
    """
    try:
        models, uid = get_odoo_connection()
        partner_id = models.execute_kw(
            'odood_db', uid, 'dfa7cd1203b06bb8a145a35e33f89a42c6354008',
            'res.partner', 'create',
            [data]
        )
        return json.dumps({
            "status": "success",
            "partner_id": partner_id
        })
    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": f"Error al crear socio: {e}"
        })

def update_partner(partner_id, data):
    """
    Actualiza un socio existente (res.partner) en Odoo.
    :param partner_id: ID del socio a actualizar
    :param data: Diccionario con los campos a actualizar
    :return: JSON indicando si se actualizó correctamente o un mensaje de error
    """
    try:
        models, uid = get_odoo_connection()
        success = models.execute_kw(
            'odood_db', uid, 'dfa7cd1203b06bb8a145a35e33f89a42c6354008',
            'res.partner', 'write',
            [[partner_id], data]
        )
        return json.dumps({
            "status": "success" if success else "error",
            "message": "Socio actualizado correctamente" if success else "No se pudo actualizar el socio"
        })
    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": f"Error al actualizar socio: {e}"
        })
