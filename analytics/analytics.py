from flask import Flask
from analytics.views.tire_sales_view import TireSalesView

analytics = Flask(__name__)

@analytics.route("/sales/tires", methods=['GET'])
def view_tire_sales():
    return TireSalesView.get_tire_sales_view()
