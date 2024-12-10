from flask import Flask, request, jsonify
from odoo_methods import read_partners, create_partner, update_partner, read_all_partners, read_all_products
import json

app = Flask(__name__)

@app.route('/partners/all', methods=['GET'])
def get_all_partners():
    """
    Endpoint para obtener todos los socios registrados.
    Ejemplo de uso en Postman:
    - GET http://localhost:5000/partners/all
    """
    try:
        # Llamar al método en Odoo para leer todos los socios
        response = read_all_partners()
        return jsonify(json.loads(response))
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/products/all', methods=['GET'])
def get_all_products():
    """
    Endpoint para obtener todos los socios registrados.
    Ejemplo de uso en Postman:
    - GET http://localhost:5000/products/all
    """
    try:
        # Llamar al método en Odoo para leer todos los socios
        response = read_all_products()
        return jsonify(json.loads(response))
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/partners', methods=['GET'])
def get_partners():
    """
    Endpoint para obtener socios por IDs.
    Ejemplo de uso en Postman:
    - GET http://localhost:5000/partners?ids=28,29,32
    """
    ids = request.args.get('ids')
    if not ids:
        return jsonify({"status": "error", "message": "Faltan los IDs de los socios"}), 400
    
    try:
        partner_ids = list(map(int, ids.split(',')))
        response = read_partners(partner_ids)
        return jsonify(json.loads(response))
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/partners', methods=['POST'])
def create_new_partner():
    """
    Endpoint para crear un nuevo socio.
    Ejemplo de uso en Postman:
    - POST http://localhost:5000/partners
    - Body (JSON):
      {
          "name": "John Doe",
          "phone": "1234567890",
          "email": "johndoe@example.com",
          "comment": "New customer created via API"
      }
    """
    data = request.json
    if not data:
        return jsonify({"status": "error", "message": "Faltan los datos del socio"}), 400
    
    try:
        response = create_partner(data)
        return jsonify(json.loads(response))
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/partners/<int:partner_id>', methods=['PUT'])
def update_existing_partner(partner_id):
    """
    Endpoint para actualizar un socio existente.
    Ejemplo de uso en Postman:
    - PUT http://localhost:5000/partners/32
    - Body (JSON):
      {
          "phone": "0987654321",
          "email": "john.doe.updated@example.com",
          "comment": "Updated via API"
      }
    """
    data = request.json
    if not data:
        return jsonify({"status": "error", "message": "Faltan los datos para actualizar"}), 400
    
    try:
        response = update_partner(partner_id, data)
        return jsonify(json.loads(response))
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
