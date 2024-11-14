import pandas as pd
from fpdf import FPDF
from datetime import datetime
import os

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Invoice", 0, 1, "C")

    def add_table_row(self, label, value):
        self.set_font("Arial", "", 10)
        self.cell(50, 10, label, border=1)
        self.cell(0, 10, str(value), border=1, ln=True)

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
        pdf = PDF()
        pdf.add_page()

        pdf.add_table_row("Invoice Number", order['Order ID'])
        pdf.add_table_row("Date of Purchase", datetime.now().strftime('%Y-%m-%d'))
        pdf.add_table_row("Customer Name", order['Customer Name'])
        pdf.add_table_row("Product Name", order['Product Name'])
        pdf.add_table_row("Quantity", order['Quantity'])
        pdf.add_table_row("Unit Price", f"${order['Unit Price']:.2f}")
        pdf.add_table_row("Total Amount", f"${order['Quantity'] * order['Unit Price']:.2f}")

        pdf.output(pdf_path)
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

print("Name: Dev Mehta\nRoll No: 22BCP282")

try:
    generate_invoices()
except Exception as e:
    print(f"An unexpected error occurred in the process: {e}")
