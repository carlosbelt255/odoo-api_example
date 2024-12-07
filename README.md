# Proyecto Odoo API Integration

Este proyecto es una integración simple con la API de Odoo usando XML-RPC. Permite interactuar con el sistema Odoo para realizar operaciones CRUD (Crear, Leer, Actualizar) sobre los modelos de datos, específicamente sobre los registros de socios (`res.partner`), y realizar otras acciones como la creación de productos y clientes.

## Recursos

- **Python 3.x**: El proyecto está desarrollado en Python, utilizando bibliotecas estándar.
- **xmlrpc.client**: Utilizado para realizar las solicitudes a la API de Odoo a través de XML-RPC.
- **Odoo API (XML-RPC)**: El sistema Odoo proporciona una API basada en XML-RPC para interactuar con su backend.
- **Odoo Instance**: La instancia de Odoo a la que se conecta el script debe estar en funcionamiento para realizar las solicitudes.

## ¿Qué hace este sistema?

Este sistema realiza las siguientes acciones principales:

1. **Leer socios**: Obtiene información de socios existentes en Odoo a partir de sus IDs.
2. **Crear nuevos socios**: Permite la creación de nuevos clientes en el sistema Odoo proporcionando un conjunto de datos.
3. **Actualizar socios**: Permite modificar la información de un socio ya existente en el sistema, como el teléfono, correo electrónico y comentarios.
4. **Registrar productos**: Se puede agregar nuevos productos al inventario de Odoo.

### Funcionalidades adicionales:
- El sistema está preparado para recibir parámetros de entrada dinámicos, lo que facilita la personalización de las operaciones.
- Se manejan excepciones para evitar errores y brindar retroalimentación si algo sale mal.

## Requisitos

- Python 3.x
- Dependencias:
  - `xmlrpc.client` (que viene por defecto en Python 3.x)

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. Instala las dependencias necesarias (si las hay):

    ```bash
    pip install -r requirements.txt
    ```

3. Asegúrate de tener configurado un servidor Odoo y actualiza los parámetros de conexión en el archivo de configuración.

## Uso

1. Para interactuar con la API de Odoo, simplemente ejecuta el archivo `main.py`:

    ```bash
    python main.py
    ```

2. Las funciones de lectura, creación y actualización de socios son llamadas dentro del código y se pueden personalizar según las necesidades.
