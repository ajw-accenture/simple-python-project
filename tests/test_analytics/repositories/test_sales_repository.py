import unittest
from analytics.repositories.sales_repository import SalesRepository


class TestSalesRepository(unittest.TestCase):
    def test_should_have_expected_columns(self):
        sales = SalesRepository.get_sales_for_product('tires')

        first_sale = sales[0]

        self.assertIn('product', first_sale)
        self.assertIn('units_sold', first_sale)
        self.assertIn('unit_price', first_sale)
        self.assertIn('unit_price_currency', first_sale)
