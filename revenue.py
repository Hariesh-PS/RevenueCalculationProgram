import csv
import time
from datetime import datetime


def calculate_monthly_revenue(csv_file):
    monthly_revenue = {}
    with open(csv_file) as file:
        reader = csv.reader(file)
        header = next(reader) # skip header row
        for row in reader:
            order_id, customer_id, order_date, product_id, product_name, product_price, quantity = row
            order_date = datetime.strptime(order_date, '%Y-%m-%d') # convert string to datetime object
            revenue = float(product_price) * int(quantity) # calculate revenue
            # update monthly revenue dictionary
            month_key = order_date.strftime('%Y-%m')
            if month_key not in monthly_revenue:
                monthly_revenue[month_key] = revenue
            else:
                monthly_revenue[month_key] += revenue
    return monthly_revenue


def calculate_product_revenue(csv_file):
    product_revenue = {}
    with open(csv_file) as file:
        reader = csv.reader(file)
        header = next(reader) # skip header row
        for row in reader:
            order_id, customer_id, order_date, product_id, product_name, product_price, quantity = row
            revenue = float(product_price) * int(quantity) # calculate revenue
            # update product revenue dictionary
            if product_id not in product_revenue:
                product_revenue[product_id] = revenue
            else:
                product_revenue[product_id] += revenue
    return product_revenue


def calculate_customer_revenue(csv_file):
    customer_revenue = {}
    with open(csv_file) as file:
        reader = csv.reader(file)
        header = next(reader) # skip header row
        for row in reader:
            order_id, customer_id, order_date, product_id, product_name, product_price, quantity = row
            revenue = float(product_price) * int(quantity) # calculate revenue
            # update customer revenue dictionary
            if customer_id not in customer_revenue:
                customer_revenue[customer_id] = revenue
            else:
                customer_revenue[customer_id] += revenue
    return customer_revenue


def calculate_top_customers(csv_file, num_customers):
    customer_revenue = {}
    with open(csv_file) as file:
        reader = csv.reader(file)
        header = next(reader) # skip header row
        for row in reader:
            order_id, customer_id, order_date, product_id, product_name, product_price, quantity = row
            revenue = float(product_price) * int(quantity) # calculate revenue
            # update customer revenue dictionary
            if customer_id not in customer_revenue:
                customer_revenue[customer_id] = revenue
            else:
                customer_revenue[customer_id] += revenue
    top_customers = sorted(customer_revenue.items(), key=lambda x: x[1], reverse=True)[:num_customers]
    result = [{'customer_id': c, 'revenue': r} for c, r in top_customers]
    return result


monthly_revenue = calculate_monthly_revenue('orders.csv')
print("monthly_revenue", monthly_revenue, "\n")

product_revenue = calculate_product_revenue('orders.csv')
print("product_revenue",product_revenue, "\n")

customer_revenue = calculate_customer_revenue('orders.csv')
print("customer_revenue", customer_revenue, "\n")

top_customers = calculate_top_customers('orders.csv', 10)
print("top_customers",top_customers, "\n")
