from collections import Counter
from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(inventory_data):
        simple_report = SimpleReport.generate(inventory_data)

        company_products_qty = []
        for product in inventory_data:
            company_products_qty.append(product["nome_da_empresa"])

        result_company_products_qty = Counter(company_products_qty)

        format_report_companies = [
            f"- {key}: {value}\n"
            for (key, value) in result_company_products_qty.items()
        ]

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{''.join(map(str, format_report_companies))}"
        )
