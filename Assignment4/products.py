import csv
import os


def read_sales_data(directory):
    sales_data = []
    # Use os to iterate over all files in the directory and subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv') and 'sales' in file:
                file_path=root+'\\'+file
                print(file_path)
                with open(file_path, newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        sales_data.append(row)
    return sales_data

def process_sales_data(sales_data):
    total_sales = {}
    for row in sales_data:
        product_id = row['Product ID']
        quantity_sold = int(row['Quantity sold'])
        if product_id in total_sales:
            total_sales[product_id] += quantity_sold
        else:
            total_sales[product_id] = quantity_sold
    return total_sales

def get_top_5_products(total_sales):
    sorted_sales = sorted(total_sales.items(), key=lambda x: x[1], reverse=True)
    return sorted_sales[:5]

def create_sales_summary(product_names, total_sales, top_products, sales_data):
    summary_data = []
    
    for product_id, total_quantity_sold in top_products:
        product_name = product_names.get(product_id, "Unknown Product")
        months = set(row['Date'][:7] for row in sales_data)  
        months_count = len(months)
        average_quantity_per_month = total_quantity_sold / months_count

        summary_data.append({
            'Product ID': product_id,
            'Product Name': product_name,
            'Total Quantity Sold': total_quantity_sold,
            'Average Quantity Sold per month': average_quantity_per_month
        })

    return summary_data

def read_product_names(file_path):
    product_names = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product_names[row['Product ID']] = row['Product Name']
    return product_names

def write_sales_summary(file_path, summary_data):
    with open(file_path, mode='w', newline='') as csvfile:
        fieldnames = ['Product ID', 'Product Name', 'Total Quantity Sold', 'Average Quantity Sold per month']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(summary_data)

sales_data_directory = 'sales_data'

sales_data = read_sales_data(sales_data_directory)

product_names = read_product_names('product_names.csv')

total_sales = process_sales_data(sales_data)

top_products = get_top_5_products(total_sales)

sales_summary = create_sales_summary(product_names, total_sales, top_products, sales_data)

write_sales_summary('sales_summary.csv', sales_summary)

print("Sales summary CSV file has been created.")
