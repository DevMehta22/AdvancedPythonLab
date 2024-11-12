import os
import json

def read_json_files(directory):
    json_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root,file)
                
                with open(file_path,'r') as f:
                    try:
                        data = json.load(f)
                        json_files.append(data)
                    except json.JSONDecodeError:
                        print(f"Error: unable to parse {file_path}")
    
    return json_files

def process_data_and_store(json_data, output_file):
    
    output_data = []

    for data in json_data:
        for i in data:
            country_data = {
                "country": i['country'],
                "total_cases": i['confirmed_cases']['total'],
                "total_deaths": i['deaths']['total'],
                "total_recovered": i['recovered']['total'],
                "total_active_cases": i['confirmed_cases']['total'] - (i['deaths']['total'] + i['recovered']['total'])
            }
            output_data.append(country_data)
    
    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=4)
    
    return output_data


directory = '/Users/devmehta/Desktop/LAB_sem5/Python_prg/python_main/Assignment5/Covid_data'

json_data = read_json_files(directory)
output_file = 'covid_summary.json'
processed_data = process_data_and_store(json_data, output_file)
sorted_data = sorted(processed_data, key=lambda x: x["total_cases"], reverse=True)
for i in range(5):
     print(sorted_data[i]['country'],':',sorted_data[i]['total_cases'])  

print("\n")
for i in range(-5,0):
    print(sorted_data[i]['country'],':',sorted_data[i]['total_cases']) 

