import json
import csv
import os

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

# Змініть шляхи до JSON та CSV файлів на потрібні вам
output_directory = r"C:\6 sem\DW\csvresource"

# Виклики функції json_to_csv для кожного JSON-файлу
json_to_csv('order.json', os.path.join(output_directory, 'orders.csv'))
json_to_csv('trading_point.json', os.path.join(output_directory, 'traiding_point.csv'))
json_to_csv('brand.json', os.path.join(output_directory, 'vendor_brand.csv'))
json_to_csv('address.json', os.path.join(output_directory, 'address.csv'))
json_to_csv('contract.json', os.path.join(output_directory, 'contract.csv'))
json_to_csv('personal_data.json', os.path.join(output_directory, 'person.csv'))
json_to_csv('payment.json', os.path.join(output_directory, 'payment.csv'))
json_to_csv('customer.json', os.path.join(output_directory, 'customer.csv'))
json_to_csv('manager.json', os.path.join(output_directory, 'manager.csv'))
json_to_csv('consultation.json', os.path.join(output_directory, 'consultation.csv'))
json_to_csv('storage.json', os.path.join(output_directory, 'storage.csv'))
json_to_csv('reminder.json', os.path.join(output_directory, 'scheduled_reminder.csv'))


