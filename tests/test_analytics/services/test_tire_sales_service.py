import unittest
from analytics.services.tire_sales_service import TireSalesService


class TestTireSalesService(unittest.TestCase):
    def test_should_add_sales_column(self):
        sales = TireSalesService.get_tire_sales(2022)

        first_sale = sales[0]

        self.assertIn('sales', first_sale)

    def test_should_calculate_sales(self):
        sales = TireSalesService.get_tire_sales(2022)

        first_sale = sales[0]
        expected_sale_value = 51_500 * 400.00
        actual_sale_value = first_sale['sales']

        self.assertEqual(actual_sale_value, expected_sale_value)
