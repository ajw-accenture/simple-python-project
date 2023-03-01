class SalesRepository():

    @staticmethod
    def get_sales_for_product(product):
        # Typically this is where a query is run on a database.

        # query thing here.

        return [
            {'product': 'Off-Road Tires 25-inch', 'units_sold': 51_500, 'unit_price': 400.00, 'unit_price_currency': 'USD'},
            {'product': 'All Weather Tires 17-inch', 'units_sold': 150_000, 'unit_price': 120.00, 'unit_price_currency': 'USD'},
            {'product': 'Racing Tires 17-inch', 'units_sold': 15_000, 'unit_price': 550.00, 'unit_price_currency': 'USD'}
        ]
