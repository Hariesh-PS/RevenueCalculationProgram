import unittest
import os
from datetime import datetime
from revenue import calculate_monthly_revenue, calculate_product_revenue, calculate_customer_revenue, calculate_top_customers

class TestRevenue(unittest.TestCase):

    def test_calculate_monthly_revenue(self):
        expected_result = {
            '2022-02': 1645.0,
            '2022-03': 100.0,
        }
        result = calculate_monthly_revenue('orders.csv')
        self.assertEqual(result, expected_result)

    def test_calculate_product_revenue(self):
        expected_result = {
            '001': 60.0,
            '002': 150.0,
            '003': 120.0,
            '004': 300.0,
            '005': 70.0,
            '006': 15.0,
            '007': 50.0,
            '008': 70.0,
            '009': 100.0,
            '010': 135.0,
            '011': 40.0,
            '012': 30.0,
            '013': 150.0,
            '014': 55.0,
            '015': 80.0,
            '016': 40.0,
            '017': 40.0,
            '018': 30.0,
            '019': 70.0,
            '020': 50.0,
            '021': 90.0,
        }
        result = calculate_product_revenue('orders.csv')
        self.assertEqual(result, expected_result)

    def test_calculate_customer_revenue(self):
        expected_result = {
            '1234': 40.0,
            '5678': 50.0,
            '9012': 120.0,
            '3456': 20.0,
            '7890': 120.0,
            '1235': 35.0,
            '5679': 100.0,
            '9013': 15.0,
            '3457': 60.0,
            '7891': 50.0,
            '1244': 70.0,
            '5688': 60.0,
            '9022': 90.0,
            '3466': 35.0,
            '7880': 40.0,
            '1334': 120.0,
            '5778': 130.0,
            '9112': 240.0,
            '3556': 200.0,
            '7990': 150.0,
        }
        result = calculate_customer_revenue('orders.csv')
        self.assertEqual(result, expected_result)

    def test_calculate_top_customers(self):
        expected_result = [
           {'customer_id': '9112', 'revenue': 240.0},
           {'customer_id': '3556', 'revenue': 200.0},
           {'customer_id': '7990', 'revenue': 150.0},
           {'customer_id': '5778', 'revenue': 130.0},
           {'customer_id': '9012', 'revenue': 120.0},
           {'customer_id': '7890', 'revenue': 120.0},
           {'customer_id': '1334', 'revenue': 120.0},
           {'customer_id': '5679', 'revenue': 100.0},
           {'customer_id': '9022', 'revenue': 90.0},
           {'customer_id': '1244', 'revenue': 70.0},
        ]
        result = calculate_top_customers('orders.csv', 10)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
