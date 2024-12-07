from odoo_methods import read_partners, create_partner, update_partner
def main():
    # Leer socios
    print("Leyendo socios...")
    partner_data = read_partners([28, 29, 32])
    print(f"Socios consultados: {partner_data}")

if __name__ == '__main__':
    main()
