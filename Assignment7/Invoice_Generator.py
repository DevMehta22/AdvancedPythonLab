import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table
from datetime import datetime
import os

def load_orders(file):
    try:
        required_columns = ['Order ID', 'Customer Name', 'Product Name', 'Quantity', 'Unit Price']

        df = pd.read_csv(file, usecols=required_columns)

        df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
        df['Unit Price'] = pd.to_numeric(df['Unit Price'], errors='coerce')
        
        df.dropna(subset=['Quantity', 'Unit Price'], inplace=True)
        
        orders = df.to_dict('records')
        return orders
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except ValueError as e:
        print(f"Error in data conversion: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
    return None

def create_pdf_with_table(order, folder):
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)

        pdf_path = os.path.join(folder, f"invoice_{order['Order ID']}.pdf")
        doc = SimpleDocTemplate(pdf_path, pagesize=A4)

        table_data = [
            ["Invoice Number", order['Order ID']],
            ["Date of Purchase", datetime.now().strftime('%Y-%m-%d')],
            ["Customer Name", order['Customer Name']],
            ["Product Name", order['Product Name']],
            ["Quantity", order['Quantity']],
            ["Unit Price", f"${order['Unit Price']:.2f}"],
            ["Total Amount", f"${order['Quantity'] * order['Unit Price']:.2f}"]
        ]

        invoice_table = Table(table_data)

        doc.build([invoice_table])

        print(f"Invoice created: {pdf_path}")

    except PermissionError:
        print(f"Error: Permission denied while creating invoice '{order['Order ID']}'.")
    except Exception as e:
        print(f"An unexpected error occurred while generating the invoice for order {order['Order ID']}: {e}")

def generate_invoices():
    orders_file = 'orders.csv'
    orders = load_orders(orders_file)
    if orders is None or len(orders) == 0:
        print("No valid orders found to process. Exiting.")
        return
    invoices_folder = 'invoices'
    for order in orders:
        try:
            create_pdf_with_table(order, invoices_folder)
        except Exception as e:
            print(f"An error occurred while processing order {order['Order ID']}: {e}")

try:
    generate_invoices()
except Exception as e:
    print(f"An unexpected error occurred in the process: {e}")
