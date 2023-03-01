from analytics.repositories.sales_repository import SalesRepository

class TireSalesService():

    @staticmethod
    def get_tire_sales(fiscal_year):
        sales = SalesRepository.get_sales_for_product('tires')

        for sale in sales:
            sale['sales'] = sale['unit_price'] * sale['units_sold']

        return sales
