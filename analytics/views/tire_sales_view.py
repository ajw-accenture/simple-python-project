from analytics.services.tire_sales_service import TireSalesService
from analytics.views.helpers.view_builder import build_full_page

class TireSalesView():

    @staticmethod
    def get_tire_sales_view():
        sales = TireSalesService.get_tire_sales(2022)

        html_table = '<table><thead><tr><th>Product</th><th>Sales</th><th>Currency</th></tr></thead><tbody>'
        for sale in sales:
            product = sale['product']
            sales_value = sale['sales']
            currency = sale['unit_price_currency']
            html_table = f'{html_table}<tr>'
            html_table = f'{html_table}<td>{product}</td>'
            html_table = f'{html_table}<td>{sales_value}</td>'
            html_table = f'{html_table}<td>{currency}</td>'
            html_table = f'{html_table}</tr>'

        html_table = f'{html_table}</tbody></table>'

        return build_full_page(html_table)
