from odoo_methods import read_partners, create_partner, update_partner
def main():
    # Leer socios
    print("Leyendo socios...")
    partner_data = read_partners([28, 29, 32])
    print(f"Socios consultados: {partner_data}")

    # Crear un nuevo socio
    print("Creando nuevo socio...")
    new_customer = {
        'name': 'John Doe',
        'phone': '1234567890',
        'email': 'johndoe@example.com',
        'comment': 'New customer created via XML-RPC',
    }
    new_customer_id = create_partner(new_customer)
    print(f"Nuevo socio creado con ID: {new_customer_id}")

    # Actualizar un socio existente
    print("Actualizando socio...")
    updated = update_partner(32, {
        'phone': '0987654321',
        'email': 'john.doe.updated@example.com',
        'comment': 'Updated via XML-RPC',
    })
    print(f"Socio actualizado: {updated}")

if __name__ == '__main__':
    main()
