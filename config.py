import xmlrpc.client

# Configuración general para conectarse a Odoo
ODOO_URL = 'http://odoodev.dish.com.mx:8069/'
ODOO_DB = 'odood_db'
ODOO_USERNAME = 'admin'
ODOO_PASSWORD = 'dfa7cd1203b06bb8a145a35e33f89a42c6354008'

def get_odoo_connection():
    """Establece la conexión al servidor Odoo."""
    try:
        # Conexión al servidor común
        common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
        print("Odoo Version:", common.version())
        
        # Autenticación
        uid = common.authenticate(ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD, {})
        if not uid:
            raise Exception("Error en la autenticación: Verifica las credenciales")
        
        # Conexión al servidor de objetos
        models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
        return models, uid
    except Exception as e:
        raise ConnectionError(f"Error al conectar a Odoo: {e}")

