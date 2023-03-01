from analytics.views.tire_sales_view import TireSalesView
import unittest
from bs4 import BeautifulSoup

class TestTireSalesView(unittest.TestCase):
    def test_should_render_data_as_table(self):
        view_html = TireSalesView.get_tire_sales_view()
        parsed_html = BeautifulSoup(view_html, 'html.parser')

        headers = parsed_html.select('table > thead > tr > th')
        first_row_cells = parsed_html.select('table > tbody > tr:first-child > td')

        self.assertEqual(headers[0].string, 'Product')
        self.assertEqual(headers[1].string, 'Sales')
        self.assertEqual(headers[2].string, 'Currency')

        self.assertEqual(first_row_cells[0].string, 'Off-Road Tires 25-inch')
        self.assertEqual(first_row_cells[1].string, f'{51_500 * 400.00}')
        self.assertEqual(first_row_cells[2].string, 'USD')


