from datetime import date


class SimpleReport:
    @classmethod
    def generate(cls, inventory_data):
        today = date.today()

        oldest_fabrication_date = min(
            [product["data_de_fabricacao"] for product in inventory_data]
        )

        closest_validate_date = min(
            [
                product["data_de_validade"]
                for product in inventory_data
                if product["data_de_validade"] >= str(today)
            ]
        )

        company_name = [product["nome_da_empresa"] for product in inventory_data]

        company_most_products = max(set(company_name), key=company_name.count)

        return (
            f"Data de fabricação mais antiga: {oldest_fabrication_date}\n"
            f"Data de validade mais próxima: {closest_validate_date}\n"
            f"Empresa com mais produtos: {company_most_products}"
        )
